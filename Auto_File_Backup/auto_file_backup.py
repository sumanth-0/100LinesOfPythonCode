#!/usr/bin/env python3
"""
Auto File Backup Script
Copies important files from source directory to a backup folder with timestamps.
Supports scheduling for daily backups.
"""

import os
import shutil
import datetime
import json
import logging
import argparse
from pathlib import Path
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup.log'),
        logging.StreamHandler()
    ]
)

class FileBackup:
    def __init__(self, source_dir, backup_dir, config_file='backup_config.json'):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from JSON file or create default."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            default_config = {
                'file_extensions': ['.txt', '.pdf', '.doc', '.docx', '.xlsx'],
                'exclude_folders': ['temp', 'cache'],
                'max_backups': 7
            }
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config):
        """Save configuration to JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    
    def create_backup_folder(self):
        """Create timestamped backup folder."""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'backup_{timestamp}'
        backup_path.mkdir(parents=True, exist_ok=True)
        return backup_path
    
    def should_backup_file(self, file_path):
        """Check if file should be backed up based on configuration."""
        file_ext = file_path.suffix
        if file_ext not in self.config['file_extensions']:
            return False
        
        for exclude in self.config['exclude_folders']:
            if exclude in file_path.parts:
                return False
        return True
    
    def backup_files(self):
        """Perform the backup operation."""
        if not self.source_dir.exists():
            logging.error(f"Source directory {self.source_dir} does not exist.")
            return False
        
        backup_path = self.create_backup_folder()
        files_backed_up = 0
        
        try:
            for root, dirs, files in os.walk(self.source_dir):
                for file in files:
                    file_path = Path(root) / file
                    
                    if self.should_backup_file(file_path):
                        relative_path = file_path.relative_to(self.source_dir)
                        dest_path = backup_path / relative_path
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        shutil.copy2(file_path, dest_path)
                        files_backed_up += 1
                        logging.info(f"Backed up: {relative_path}")
            
            logging.info(f"Backup completed. {files_backed_up} files backed up to {backup_path}")
            self.cleanup_old_backups()
            return True
            
        except Exception as e:
            logging.error(f"Backup failed: {str(e)}")
            return False
    
    def cleanup_old_backups(self):
        """Remove old backups exceeding max_backups limit."""
        if not self.backup_dir.exists():
            return
        
        backups = sorted([d for d in self.backup_dir.iterdir() if d.is_dir()],
                        key=lambda x: x.stat().st_mtime, reverse=True)
        
        if len(backups) > self.config['max_backups']:
            for old_backup in backups[self.config['max_backups']:]:
                shutil.rmtree(old_backup)
                logging.info(f"Removed old backup: {old_backup}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Auto File Backup Script')
    parser.add_argument('source', help='Source directory path')
    parser.add_argument('backup', help='Backup directory path')
    parser.add_argument('--config', default='backup_config.json', help='Config file path')
    
    args = parser.parse_args()
    
    backup_tool = FileBackup(args.source, args.backup, args.config)
    backup_tool.backup_files()
