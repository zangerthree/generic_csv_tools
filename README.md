These tools are mostly used for AUPost Unmanifested tickets, but can also be used for any csv merging and deduplication as well if needed.

## Quick Usage
Run `python main.py` to execute all steps in sequence:

## Script Descriptions

**csv_merger.py** - Merges all CSV files from the "unmerged" folder into `Merged.csv`

**csv_remove_01000_suffix.py** - Removes "01000" and everything after it, also removes rows starting with "33EJK", outputs to `Cleaned.csv`

**csv_deduplicator.py** - Removes duplicate rows based on first column values, outputs to `Deduplicated.csv`

**remove_from_list.py** - Removes rows where first column matches values in `to_remove.txt`, outputs to `_removed.csv`

**split_to_columns.py** - Takes first column from `_removed.csv` and splits into columns of 1000 values each, outputs to `_final.csv`

**main.py** - Orchestrates all 5 steps in sequence