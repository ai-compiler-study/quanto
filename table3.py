import os
import json
import logging
import argparse
from collections import defaultdict
import matplotlib.pyplot as plt
from PIL import Image
import re
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_filename(filename):
    pattern = r"ckpt@([\w-]+)-bs@(\d+)-dtype@(\w+)-qtype@(\w+)-qte@(\d+)-fuse@(\d+)"
    match = re.match(pattern, filename)
    if match:
        return {
            "ckpt": match.group(1),
            "bs": int(match.group(2)),
            "dtype": match.group(3),
            "qtype": match.group(4),
            "qte": int(match.group(5)),
            "fuse": int(match.group(6)),
        }
    return None


def create_image_grid(images, titles, output_filename, grid_size):
    rows, cols = grid_size
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
    fig.suptitle("Quantization Comparison", fontsize=16)

    for idx, (img_path, title) in enumerate(zip(images, titles)):
        row = idx // cols
        col = idx % cols
        ax = axes[row, col] if rows > 1 else axes[col]

        img = Image.open(img_path)
        ax.imshow(img)
        ax.set_title(title, fontsize=8)
        ax.axis("off")

    # Hide any unused subplots
    for idx in range(len(images), rows * cols):
        row = idx // cols
        col = idx % cols
        ax = axes[row, col] if rows > 1 else axes[col]
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.close()


def generate_grids(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = [
        f
        for f in os.listdir(input_dir)
        if f.endswith(".png") and not f.endswith("_info.json")
    ]

    # Group images by checkpoint and dtype
    groups = {}
    for img_file in image_files:
        parsed = parse_filename(img_file)
        if parsed:
            key = (parsed["ckpt"], parsed["dtype"])
            if key not in groups:
                groups[key] = []
            groups[key].append((img_file, parsed))

    for (ckpt, dtype), group in groups.items():
        # Sort images by qtype, qte, and fuse
        sorted_group = sorted(
            group, key=lambda x: (x[1]["qtype"], x[1]["qte"], x[1]["fuse"])
        )

        images = [os.path.join(input_dir, img[0]) for img in sorted_group]
        titles = [
            f"qtype: {img[1]['qtype']}, qte: {img[1]['qte']}, fuse: {img[1]['fuse']}"
            for img in sorted_group
        ]

        # Determine grid size
        n = len(images)
        cols = min(3, n)
        rows = math.ceil(n / cols)
        grid_size = (rows, cols)

        output_filename = os.path.join(output_dir, f"{ckpt}_{dtype}_comparison.png")
        create_image_grid(images, titles, output_filename, grid_size)
        logger.info(f"Created grid for {ckpt} with {dtype}: {output_filename}")


def write_sorted_table(file, configs, sort_key):
    file.write(
        "| Quantization | Quantize TE | Fuse QKV | Memory (GB) | Latency (s) |\n"
    )
    file.write(
        "|--------------|-------------|----------|-------------|-------------|\n"
    )

    sorted_configs = sorted(configs.items(), key=lambda x: x[1][sort_key])

    for (qtype, qte, fuse), metrics in sorted_configs:
        qte_str = "Yes" if qte else "No"
        fuse_str = "Yes" if fuse else "No"
        file.write(
            f"| {qtype.upper() or 'None':<12} | {qte_str:<11} | {fuse_str:<8} | {metrics['memory']:<11.3f} | {metrics['time']:<11.3f} |\n"
        )

    file.write("\n")


def generate_markdown(input_dir, output_file, image_grids_dir):
    results = defaultdict(lambda: defaultdict(dict))

    for filename in os.listdir(input_dir):
        if filename.endswith("_info.json"):
            try:
                with open(os.path.join(input_dir, filename), "r") as f:
                    info = json.load(f)

                parsed = parse_filename(filename.replace("_info.json", ""))
                if parsed is None:
                    continue

                key = (parsed["ckpt"], parsed["bs"], parsed["dtype"])
                config = (parsed["qtype"], parsed["qte"], parsed["fuse"])

                results[key][config] = {
                    "memory": float(info["memory"]),
                    "time": float(info["time"]),
                }
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON from file {filename}")
            except KeyError as e:
                logger.error(f"Missing key in JSON file {filename}: {str(e)}")

    with open(output_file, "w") as readme:
        readme.write("# Experiment Results\n\n")

        for (ckpt, bs, dtype), configs in results.items():
            readme.write(
                f"## {ckpt.capitalize()} - Batch Size: {bs}, Data Type: {dtype}\n\n"
            )

            # Add image grid
            grid_filename = f"{ckpt}_{dtype}_comparison.png"
            if os.path.exists(os.path.join(image_grids_dir, grid_filename)):
                readme.write(
                    f"![{ckpt} {dtype} Comparison](http://localhost:8000/{image_grids_dir}/{grid_filename})\n\n"
                )

            # Generate table sorted by memory
            readme.write("### Sorted by Memory Usage (Ascending)\n\n")
            write_sorted_table(readme, configs, sort_key="memory")

            # Generate table sorted by latency
            readme.write("### Sorted by Latency (Ascending)\n\n")
            write_sorted_table(readme, configs, sort_key="time")

            readme.write("\n")

    logger.info(f"Markdown with image grids generated and written to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate grid images and markdown with tables from experiment results"
    )
    parser.add_argument(
        "--input",
        default="experiment_results",
        help="Input directory containing experiment results",
    )
    parser.add_argument("--output", default="README3.md", help="Output README file")
    parser.add_argument(
        "--image-grids", default="image_grids", help="Output directory for image grids"
    )
    args = parser.parse_args()

    # Generate image grids
    generate_grids(args.input, args.image_grids)

    # Generate README with tables and image grid references
    generate_markdown(args.input, args.output, args.image_grids)

    print("\nTo view the markdown file with images:")
    print(
        "1. Open a terminal in the directory containing your README.md, experiment_results, and image_grids folders"
    )
    print("2. Run the following command to start a local HTTP server:")
    print("   python -m http.server")
    print("3. Open a web browser and go to http://localhost:8000")
    print("4. Click on the README.md file to view it with images")
