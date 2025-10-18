#!/usr/bin/env python3
"""
Auto CSV Cleaner - Clean CSV files by removing empty rows, duplicate rows, and fixing missing values.
Usage: python auto_csv_cleaner.py <input_file> [output_file] [--strategy STRATEGY]
"""

import argparse
import csv
import sys
from pathlib import Path

def clean_csv(input_file, output_file=None, missing_strategy='remove'):
    """
    Clean CSV file by removing empty rows, duplicates, and handling missing values.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file (default: input_cleaned.csv)
        missing_strategy: Strategy for missing values - 'remove', 'fill', or 'keep'
    """
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: File '{input_file}' not found")
        return False
    
    if output_file is None:
        output_file = input_path.stem + '_cleaned' + input_path.suffix
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            rows = list(reader)
        
        print(f"Original rows: {len(rows)}")
        
        # Remove completely empty rows
        rows = [row for row in rows if any(cell.strip() for cell in row)]
        print(f"After removing empty rows: {len(rows)}")
        
        # Remove duplicate rows
        seen = set()
        unique_rows = []
        for row in rows:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_rows.append(row)
        rows = unique_rows
        print(f"After removing duplicates: {len(rows)}")
        
        # Handle missing values
        if missing_strategy == 'remove':
            rows = [row for row in rows if all(cell.strip() for cell in row)]
            print(f"After removing rows with missing values: {len(rows)}")
        elif missing_strategy == 'fill':
            for row in rows:
                for i in range(len(row)):
                    if not row[i].strip():
                        row[i] = 'N/A'
            print("Filled missing values with 'N/A'")
        
        # Write cleaned data
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)
            writer.writerows(rows)
        
        print(f"\nCleaned CSV saved to: {output_file}")
        return True
    
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Clean CSV files by removing empty rows, duplicates, and handling missing values'
    )
    parser.add_argument('input', help='Input CSV file path')
    parser.add_argument('output', nargs='?', help='Output CSV file path (optional)')
    parser.add_argument(
        '--strategy', 
        choices=['remove', 'fill', 'keep'],
        default='remove',
        help='Strategy for missing values: remove rows, fill with N/A, or keep as-is (default: remove)'
    )
    
    args = parser.parse_args()
    success = clean_csv(args.input, args.output, args.strategy)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
