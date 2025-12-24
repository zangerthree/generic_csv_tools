import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "_merged.csv")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "_deduplicated.csv")

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

seen_first_column = set()
rows_removed = 0

# deletes rows from the CSV where data in the first column are duplicates
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        
        for row in reader:
            if row:  # Skip empty rows
                first_col_value = row[0]
                
                if first_col_value not in seen_first_column:
                    seen_first_column.add(first_col_value)
                    writer.writerow(row)
                else:
                    rows_removed += 1

print(f"Removed {rows_removed} duplicate rows based on first column")
print(f"Output saved to: {OUTPUT_FILE}")
