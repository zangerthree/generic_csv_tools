import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "_removed.csv")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "_final.csv")

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

# Read first column values
values = []
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    
    for row in infile:
        if row.strip():  # Skip empty lines
            first_col = row.split(',')[0].strip('"')  # Extract first column
            values.append(first_col)

print(f"Loaded {len(values)} values from {INPUT_FILE}")

# Split into groups of 1000 and write as columns
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    
    # Create header row with column names
    num_columns = (len(values) + 999) // 1000  # Ceiling division
    headers = [f"Column_{i+1}" for i in range(num_columns)]
    writer.writerow(headers)
    
    # Write data split into columns of 1000 rows each
    for row_idx in range(1000):
        row_data = []
        for col_idx in range(num_columns):
            value_idx = col_idx * 1000 + row_idx
            if value_idx < len(values):
                row_data.append(values[value_idx])
            else:
                row_data.append("")  # Empty cell if we run out of values
        writer.writerow(row_data)

print(f"Created {num_columns} columns with up to 1000 rows each")
print(f"Output saved to: {OUTPUT_FILE}")
