import os
import argparse
from optimum.quanto import freeze, qfloat8, qint4, qint8, quantize
import torch
import json
import torch.utils.benchmark as benchmark
from diffusers import DiffusionPipeline
import gc

json_dir_path = "./experiment_results"  # Change this to the directory where your JSON files are stored
os.makedirs(json_dir_path, exist_ok=True)

WARM_UP_ITERS = 5
PROMPT = "a photo of an astronaut riding a horse on mars"

TORCH_DTYPES = {"fp32": torch.float32, "fp16": torch.float16, "bf16": torch.bfloat16}
QTYPES = {"fp8": qfloat8, "int8": qint8, "int4": qint4, "none": None}
# QTYPES = {"fp8": qfloat8, "int8": qint8, "none": None}

PREFIXES = {
    "stabilityai/stable-diffusion-3-medium-diffusers": "sd3",
    "PixArt-alpha/PixArt-Sigma-XL-2-1024-MS": "pixart",
    "fal/AuraFlow": "auraflow",
    "black-forest-labs/FLUX.1-dev": "flux-dev",
    "black-forest-labs/FLUX.1-schnell": "flux-schnell",
}


def flush():
    """Wipes off memory."""
    gc.collect()
    torch.cuda.empty_cache()
    torch.cuda.reset_max_memory_allocated()
    torch.cuda.reset_peak_memory_stats()


def load_pipeline(
    ckpt_id, torch_dtype, qtype=None, exclude_layers=None, qte=False, fuse=False
):
    pipe = DiffusionPipeline.from_pretrained(ckpt_id, torch_dtype=torch_dtype).to(
        "cuda"
    )
    if fuse:
        pipe.transformer.fuse_qkv_projections()

    if qtype:
        quantize(pipe.transformer, weights=qtype, exclude=exclude_layers)
        freeze(pipe.transformer)

        if qte:
            quantize(pipe.text_encoder, weights=qtype)
            freeze(pipe.text_encoder)
            if hasattr(pipe, "text_encoder_2"):
                quantize(pipe.text_encoder_2, weights=qtype)
                freeze(pipe.text_encoder_2)
            if hasattr(pipe, "text_encoder_3"):
                quantize(pipe.text_encoder_3, weights=qtype)
                freeze(pipe.text_encoder_3)

    pipe.set_progress_bar_config(disable=True)
    return pipe


def run_inference(pipe, batch_size=1):
    _ = pipe(
        prompt=PROMPT,
        num_images_per_prompt=batch_size,
        generator=torch.manual_seed(0),
    )


def benchmark_fn(f, *args, **kwargs):
    t0 = benchmark.Timer(
        stmt="f(*args, **kwargs)", globals={"args": args, "kwargs": kwargs, "f": f}
    )
    return f"{(t0.blocked_autorange().mean):.3f}"


def bytes_to_giga_bytes(bytes):
    return f"{(bytes / 1024 / 1024 / 1024):.3f}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ckpt_id",
        type=str,
        default="stabilityai/stable-diffusion-3-medium-diffusers",
        choices=list(PREFIXES.keys()),
    )
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument(
        "--torch_dtype", type=str, default="fp16", choices=list(TORCH_DTYPES.keys())
    )
    parser.add_argument(
        "--qtype", type=str, default="none", choices=list(QTYPES.keys())
    )
    parser.add_argument("--qte", type=int, default=0, help="Quantize text encoder")
    parser.add_argument("--fuse", type=int, default=0)
    parser.add_argument(
        "--exclude_layers", metavar="N", type=str, nargs="*", default=None
    )
    args = parser.parse_args()

    flush()

    ckpt_id = PREFIXES[args.ckpt_id]
    img_name = f"ckpt@{ckpt_id}-bs@{args.batch_size}-dtype@{args.torch_dtype}-qtype@{args.qtype}-qte@{args.qte}-fuse@{args.fuse}"
    if os.path.exists(f"{img_name}.png"):
        print(f"Skipping {img_name}.png")
        exit()

    print(
        f"Running with ckpt_id: {args.ckpt_id}, batch_size: {args.batch_size}, torch_dtype: {args.torch_dtype}, qtype: {args.qtype}, qte: {bool(args.qte)}, {args.exclude_layers=}, {args.fuse=}"
    )
    pipeline = load_pipeline(
        ckpt_id=args.ckpt_id,
        torch_dtype=TORCH_DTYPES[args.torch_dtype],
        qtype=QTYPES[args.qtype],
        exclude_layers=args.exclude_layers,
        qte=args.qte,
        fuse=bool(args.fuse),
    )

    for _ in range(WARM_UP_ITERS):
        run_inference(pipeline, args.batch_size)

    time = benchmark_fn(run_inference, pipeline, args.batch_size)
    torch.cuda.empty_cache()
    memory = bytes_to_giga_bytes(torch.cuda.memory_allocated())  # in GBs.
    print(
        f"ckpt: {args.ckpt_id} batch_size: {args.batch_size}, qte: {args.qte}, {args.exclude_layers=} "
        f"torch_dtype: {args.torch_dtype}, qtype: {args.qtype}  in {time} seconds and {memory} GBs."
    )
    if args.exclude_layers:
        exclude_layers = "_".join(args.exclude_layers)
        img_name += f"-exclude@{exclude_layers}"
    image = pipeline(
        prompt=PROMPT,
        num_images_per_prompt=args.batch_size,
        generator=torch.manual_seed(0),
    ).images[0]
    image_path = os.path.join(json_dir_path, f"{img_name}.png")
    image.save(image_path)

    info = dict(
        batch_size=args.batch_size,
        memory=memory,
        time=time,
        dtype=args.torch_dtype,
        qtype=args.qtype,
        qte=args.qte,
        exclude_layers=args.exclude_layers,
        fuse=args.fuse,
    )
    info_file = os.path.join(json_dir_path, f"{img_name}_info.json")
    with open(info_file, "w") as f:
        json.dump(info, f)
