# Folder Size Calculator

A minimal Python script that calculates and displays the size of each folder in a directory in human-readable format.

## Features

- **Recursive Size Calculation**: Calculates total size including all subdirectories
- **Human-Readable Format**: Displays sizes in B, KB, MB, GB, TB, PB
- **Sorted Results**: Shows folders sorted by size (largest first)
- **Total Summary**: Displays total size of all folders
- **Error Handling**: Gracefully handles permission errors and missing files

## Usage

### Command Line
```bash
python folder_size_calculator.py [directory]
```

### Interactive Mode
```bash
python folder_size_calculator.py
```

## Example Output

```
Folder Size Calculator
=========================

Calculating folder sizes in: /home/user/projects

Folder sizes in: /home/user/projects
--------------------------------------------------
Folder Name                    Size           
--------------------------------------------------
large_project                  1.2 GB         
media_files                    856.3 MB       
documents                      45.7 MB        
scripts                        2.1 MB         
configs                        156.8 KB       
--------------------------------------------------
Total                          2.1 GB         
```

## Size Units

| Unit | Description |
|------|-------------|
| B    | Bytes |
| KB   | Kilobytes (1,024 B) |
| MB   | Megabytes (1,024 KB) |
| GB   | Gigabytes (1,024 MB) |
| TB   | Terabytes (1,024 GB) |
| PB   | Petabytes (1,024 TB) |

## Use Cases

- **Disk Space Analysis**: Identify which folders consume most space
- **Cleanup Planning**: Find large directories for cleanup
- **Storage Management**: Monitor folder growth over time
- **System Administration**: Quick directory size overview

## Requirements

- Python 3.6+
- No external dependencies

## Error Handling

- Permission denied folders are skipped silently
- Missing or inaccessible files don't break the calculation
- Invalid directories show appropriate error messages

## Performance

- Efficiently walks directory trees
- Handles large directories with many files
- Minimal memory usage during calculation

## Author

Created for issue #786 - 100 Lines of Python Code Project