# JSON to CSV Converter 📊

A simple yet powerful utility to convert JSON files to CSV format with support for nested structures.

## Features ✨

- **Nested JSON Support**: Automatically flattens nested JSON structures
- **Smart Column Detection**: Identifies all unique keys across records
- **List Handling**: Converts arrays to comma-separated values
- **Error Handling**: Comprehensive validation and error messages
- **Clean Output**: Well-formatted CSV files ready for analysis

## Usage 🚀

### Basic Usage

```bash
python json_to_csv_converter.py input.json output.csv
```

### Example

**Input JSON** (`data.json`):
```json
[
  {
    "name": "Alice",
    "age": 30,
    "address": {
      "city": "New York",
      "country": "USA"
    },
    "hobbies": ["reading", "coding"]
  },
  {
    "name": "Bob",
    "age": 25,
    "address": {
      "city": "London",
      "country": "UK"
    },
    "hobbies": ["gaming", "music"]
  }
]
```

**Command**:
```bash
python json_to_csv_converter.py data.json output.csv
```

**Output CSV** (`output.csv`):
```csv
address_city,address_country,age,hobbies,name
New York,USA,30,"reading, coding",Alice
London,UK,25,"gaming, music",Bob
```

## How It Works 🔧

1. **Read JSON**: Loads JSON data from file
2. **Flatten Structure**: Converts nested objects using underscore notation
3. **Extract Columns**: Identifies all unique keys across all records
4. **Write CSV**: Creates properly formatted CSV with headers

## Features in Detail 📋

### Nested Object Flattening
```json
{"user": {"name": "Alice", "age": 30}}
```
Becomes:
```csv
user_name,user_age
Alice,30
```

### Array Handling
```json
{"tags": ["python", "json", "csv"]}
```
Becomes:
```csv
tags
"python, json, csv"
```

### Multiple Records
Handles both single objects and arrays of objects automatically.

## Error Handling ⚠️

- Validates file existence
- Checks JSON syntax
- Handles empty files
- Provides clear error messages
- Safe file operations

## Requirements 📦

- Python 3.6+
- Standard library only (no external dependencies)

## Use Cases 💡

1. **Data Analysis**: Convert API responses to CSV for Excel/spreadsheet analysis
2. **Data Migration**: Transform JSON databases to CSV format
3. **Reporting**: Generate CSV reports from JSON logs
4. **Data Cleaning**: Convert and flatten complex JSON structures
5. **Integration**: Prepare JSON data for CSV-based tools

## Limitations ⚡

- Each Python file must be under 100 lines (repository requirement)
- Very deeply nested structures create many columns
- Large files processed in memory

## Tips 💭

- Use descriptive output filenames
- Check column names for nested data
- Review flattened structure for complex JSON
- Consider file size for large datasets

## Example Scenarios 🎯

### API Response to CSV
```bash
# Download data from API
curl https://api.example.com/users > users.json

# Convert to CSV
python json_to_csv_converter.py users.json users.csv
```

### Multiple Files
```bash
for file in *.json; do
    python json_to_csv_converter.py "$file" "${file%.json}.csv"
done
```

## Output Format 📄

- UTF-8 encoding
- Standard CSV format
- Quoted fields when necessary
- Sorted column names for consistency

## Contributing 🤝

Contributions welcome! This is part of the 100LinesOfPythonCode project.

## License 📜

Open source - free to use and modify.

---

**Author**: Contributed for Hacktoberfest 2025
**Project**: 100LinesOfPythonCode
