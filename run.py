import itertools
import subprocess

# Define the possible values for each argument
ckpt_ids = [
    # "stabilityai/stable-diffusion-3-medium-diffusers",
    # "PixArt-alpha/PixArt-Sigma-XL-2-1024-MS",
    # "fal/AuraFlow",
    "black-forest-labs/FLUX.1-dev",
    "black-forest-labs/FLUX.1-schnell",
]

torch_dtypes = [
    # "fp32",
    "fp16",
    "bf16",
]
qtypes = ["fp8", "int8", "int4", "none"]
batch_sizes = [1]  # You can add more sizes if needed
qte_options = [0, 1]
fuse_options = [0, 1]
exclude_layers_options = [
    [],
    # ["layer1"],
    # ["layer2"],
    # ["layer1", "layer2"],
]  # Adjust as needed

# Generate all combinations of the arguments
combinations = itertools.product(
    ckpt_ids,
    torch_dtypes,
    qtypes,
    batch_sizes,
    qte_options,
    fuse_options,
    exclude_layers_options,
)

# Run benchmark.py for each combination
for combination in combinations:
    ckpt_id, torch_dtype, qtype, batch_size, qte, fuse, exclude_layers = combination

    exclude_layers_str = " ".join(exclude_layers)
    command = [
        "python",
        "benchmark.py",
        "--ckpt_id",
        ckpt_id,
        "--torch_dtype",
        torch_dtype,
        "--qtype",
        qtype,
        "--batch_size",
        str(batch_size),
        "--qte",
        str(qte),
        "--fuse",
        str(fuse),
    ]
    if exclude_layers_str:
        command.extend(["--exclude_layers"] + exclude_layers)

    print(f"Running: {' '.join(command)}")
    subprocess.run(command)
