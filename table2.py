import os
import json
import logging
import argparse
from collections import defaultdict
import re

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


def create_image_table(images, titles, input_dir):
    table = "<table>\n"
    for i in range(0, len(images), 3):
        table += "<tr>\n"
        for j in range(3):
            if i + j < len(images):
                img_path = f"http://localhost:8000/{input_dir}/{images[i+j]}"
                title = titles[i + j]
                table += f"<td><img src='{img_path}' alt='{title}' width='300'/><br>{title}</td>\n"
        table += "</tr>\n"
    table += "</table>\n"
    return table


def generate_markdown(input_dir, output_file):
    results = defaultdict(lambda: defaultdict(dict))
    image_files = defaultdict(list)
    image_titles = defaultdict(list)

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
        elif filename.endswith(".png"):
            parsed = parse_filename(filename.replace(".png", ""))
            if parsed:
                key = (parsed["ckpt"], parsed["dtype"])
                image_files[key].append(filename)
                image_titles[key].append(
                    f"qtype: {parsed['qtype']}, qte: {parsed['qte']}, fuse: {parsed['fuse']}"
                )

    with open(output_file, "w") as readme:
        readme.write("# Experiment Results\n\n")

        for (ckpt, bs, dtype), configs in results.items():
            readme.write(
                f"## {ckpt.capitalize()} - Batch Size: {bs}, Data Type: {dtype}\n\n"
            )

            # Add image table
            key = (ckpt, dtype)
            if key in image_files:
                readme.write(
                    create_image_table(image_files[key], image_titles[key], input_dir)
                )
                readme.write("\n")

            # Generate table sorted by memory
            readme.write("### Sorted by Memory Usage (Ascending)\n\n")
            write_sorted_table(readme, configs, sort_key="memory")

            # Generate table sorted by latency
            readme.write("### Sorted by Latency (Ascending)\n\n")
            write_sorted_table(readme, configs, sort_key="time")

            readme.write("\n")

    logger.info(f"Markdown with embedded images generated and written to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate markdown with embedded images and tables from experiment results"
    )
    parser.add_argument(
        "--input",
        default="experiment_results",
        help="Input directory containing experiment results and images",
    )
    parser.add_argument("--output", default="README2.md", help="Output markdown file")
    args = parser.parse_args()

    generate_markdown(args.input, args.output)

    print("\nTo view the markdown file with images:")
    print(
        "1. Open a terminal in the directory containing your README.md and experiment_results folder"
    )
    print("2. Run the following command to start a local HTTP server:")
    print("   python -m http.server")
    print("3. Open a web browser and go to http://localhost:8000")
    print("4. Click on the README.md file to view it with images")
