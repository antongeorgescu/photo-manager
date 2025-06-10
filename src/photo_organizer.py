import os
from datetime import datetime
from pathlib import Path
import shutil

# Source directory with photos
source_dir = Path(os.getenv("MEDIA_SOURCE_PATH"))

# Target directory for organized photos
target_dir = Path(os.getenv("MEDIA_DESTINATION_PATH"))

def organize_photos(source_path,target_path):
    # Get all files recursively, excluding directories
    files = [f for f in source_path.rglob('*') if f.is_file()]
    
    for file in files:
        # Get last modified time
        last_modified = datetime.fromtimestamp(file.stat().st_mtime)
        year = str(last_modified.year)
        month = last_modified.strftime("%B")  # Full month name
        
        # Print file info
        print(f"File: {file.name}")
        print(f"Year: {year}")
        print(f"Month: {month}")
        
        # Create target directory path
        target_dir = target_path / year / month
        
        # Create directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Move file to new location
        shutil.move(str(file), str(target_dir / file.name))

if __name__ == "__main__":
    try:
        organize_photos(source_dir, target_dir)
        print("Photo organization completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")