from datetime import datetime
from pathlib import Path
import shutil
import time
import os
from PIL import Image
from PIL.ExifTags import TAGS



# Source directory with photos
source_dir = Path(os.getenv("MEDIA_SOURCE_PATH"))

# Target directory for organized photos
target_dir = Path(os.getenv("MEDIA_DESTINATION_PATH"))

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        exif = {TAGS.get(tag): value for tag, value in exif_data.items()}
        return exif
    return None

def get_original_date(exif_data):
    if 'DateTimeOriginal' in exif_data:
        return exif_data['DateTimeOriginal']
    return None

def update_file_timestamp(file_path, date_str):
    date_time_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    timestamp = time.mktime(date_time_obj.timetuple())
    os.utime(file_path, (timestamp, timestamp))

def process_folder(folder_path):
    exceptions = 0
    unprocessed_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mov', '.mp4')):
            print(f"Skipping video file: {filename}")
            unprocessed_files.append(filename)
            continue
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            exif_data = get_exif_data(file_path)
            if exif_data:
                original_date = get_original_date(exif_data)
                if original_date:
                    update_file_timestamp(file_path, original_date)
                    # print(f"Updated timestamps for {filename} to {original_date}")
                else:
                    print(f"No DateTimeOriginal found for {filename}")
                    unprocessed_files.append(filename)
                    exceptions += 1
            else:
                print(f"No EXIF data found for {filename}")
                exceptions += 1
    if exceptions > 0:
        print(f"Process completed with {exceptions} files with exceptions.")
    return unprocessed_files

def organize_photos(source_path,target_path, unprocessed_files):
    total_files = 0
    # Get all files recursively, excluding directories
    files = [f for f in source_path.rglob('*') if f.is_file()]
    
    for file in files:
        if file.name in unprocessed_files:
            print(f"Skipping unprocessed file: {file.name}")
            continue

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
        
        # Move file to new location; only move if destination doesn't exist
        if not os.path.exists(target_dir / file.name):
            shutil.move(str(file), str(target_dir / file.name))
        
        total_files += 1
    return total_files

if __name__ == "__main__":
    try:

        unprocessed_files = process_folder(source_dir)
        print("Photo attributes completed successfully!")
        
        files_processed = organize_photos(source_dir, target_dir, unprocessed_files)
        print(f"Photo organization completed successfully: {files_processed} files processed.")
    except Exception as e:
        print(f"ERROR:An error occurred: {str(e)}")