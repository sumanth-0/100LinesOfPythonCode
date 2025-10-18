#!/usr/bin/env python3
"""
Tiny Log Analyzer - Scan log files and count keyword occurrences
Usage: python log_analyzer.py <log_file> [keywords...]
"""

import sys
import os
from collections import Counter
import argparse


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Scan a log file and count occurrences of specific keywords',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example:\n  python log_analyzer.py server.log ERROR WARNING INFO'
    )
    parser.add_argument('logfile', help='Path to the log file to analyze')
    parser.add_argument('keywords', nargs='+', help='Keywords to search for (case-insensitive)')
    parser.add_argument('-c', '--case-sensitive', action='store_true',
                        help='Make keyword matching case-sensitive')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='Show line numbers where keywords appear')
    return parser.parse_args()


def analyze_log(logfile, keywords, case_sensitive=False, show_lines=False):
    """Analyze log file for keyword occurrences."""
    if not os.path.exists(logfile):
        print(f"Error: File '{logfile}' not found.")
        sys.exit(1)
    
    if not os.path.isfile(logfile):
        print(f"Error: '{logfile}' is not a file.")
        sys.exit(1)
    
    keyword_counts = Counter()
    keyword_lines = {kw: [] for kw in keywords}
    
    try:
        with open(logfile, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                search_line = line if case_sensitive else line.lower()
                
                for keyword in keywords:
                    search_keyword = keyword if case_sensitive else keyword.lower()
                    count = search_line.count(search_keyword)
                    
                    if count > 0:
                        keyword_counts[keyword] += count
                        if show_lines:
                            keyword_lines[keyword].append(line_num)
    
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return keyword_counts, keyword_lines


def display_results(keyword_counts, keyword_lines, show_lines=False):
    """Display analysis results."""
    print("\n" + "="*50)
    print("LOG ANALYSIS RESULTS")
    print("="*50 + "\n")
    
    if not keyword_counts:
        print("No keywords found in the log file.")
        return
    
    for keyword in sorted(keyword_counts.keys(), key=lambda k: keyword_counts[k], reverse=True):
        count = keyword_counts[keyword]
        print(f"{keyword}: {count} occurrence{'s' if count != 1 else ''}")
        
        if show_lines and keyword_lines[keyword]:
            lines_str = ', '.join(map(str, keyword_lines[keyword][:10]))
            if len(keyword_lines[keyword]) > 10:
                lines_str += f" ... ({len(keyword_lines[keyword]) - 10} more)"
            print(f"  Lines: {lines_str}")
    
    print("\n" + "="*50)
    print(f"Total matches: {sum(keyword_counts.values())}")
    print("="*50 + "\n")


def main():
    """Main function."""
    args = parse_arguments()
    keyword_counts, keyword_lines = analyze_log(
        args.logfile, args.keywords, args.case_sensitive, args.lines
    )
    display_results(keyword_counts, keyword_lines, args.lines)


if __name__ == '__main__':
    main()
