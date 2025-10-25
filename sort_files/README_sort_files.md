# List Files by Size

This small script `sort_files_by_size.py` lists files in a directory sorted by their size.

Quick usage:

```
python3 sort_files_by_size.py .           # list files (smallest first)
python3 sort_files_by_size.py -r -l .    # recursive and show largest first
python3 sort_files_by_size.py -H .       # human-readable sizes
python3 sort_files_by_size.py -n 10 .    # only first 10 results
```

Options:
- `--recursive` / `-r`: search in subdirectories
- `--largest` / `-l`: show largest files first (default: smallest first)
- `--human` / `-H`: show human-readable sizes (KB, MB)
- `--limit N` / `-n N`: limit number of results

Output:
Each line contains: `SIZE\tFILE_PATH`.

License: follows the repository's license if applicable.
