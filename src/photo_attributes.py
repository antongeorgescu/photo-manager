import time
from datetime import datetime
import os
from PIL import Image
from PIL.ExifTags import TAGS

# Replace this with your actual folder path
folder_path = os.getenv("PHOTO_SOURCE_PATH")

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
    for filename in os.listdir(folder_path):
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
                    exceptions += 1
            else:
                print(f"No EXIF data found for {filename}")
                exceptions += 1
    print(f"Process completed with {exceptions} files with exceptions.")

process_folder(folder_path)