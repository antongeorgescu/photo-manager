import time
from datetime import datetime
import os
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path
import sys

SAMPLE_MEDIA_FILE = "sample_media\\IMG_4302.jpeg"

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


if __name__ == "__main__":
    file_dir = Path.cwd() # Get the current working directory
    if not file_dir.exists():
        print(f"Directory {file_dir} does not exist.")
        sys.exit(1)
    file_path = file_dir / SAMPLE_MEDIA_FILE
    if not file_path.exists():
        print(f"File {file_path} does not exist.")
        sys.exit(1)
    exif_data = get_exif_data(file_path)
    if exif_data:
        original_date = get_original_date(exif_data)
        if original_date:
            update_file_timestamp(file_path, original_date)
            print(f"Updated timestamps for {SAMPLE_MEDIA_FILE} to {original_date}")
        else:
            print(f"No DateTimeOriginal found for {SAMPLE_MEDIA_FILE}")
    else:
        print(f"No EXIF data found for {SAMPLE_MEDIA_FILE}")

    print("Process completed.")
    sys.exit(0)

