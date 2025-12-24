import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "_cleaned.csv")
REMOVE_FILE = os.path.join(SCRIPT_DIR, "to_remove.txt")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "_removed.csv")

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

if not os.path.exists(REMOVE_FILE):
    raise FileNotFoundError(f"Remove file not found: {REMOVE_FILE}")

# Read values to remove from to_remove.txt
values_to_remove = set()
with open(REMOVE_FILE, mode="r", encoding="utf-8") as f:
    for line in f:
        value = line.strip()
        if value:  # Skip empty lines
            values_to_remove.add(value)

print(f"Loaded {len(values_to_remove)} values to remove from {REMOVE_FILE}")

rows_removed = 0

# Remove rows from _cleaned.csv where first column matches values in to_remove.txt
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        
        for row in reader:
            if row:  # Skip empty rows
                first_col_value = row[0]
                
                # Check if value should be removed
                if first_col_value in values_to_remove:
                    rows_removed += 1
                    print(f"Removed: {first_col_value}")
                else:
                    writer.writerow(row)

print(f"\nRemoved {rows_removed} rows matching values in to_remove.txt")
print(f"Output saved to: {OUTPUT_FILE}")
