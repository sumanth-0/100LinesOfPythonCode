# Case-Insensitive Conflict Checker

## Description
Cloning this repository on Windows or default macOS can fail when two files only differ in their letter casing. This tool scans a project directory and reports every location where case-insensitive filesystems would treat multiple entries as the same path.

## Features
- Detects collisions between files and folders that differ only by case.
- Traverses the tree recursively from any starting directory.
- Optional flag to include hidden entries such as `.gitignore`.
- Prints a concise report so collisions can be fixed quickly.

## Requirements
- Python 3.8 or newer.

## Usage
```bash
python Case_Insensitive_Conflict_Checker/case_insensitive_conflict_checker.py
```

### Scan another directory
```bash
python Case_Insensitive_Conflict_Checker/case_insensitive_conflict_checker.py path/to/project
```

### Include hidden files
```bash
python Case_Insensitive_Conflict_Checker/case_insensitive_conflict_checker.py --include-hidden
```

## Example Output
```
Conflicts found under C:\path\to\repo (case-insensitive check):
[scripts]
  - Readme.md, README.md
[tools]
  - helper.py, Helper.py
```

Use the report to rename or consolidate the listed entries so the project works on every platform.
