import os
import json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Set the paths
json_files_path = "./experiment_results"  # Directory where your JSON files are stored
output_dir = "./assets"  # Directory where your plots will be saved

# Initialize lists to store data
batch_sizes = []
memories = []
times = []
dtypes = []
qtypes = []
qtes = []
fuses = []
exclude_layers = []
filenames = []
images = []

# Read all JSON files and extract data
for filename in os.listdir(json_files_path):
    if filename.endswith("_info.json"):
        with open(os.path.join(json_files_path, filename), "r") as f:
            data = json.load(f)
            batch_sizes.append(data["batch_size"])
            memories.append(float(data["memory"]))
            times.append(float(data["time"]))
            dtypes.append(data["dtype"])
            qtypes.append(data["qtype"])
            qtes.append(data["qte"])
            fuses.append(data["fuse"])
            exclude_layers.append(data["exclude_layers"])
            filenames.append(filename)
            image_filename = filename.replace("_info.json", ".png")
            image_path = os.path.join(json_files_path, image_filename)
            images.append(image_path)

# Convert x_data strings to numeric indices
x_data_labels = [f"{dtype}-{qtype}" for dtype, qtype in zip(dtypes, qtypes)]
unique_labels = list(sorted(set(x_data_labels)))
x_data_indices = [unique_labels.index(label) for label in x_data_labels]


# Scatter plot with images
def plot_images_scatter(
    x_data, y_data, x_label, y_label, title, images, filename, x_ticks
):
    plt.figure(figsize=(15, 10))
    plt.scatter(x_data, y_data, marker="o", s=100)

    for i, image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.resize((50, 50))  # Resize for display purposes

        # Offset the image slightly from the point it represents
        plt.imshow(
            image,
            aspect="auto",
            extent=(x_data[i] - 0.5, x_data[i] + 0.5, y_data[i] - 0.5, y_data[i] + 0.5),
            zorder=1,
        )

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(ticks=range(len(x_ticks)), labels=x_ticks, rotation=45, ha="right")
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to the specified file
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()


# Example of plotting images on a scatter plot with dtype vs qtype
y_data = times
x_label = "Dtype-Quantization Type"
y_label = "Inference Time (s)"
title = "Inference Time vs Dtype-Quantization Type with Images"
filename = "scatter_time_vs_dtype_qtype_with_images.png"

plot_images_scatter(
    x_data=x_data_indices,
    y_data=y_data,
    x_label=x_label,
    y_label=y_label,
    title=title,
    images=images,
    filename=filename,
    x_ticks=unique_labels,
)

# Another example: Memory usage vs Dtype-Quantization Type
y_data = memories
y_label = "Memory Usage (GB)"
title = "Memory Usage vs Dtype-Quantization Type with Images"
filename = "scatter_memory_vs_dtype_qtype_with_images.png"

plot_images_scatter(
    x_data=x_data_indices,
    y_data=y_data,
    x_label=x_label,
    y_label=y_label,
    title=title,
    images=images,
    filename=filename,
    x_ticks=unique_labels,
)
