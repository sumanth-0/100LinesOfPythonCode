"""
CSV Column Summarizer
Author: Diya Satish Kumar
Reads a CSV file and calculates sums, averages, and counts for numeric columns.
"""

import csv
import statistics

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def summarize_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        data = {col: [] for col in columns}

        for row in reader:
            for col in columns:
                val = row[col].strip()
                if is_float(val):
                    data[col].append(float(val))

    print(f"\n📊 Summary for '{filename}'")
    print(f"{'Column':20} {'Count':>8} {'Sum':>12} {'Average':>12}")
    print("-" * 50)

    for col, values in data.items():
        if values:
            count = len(values)
            total = sum(values)
            avg = statistics.mean(values)
            print(f"{col:20} {count:8} {total:12.2f} {avg:12.2f}")

    print("\n✅ Done!")

if __name__ == "__main__":
    filename = input("Enter CSV filename (with path): ").strip()
    try:
        summarize_csv(filename)
    except FileNotFoundError:
        print("⚠️ File not found. Please check the path.")
    except Exception as e:
        print(f"⚠️ Error: {e}")