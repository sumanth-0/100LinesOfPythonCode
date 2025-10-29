# Temporary File Cleaner

A Python script to delete old files from a directory based on creation or modification date.

## Usage

```bash
python temp_cleaner.py <path> --days <number_of_days> [--mode created|modified|both] [--dry-run]
```

### Arguments

* `path` : Directory to clean
* `--days` : Delete files older than this many days
* `--mode` : `created`, `modified`, or `both` (default: `both`)
* `--dry-run` : Preview files without deleting

### Example

Preview files older than 30 days:

```bash
python temp_cleaner.py "/tmp" --days 30 --dry-run
```

Delete files older than 15 days based on modified date:

```bash
python temp_cleaner.py "/tmp" --days 15 --mode modified
```
---