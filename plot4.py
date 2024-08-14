import os
import json
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def read_json_files(input_dir):
    results = []
    for filename in os.listdir(input_dir):
        if filename.endswith("_info.json"):
            try:
                with open(os.path.join(input_dir, filename), "r") as f:
                    info = json.load(f)
                parsed = parse_filename(filename.replace("_info.json", ""))
                if parsed is None:
                    print(f"Failed to parse filename: {filename}")
                    continue
                results.append(
                    {
                        **parsed,
                        "memory": float(info["memory"]),
                        "time": float(info["time"]),
                    }
                )
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file {filename}")
            except KeyError as e:
                print(f"Missing key in JSON file {filename}: {str(e)}")
    return pd.DataFrame(results)


def plot_memory_latency_scatter(df, output_dir):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        data=df,
        x="memory",
        y="time",
        hue="ckpt",
        style="qtype",
        size="bs",
        sizes=(50, 200),
    )
    plt.title("Memory vs Latency Comparison")
    plt.xlabel("Memory Usage (GB)")
    plt.ylabel("Latency (Seconds)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "memory_vs_latency_comparison.png"))
    plt.close()


def plot_quantization_comparison(df, metric, output_dir):
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=df, x="ckpt", y=metric, hue="qtype")
    plt.title(f"{metric.capitalize()} by Quantization Method")
    plt.xlabel("Model")
    plt.ylabel(metric.capitalize())
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{metric}_by_quantization_method.png"))
    plt.close()


def plot_te_quantization_effect(df, metric, output_dir):
    df["te_quantized"] = df["qte"].astype(bool)
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="ckpt", y=metric, hue="te_quantized")
    plt.title(f"Effect of Text Encoder Quantization on {metric.capitalize()}")
    plt.xlabel("Model")
    plt.ylabel(metric.capitalize())
    plt.xticks(rotation=45)
    plt.legend(title="Text Encoder Quantized", labels=["No", "Yes"])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"effect_of_te_quantization_on_{metric}.png"))
    plt.close()


def plot_fuse_effect(df, metric, output_dir):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="ckpt", y=metric, hue="fuse")
    plt.title(f"Effect of QKV Fusion on {metric.capitalize()}")
    plt.xlabel("Model")
    plt.ylabel(metric.capitalize())
    plt.xticks(rotation=45)
    plt.legend(title="QKV Fusion", labels=["No", "Yes"])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"effect_of_qkv_fusion_on_{metric}.png"))
    plt.close()


def main():
    input_dir = "experiment_results"
    output_dir = "visualizations"
    os.makedirs(output_dir, exist_ok=True)

    df = read_json_files(input_dir)

    print("Unique checkpoints found:", df["ckpt"].unique())
    print("Data shape:", df.shape)

    plot_memory_latency_scatter(df, output_dir)
    plot_quantization_comparison(df, "memory", output_dir)
    plot_quantization_comparison(df, "time", output_dir)
    plot_te_quantization_effect(df, "memory", output_dir)
    plot_te_quantization_effect(df, "time", output_dir)
    plot_fuse_effect(df, "memory", output_dir)
    plot_fuse_effect(df, "time", output_dir)

    print(
        "Visualizations have been generated and saved in the 'visualizations' directory."
    )


if __name__ == "__main__":
    main()
