
Simple Backup Script
====================

This is a simple Python script to create backups of a specified source directory by copying it 
to a backup directory with a timestamp suffix.

Description
-----------
The script uses the standard Python libraries: `shutil`, `os`, and `datetime`.
It copies the entire source directory to a new directory inside the backup folder, with the 
name formatted as `backup_YYYY-MM-DD_HH-MM-SS`.

Usage
-----
1. Set the `source_directory` variable to the path of the directory you want to back up.
2. Set the `backup_directory` variable to the path where you want to store backups.
3. Run the script.

