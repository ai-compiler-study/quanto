import os
import json

# Set the paths
json_files_path = "./experiment_results"  # Directory where your JSON files are stored
output_md_path = "./README.md"  # Path to the output README.md file

# Initialize lists to store data
results = []

# Read all JSON files and extract data
for filename in os.listdir(json_files_path):
    if filename.endswith("_info.json"):
        with open(os.path.join(json_files_path, filename), "r") as f:
            data = json.load(f)
            # Extract model name from filename
            model_name = filename.split("-")[0].replace("ckpt@", "")
            data["model_name"] = model_name
            results.append(data)


# Function to generate markdown table
def generate_markdown_table(headers, rows):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        table += "| " + " | ".join(str(x) for x in row) + " |\n"
    return table


# Function to sort and generate tables
def create_sorted_tables(table_headers, table_rows, sort_by):
    sorted_by_memory = sorted(table_rows, key=lambda x: float(x[sort_by["memory"]]))
    sorted_by_latency = sorted(table_rows, key=lambda x: float(x[sort_by["latency"]]))

    table_memory_md = generate_markdown_table(table_headers, sorted_by_memory)
    table_latency_md = generate_markdown_table(table_headers, sorted_by_latency)

    return table_memory_md, table_latency_md


# Headers for the tables
table_headers = [
    "Model Name",
    "Batch Size",
    "Quantization",
    "Quantize TE",
    "Memory (GB)",
    "Latency (Seconds)",
]

# Prepare rows for the first table
table_rows = []

for result in results:
    table_rows.append(
        [
            result["model_name"],
            result["batch_size"],
            result["qtype"].upper(),
            "True" if result["qte"] else "False",
            result["memory"],
            result["time"],
        ]
    )

# Sort and create tables
table_1_memory_md, table_1_latency_md = create_sorted_tables(
    table_headers, table_rows, {"memory": 4, "latency": 5}
)

# Prepare rows for the second table
table_2_headers = [
    "Model Name",
    "Batch Size",
    "Quantization",
    "Memory (GB)",
    "Latency (Seconds)",
]
table_2_rows = []

for result in results:
    if result["qte"] == 0:  # Only include rows where qte is False
        table_2_rows.append(
            [
                result["model_name"],
                result["batch_size"],
                result["qtype"].upper(),
                result["memory"],
                result["time"],
            ]
        )

# Sort and create tables
table_2_memory_md, table_2_latency_md = create_sorted_tables(
    table_2_headers, table_2_rows, {"memory": 3, "latency": 4}
)

# Prepare rows for the third table (example with Quantize TE 1, 2, 3 columns)
table_3_headers = [
    "Model Name",
    "Batch Size",
    "Quantization",
    "Quantize TE 1",
    "Quantize TE 2",
    "Quantize TE 3",
    "Memory (GB)",
    "Latency (Seconds)",
]
table_3_rows = []

for result in results:
    # Add dummy Quantize TE 1, 2, 3 values for demonstration
    qte_1 = 1 if result["qte"] == 1 else 0
    qte_2 = 1 if result["qte"] == 1 else 0
    qte_3 = 1 if result["qte"] == 1 else 0

    table_3_rows.append(
        [
            result["model_name"],
            result["batch_size"],
            result["qtype"].upper(),
            qte_1,
            qte_2,
            qte_3,
            result["memory"],
            result["time"],
        ]
    )

# Sort and create tables
table_3_memory_md, table_3_latency_md = create_sorted_tables(
    table_3_headers, table_3_rows, {"memory": 6, "latency": 7}
)

# Write to README.md
with open(output_md_path, "w") as md_file:
    md_file.write("# Experiment Results\n\n")

    md_file.write("## Table 1 (Sorted by Memory)\n\n")
    md_file.write(table_1_memory_md + "\n")

    md_file.write("## Table 1 (Sorted by Latency)\n\n")
    md_file.write(table_1_latency_md + "\n")

    md_file.write("## Table 2 (Sorted by Memory)\n\n")
    md_file.write(table_2_memory_md + "\n")

    md_file.write("## Table 2 (Sorted by Latency)\n\n")
    md_file.write(table_2_latency_md + "\n")

    md_file.write("## Table 3 (Sorted by Memory)\n\n")
    md_file.write(table_3_memory_md + "\n")

    md_file.write("## Table 3 (Sorted by Latency)\n\n")
    md_file.write(table_3_latency_md + "\n")
