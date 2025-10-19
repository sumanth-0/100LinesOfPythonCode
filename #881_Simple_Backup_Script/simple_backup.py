import shutil
import datetime 
import os

def backup_files(source_dir, backup_dir):
'''
    this adds documentation to the file to improve readablibity of backup 
'''
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination_dir = os.path.join(backup_dir, f"backup_{timestamp}")

''' 
    try and catch exceptions for error handling
        '''
    try:
        shutil.copytree(source_dir, destination_dir)
        print(f"Backup successful. -> to -> {destination_dir}")
    except Exception as e:
        print(f"Backup failed: {e}")

source_directory = "/path/to/source"
backup_directory = "/path/to/backup"


backup_files(source_directory, backup_directory)

