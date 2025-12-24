import os
import glob
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_PATH = os.path.join(SCRIPT_DIR, "unmerged")

OUTPUT_FILE = os.path.join(SCRIPT_DIR, "_merged.csv")

# Match ANY CSV file in the folder
PATTERN = os.path.join(FOLDER_PATH, "*.csv")

csv_files = glob.glob(PATTERN)
csv_files.sort()

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in: {FOLDER_PATH}")

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as outfile:
    writer = None

    for i, file_path in enumerate(csv_files):
        with open(file_path, mode="r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            header = next(reader)

            if i == 0:
                writer = csv.writer(outfile)
                writer.writerow(header)

            for row in reader:
                writer.writerow(row)

print(f"Merged {len(csv_files)} files into {OUTPUT_FILE}")
