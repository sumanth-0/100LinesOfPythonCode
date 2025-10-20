#!/usr/bin/env python3
"""
Simple Backup Script
A Python script to backup directories and files with compression and logging.

Author: GitHub User
Date: October 2025
Issue: #881 - Simple Backup Script
"""

import os
import shutil
import zipfile
import datetime
import argparse
import logging
import json
from pathlib import Path


class BackupManager:
    """Manages backup operations for files and directories."""
    
    def __init__(self, config_file=None):
        """Initialize the backup manager with optional config file."""
        self.config = self._load_config(config_file) if config_file else {}
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging configuration."""
        log_dir = self.config.get('log_dir', 'backup_logs')
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(
            log_dir,
            f'backup_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        )
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def _load_config(self, config_file):
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def create_backup_name(self, source_path, backup_dir):
        """Generate a unique backup filename."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        source_name = os.path.basename(os.path.normpath(source_path))
        backup_name = f"{source_name}_backup_{timestamp}.zip"
        return os.path.join(backup_dir, backup_name)
    
    def backup_directory(self, source_dir, backup_dir):
        """Backup an entire directory to a zip file."""
        if not os.path.exists(source_dir):
            self.logger.error(f"Source directory does not exist: {source_dir}")
            return False
        
        os.makedirs(backup_dir, exist_ok=True)
        backup_path = self.create_backup_name(source_dir, backup_dir)
        
        try:
            self.logger.info(f"Starting backup of {source_dir}...")
            
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zipf.write(file_path, arcname)
                        self.logger.debug(f"Added {file_path} to backup")
            
            backup_size = os.path.getsize(backup_path) / (1024 * 1024)  # Size in MB
            self.logger.info(f"Backup completed successfully: {backup_path}")
            self.logger.info(f"Backup size: {backup_size:.2f} MB")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during backup: {e}")
            return False
    
    def backup_files(self, file_list, backup_dir):
        """Backup specific files to a zip archive."""
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"files_backup_{timestamp}.zip")
        
        try:
            self.logger.info(f"Starting backup of {len(file_list)} files...")
            
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in file_list:
                    if os.path.exists(file_path):
                        arcname = os.path.basename(file_path)
                        zipf.write(file_path, arcname)
                        self.logger.info(f"Backed up: {file_path}")
                    else:
                        self.logger.warning(f"File not found: {file_path}")
            
            self.logger.info(f"Files backup completed: {backup_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during files backup: {e}")
            return False
    
    def restore_backup(self, backup_path, restore_dir):
        """Restore files from a backup archive."""
        if not os.path.exists(backup_path):
            self.logger.error(f"Backup file does not exist: {backup_path}")
            return False
        
        os.makedirs(restore_dir, exist_ok=True)
        
        try:
            self.logger.info(f"Restoring backup from {backup_path}...")
            
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                zipf.extractall(restore_dir)
            
            self.logger.info(f"Restore completed successfully to {restore_dir}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during restore: {e}")
            return False
    
    def list_backups(self, backup_dir):
        """List all backup files in the backup directory."""
        if not os.path.exists(backup_dir):
            self.logger.error(f"Backup directory does not exist: {backup_dir}")
            return []
        
        backups = [f for f in os.listdir(backup_dir) if f.endswith('.zip')]
        return sorted(backups, reverse=True)


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description='Simple Backup Script')
    parser.add_argument('-s', '--source', help='Source directory to backup')
    parser.add_argument('-d', '--destination', default='backups',
                       help='Destination directory for backups')
    parser.add_argument('-f', '--files', nargs='+', help='Specific files to backup')
    parser.add_argument('-r', '--restore', help='Backup file to restore')
    parser.add_argument('--restore-dir', default='restored',
                       help='Directory to restore backup to')
    parser.add_argument('-l', '--list', action='store_true',
                       help='List all backups')
    parser.add_argument('-c', '--config', help='Configuration file path')
    
    args = parser.parse_args()
    
    backup_manager = BackupManager(args.config)
    
    if args.list:
        backups = backup_manager.list_backups(args.destination)
        print("\nAvailable backups:")
        for backup in backups:
            print(f"  - {backup}")
    
    elif args.restore:
        backup_manager.restore_backup(args.restore, args.restore_dir)
    
    elif args.files:
        backup_manager.backup_files(args.files, args.destination)
    
    elif args.source:
        backup_manager.backup_directory(args.source, args.destination)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
