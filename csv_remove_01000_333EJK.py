import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "_merged.csv")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "_cleaned.csv")

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

rows_modified = 0
rows_removed = 0

# removes "01000" and everything after it from the first column
# also removes rows where the first column starts with "33EJK"
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        
        for row in reader:
            if row:  # Skip empty rows
                first_col_value = row[0]
                
                # Remove rows starting with "33EJK"
                if first_col_value.startswith("33EJK"):
                    rows_removed += 1
                    print(f"Removed: {first_col_value} (starts with 33EJK)")
                    continue
                
                # Remove "01000" and everything after it
                if "01000" in first_col_value:
                    cleaned_value = first_col_value.split("01000")[0]
                    row[0] = cleaned_value
                    rows_modified += 1
                    print(f"Cleaned: {first_col_value} -> {cleaned_value}")
                
                writer.writerow(row)

print(f"\nModified {rows_modified} rows by removing '01000' suffix")
print(f"Removed {rows_removed} rows starting with '33EJK'")
print(f"Output saved to: {OUTPUT_FILE}")
