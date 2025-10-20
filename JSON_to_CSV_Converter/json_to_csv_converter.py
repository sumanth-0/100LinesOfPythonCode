"""
JSON to CSV Converter
=====================
Simple utility to convert JSON files to CSV format.
Supports nested JSON and automatic flattening.

Features:
- Handles nested JSON structures
- Automatic column detection
- Pretty formatting
- Error handling
- File validation

Usage:
    python json_to_csv_converter.py input.json output.csv
"""

import json
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any

def flatten_json(nested_json: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flatten nested JSON structure"""
    items = []
    for key, value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            items.append((new_key, ', '.join(map(str, value))))
        else:
            items.append((new_key, value))
    
    return dict(items)

def convert_json_to_csv(json_file: str, csv_file: str) -> bool:
    """Convert JSON file to CSV"""
    try:
        # Validate input file
        if not Path(json_file).exists():
            print(f"❌ Error: File '{json_file}' not found")
            return False
        
        # Read JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle single object or array
        if isinstance(data, dict):
            data = [data]
        
        if not data:
            print("⚠️  Warning: JSON file is empty")
            return False
        
        # Flatten all records
        flattened_data = [flatten_json(record) for record in data]
        
        # Get all unique keys for columns
        all_keys = set()
        for record in flattened_data:
            all_keys.update(record.keys())
        
        columns = sorted(all_keys)
        
        # Write CSV
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(flattened_data)
        
        print(f"✅ Successfully converted '{json_file}' to '{csv_file}'")
        print(f"📊 Rows: {len(flattened_data)}, Columns: {len(columns)}")
        return True
        
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in '{json_file}'")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("📝 Usage: python json_to_csv_converter.py <input.json> <output.csv>")
        print("\n💡 Example: python json_to_csv_converter.py data.json output.csv")
        sys.exit(1)
    
    json_file = sys.argv[1]
    csv_file = sys.argv[2]
    
    # Ensure output has .csv extension
    if not csv_file.endswith('.csv'):
        csv_file += '.csv'
    
    success = convert_json_to_csv(json_file, csv_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
