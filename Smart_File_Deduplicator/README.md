# Smart File Deduplicator 🗂️

An intelligent utility to find and remove duplicate files based on content (not just filename), helping you reclaim wasted storage space.

## Features ✨

- **Content-Based Detection**: Uses MD5 hashing to identify true duplicates
- **Smart Scanning**: Recursively scans directories and subdirectories
- **Storage Analysis**: Shows wasted space per duplicate group
- **Safe Deletion**: Confirms before deleting each file
- **Detailed Reporting**: Clear visualization of duplicate files
- **Size Formatting**: Human-readable file sizes (KB, MB, GB)

## Usage 🚀

### Basic Scan

```bash
python file_deduplicator.py /path/to/directory
```

### Example

```bash
# Scan Downloads folder
python file_deduplicator.py ~/Downloads

# Scan current directory
python file_deduplicator.py .

# Scan specific folder
python file_deduplicator.py /Users/username/Documents
```

## Output Example 📊

```
🔍 Scanning directory: /Users/john/Downloads

📊 Scanned 150 files
🔄 Found 5 groups of duplicates

📁 Group 1 (3 copies) - 2.50 MB each:
  ✓ [1] /Users/john/Downloads/photo.jpg
  🗑️  [2] /Users/john/Downloads/photo-copy.jpg
  🗑️  [3] /Users/john/Downloads/photo (1).jpg
  💾 Wasted space: 5.00 MB

📁 Group 2 (2 copies) - 1.20 MB each:
  ✓ [1] /Users/john/Downloads/document.pdf
  🗑️  [2] /Users/john/Downloads/document-backup.pdf
  💾 Wasted space: 1.20 MB

📈 Summary:
  Total duplicate files: 4
  Recoverable space: 6.20 MB

Delete duplicates? (y/n):
```

## How It Works 🔧

1. **Scanning**: Recursively walks through all files in directory
2. **Hashing**: Calculates MD5 hash for each file's content
3. **Grouping**: Groups files with identical hashes
4. **Analysis**: Calculates wasted space and displays results
5. **Cleanup**: Optionally deletes duplicates with confirmation

## Why MD5 Hash? 🔐

- **Content-Based**: Compares actual file content, not just names
- **Fast**: Efficient even for large files using chunk processing
- **Reliable**: Same content = same hash, guaranteed
- **Rename-Proof**: Finds duplicates even if renamed

## Safety Features 🛡️

- **Keep Original**: Always keeps first occurrence
- **Confirmation Required**: Asks before each deletion
- **Error Handling**: Gracefully handles permission errors
- **Read-Only**: Scan mode doesn't modify anything

## Use Cases 💡

1. **Photo Libraries**: Find duplicate photos with different names
2. **Download Cleanup**: Remove duplicate downloads
3. **Backup Organization**: Identify redundant backup files
4. **Disk Cleanup**: Reclaim storage space
5. **File Management**: Organize large document collections

## Advanced Usage 🎯

### Find Only (No Delete)
```bash
# Run script and choose 'n' when asked to delete
python file_deduplicator.py ~/Documents
```

### Scan Specific File Types
```bash
# Combine with find command (Unix/Linux)
find ~/Photos -name "*.jpg" -o -name "*.png" | python file_deduplicator.py ~/Photos
```

## Performance ⚡

- **Chunk Processing**: Reads files in 8KB chunks for memory efficiency
- **Skip Empty Files**: Automatically skips 0-byte files
- **Error Resilience**: Continues scanning even if some files fail

## Output Information 📋

### Duplicate Groups
- Shows all files with identical content
- First file marked with ✓ (will be kept)
- Duplicates marked with 🗑️ (candidates for deletion)
- File size per copy
- Total wasted space per group

### Summary Statistics
- Total files scanned
- Number of duplicate groups found
- Total duplicate files
- Total recoverable space

## Requirements 📦

- Python 3.6+
- Standard library only:
  - `hashlib` (MD5 calculation)
  - `pathlib` (path handling)
  - `os` (file operations)

## Important Notes ⚠️

- **Original Kept**: First occurrence is always preserved
- **Confirmation**: Each deletion requires manual confirmation
- **Permissions**: Requires read access to scan, write to delete
- **Symbolic Links**: Skips symbolic links (processes real files only)
- **Hidden Files**: Includes hidden files in scan

## Tips 💭

1. **Test First**: Run on small directory first to understand output
2. **Backup**: Consider backing up before bulk deletions
3. **Review Groups**: Check each group before confirming deletion
4. **Large Directories**: May take time for directories with many files
5. **External Drives**: Works on external drives and network shares

## Example Scenarios 🎬

### Clean Download Folder
```bash
python file_deduplicator.py ~/Downloads
# Review duplicates, delete unwanted copies
```

### Photo Library Cleanup
```bash
python file_deduplicator.py ~/Pictures
# Find duplicate photos from different sources
```

### Project Folder Organization
```bash
python file_deduplicator.py ~/Projects
# Remove duplicate source files and resources
```

## Limitations ⚡

- Under 100 lines per file (repository requirement)
- MD5 only (no SHA256 option in this version)
- Interactive deletion (no batch mode)
- No file preview option

## Future Enhancements 🚀

- Batch deletion mode
- File type filtering
- Preview before delete
- Move to trash instead of permanent delete
- Hardlink option for space saving

## Contributing 🤝

Part of the 100LinesOfPythonCode project. Contributions welcome!

## License 📜

Open source - free to use and modify.

---

**Author**: Contributed for Hacktoberfest 2025
**Project**: 100LinesOfPythonCode
