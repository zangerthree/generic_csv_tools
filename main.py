import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Step 1: Merge CSV files
print("Step 1: Merging CSV files...")
subprocess.run([os.sys.executable, os.path.join(SCRIPT_DIR, "csv_merger.py")])

# Step 2: Remove 01000 suffix
print("\nStep 2: Removing '01000' suffix...")
subprocess.run([os.sys.executable, os.path.join(SCRIPT_DIR, "csv_remove_01000_333EJK.py")])

# Step 3: Deduplicate
print("\nStep 3: Removing duplicates...")
subprocess.run([os.sys.executable, os.path.join(SCRIPT_DIR, "csv_deduplicator.py")])

# Step 4: remove from list
print("\nStep 4: Removing from list in to_remove.txt...")
subprocess.run([os.sys.executable, os.path.join(SCRIPT_DIR, "remove_from_list.py")])

# Step 5: Split to columns
print("\nStep 5: Splitting to columns (1000 per column)...")
subprocess.run([os.sys.executable, os.path.join(SCRIPT_DIR, "split_to_columns.py")])

print("\nAll steps completed!")
