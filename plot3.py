import os
import json
import matplotlib.pyplot as plt
from PIL import Image

# Set the paths
json_files_path = "./experiment_results"  # Directory where your JSON files are stored
output_dir = "./assets"  # Directory where your plots will be saved

# Initialize lists to store data
qte_options = []
fuses = []
dtypes = []
images = []

# Read all JSON files and extract data
for filename in os.listdir(json_files_path):
    if filename.endswith("_info.json"):
        with open(os.path.join(json_files_path, filename), "r") as f:
            data = json.load(f)
            qte_options.append(data["qte"])
            fuses.append(data["fuse"])
            dtypes.append(data["dtype"])
            image_filename = filename.replace("_info.json", ".png")
            image_path = os.path.join(json_files_path, image_filename)
            images.append(image_path)

# Determine unique qte, fuse, and dtype combinations
unique_qte = sorted(set(qte_options))
unique_fuse = sorted(set(fuses))
unique_dtype = sorted(set(dtypes))

# Combine qte and fuse into a single x-axis label
x_labels = [f"qte={qte}\nfuse={fuse}" for qte in unique_qte for fuse in unique_fuse]
x_combinations = [(qte, fuse) for qte in unique_qte for fuse in unique_fuse]

# Create a grid for plotting
fig, ax = plt.subplots(len(unique_dtype), len(x_combinations), figsize=(20, 10))

for i, dtype in enumerate(unique_dtype):
    for j, (qte, fuse) in enumerate(x_combinations):
        # Filter images matching the current qte, fuse, and dtype
        indices = [
            k
            for k in range(len(qte_options))
            if qte_options[k] == qte and fuses[k] == fuse and dtypes[k] == dtype
        ]

        if indices:
            image_path = images[indices[0]]
            image = Image.open(image_path)
            image = image.resize(
                (150, 150), Image.Resampling.LANCZOS
            )  # Increase size and use high-quality resizing
            ax[i, j].imshow(image)
            ax[i, j].set_title(f"qte={qte}\nfuse={fuse}", fontsize=8)
        else:
            ax[i, j].text(
                0.5,
                0.5,
                "No Image",
                horizontalalignment="center",
                verticalalignment="center",
            )

        ax[i, j].axis("off")

# Set x-axis and y-axis labels
for j in range(len(x_combinations)):
    ax[-1, j].set_xlabel(x_labels[j], fontsize=10, rotation=45, ha="right")

for i in range(len(unique_dtype)):
    ax[i, 0].set_ylabel(f"dtype={unique_dtype[i]}", fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grid_plot_all_settings.png"))
plt.show()
