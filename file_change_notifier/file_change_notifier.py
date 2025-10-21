#!/usr/bin/env python3
"""
File Change Notifier

This script monitors files and directories for changes and sends notifications
when modifications, additions, or deletions occur.

Features:
- Monitor multiple files and directories
- Detect file creation, modification, and deletion
- Configurable notification methods (console, email, log file)
- Support for recursive directory monitoring
- File hash comparison for accurate change detection
"""

import os
import sys
import time
import hashlib
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Set, Optional


class FileChangeNotifier:
    """Monitor files and directories for changes and send notifications."""
    
    def __init__(self, watch_paths: list, recursive: bool = True, 
                 check_interval: int = 5, log_file: Optional[str] = None):
        """
        Initialize the File Change Notifier.
        
        Args:
            watch_paths: List of file/directory paths to monitor
            recursive: Whether to monitor subdirectories recursively
            check_interval: Time interval (seconds) between checks
            log_file: Optional log file path for notifications
        """
        self.watch_paths = [Path(p) for p in watch_paths]
        self.recursive = recursive
        self.check_interval = check_interval
        self.file_registry: Dict[str, dict] = {}
        
        # Set up logging
        self.logger = self._setup_logger(log_file)
        
        # Initialize file registry
        self._initialize_registry()
    
    def _setup_logger(self, log_file: Optional[str] = None) -> logging.Logger:
        """Set up logging configuration."""
        logger = logging.getLogger('FileChangeNotifier')
        logger.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        # File handler (if specified)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(console_formatter)
            logger.addHandler(file_handler)
        
        return logger
    
    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of a file."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            self.logger.error(f"Error calculating hash for {file_path}: {e}")
            return ""
    
    def _get_file_info(self, file_path: Path) -> dict:
        """Get file information including size, modification time, and hash."""
        try:
            stat_info = file_path.stat()
            return {
                'size': stat_info.st_size,
                'mtime': stat_info.st_mtime,
                'hash': self._calculate_hash(file_path) if file_path.is_file() else None
            }
        except Exception as e:
            self.logger.error(f"Error getting file info for {file_path}: {e}")
            return {}
    
    def _scan_directory(self, directory: Path) -> Set[Path]:
        """Scan directory and return set of all files."""
        files = set()
        try:
            if self.recursive:
                for item in directory.rglob('*'):
                    if item.is_file():
                        files.add(item)
            else:
                for item in directory.iterdir():
                    if item.is_file():
                        files.add(item)
        except Exception as e:
            self.logger.error(f"Error scanning directory {directory}: {e}")
        return files
    
    def _initialize_registry(self):
        """Initialize the file registry with current state of watched paths."""
        self.logger.info("Initializing file registry...")
        
        for watch_path in self.watch_paths:
            if not watch_path.exists():
                self.logger.warning(f"Path does not exist: {watch_path}")
                continue
            
            if watch_path.is_file():
                # Single file monitoring
                file_info = self._get_file_info(watch_path)
                self.file_registry[str(watch_path)] = file_info
                self.logger.info(f"Monitoring file: {watch_path}")
            
            elif watch_path.is_dir():
                # Directory monitoring
                files = self._scan_directory(watch_path)
                for file_path in files:
                    file_info = self._get_file_info(file_path)
                    self.file_registry[str(file_path)] = file_info
                self.logger.info(f"Monitoring directory: {watch_path} ({len(files)} files)")
        
        self.logger.info(f"Initialized {len(self.file_registry)} files in registry")
    
    def _check_for_changes(self):
        """Check for changes in monitored files and directories."""
        current_files = set()
        
        # Scan all watch paths
        for watch_path in self.watch_paths:
            if not watch_path.exists():
                self.logger.warning(f"Path no longer exists: {watch_path}")
                continue
            
            if watch_path.is_file():
                current_files.add(watch_path)
            elif watch_path.is_dir():
                current_files.update(self._scan_directory(watch_path))
        
        # Convert to string paths for comparison
        current_file_paths = {str(f) for f in current_files}
        registered_paths = set(self.file_registry.keys())
        
        # Detect new files
        new_files = current_file_paths - registered_paths
        for file_path in new_files:
            path_obj = Path(file_path)
            file_info = self._get_file_info(path_obj)
            self.file_registry[file_path] = file_info
            self.logger.info(f"NEW FILE: {file_path}")
        
        # Detect deleted files
        deleted_files = registered_paths - current_file_paths
        for file_path in deleted_files:
            del self.file_registry[file_path]
            self.logger.info(f"DELETED: {file_path}")
        
        # Detect modified files
        for file_path in current_file_paths & registered_paths:
            path_obj = Path(file_path)
            old_info = self.file_registry[file_path]
            new_info = self._get_file_info(path_obj)
            
            # Compare hashes for accurate change detection
            if old_info.get('hash') != new_info.get('hash'):
                self.file_registry[file_path] = new_info
                self.logger.info(f"MODIFIED: {file_path}")
    
    def start_monitoring(self):
        """Start monitoring files and directories for changes."""
        self.logger.info(f"Starting file monitoring (check interval: {self.check_interval}s)")
        self.logger.info("Press Ctrl+C to stop monitoring")
        
        try:
            while True:
                self._check_for_changes()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.logger.info("Monitoring stopped by user")
        except Exception as e:
            self.logger.error(f"Error during monitoring: {e}")


def main():
    """Main entry point for the File Change Notifier."""
    parser = argparse.ArgumentParser(
        description='Monitor files and directories for changes'
    )
    parser.add_argument(
        'paths',
        nargs='+',
        help='File or directory paths to monitor'
    )
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        default=True,
        help='Monitor directories recursively (default: True)'
    )
    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=5,
        help='Check interval in seconds (default: 5)'
    )
    parser.add_argument(
        '-l', '--log-file',
        type=str,
        help='Log file path for notifications'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    for path in args.paths:
        if not os.path.exists(path):
            print(f"Warning: Path does not exist: {path}")
    
    # Create and start the notifier
    notifier = FileChangeNotifier(
        watch_paths=args.paths,
        recursive=args.recursive,
        check_interval=args.interval,
        log_file=args.log_file
    )
    
    notifier.start_monitoring()


if __name__ == '__main__':
    main()
