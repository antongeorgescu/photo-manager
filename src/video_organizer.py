from pathlib import Path
import subprocess
import json
import sys
import os
from datetime import datetime
import shutil

# Source directory with photos
source_dir = Path(os.getenv("MEDIA_SOURCE_PATH"))

# Target directory for organized photos
target_dir = Path(os.getenv("MEDIA_DESTINATION_PATH"))

def get_creation_date(file_path):
    try:
        # Run ffprobe to get metadata
        try:
            result = subprocess.run(
                ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_entries',
                 'format_tags=creation_time', file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                check=True
            )
        except FileNotFoundError:
            print("Error: ffprobe is not installed or not found in PATH.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Error running ffprobe: {e.stderr}")
            return None

        try:
            metadata = json.loads(result.stdout)
        except json.JSONDecodeError:
            print("Error: ffprobe did not return valid JSON.")
            return None

        creation_time = metadata.get('format', {}).get('tags', {}).get('creation_time', None)
        return creation_time
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_folder(folder_path):
    exceptions = 0
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.mov', '.mp4')):
            file_path = os.path.join(folder_path, file)

            creation_date = get_creation_date(str(file_path))
            if creation_date:
                print(f"Original Creation Date: {creation_date}")

                # Remove timezone info if present and parse ISO format
                if creation_date.endswith('Z'):
                    creation_date = creation_date[:-1]
                try:
                    last_modified = datetime.datetime.fromisoformat(creation_date)
                except AttributeError:
                    # For Python < 3.7, fallback to strptime
                    last_modified = datetime.datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
                year = str(last_modified.year)
                month = last_modified.strftime("%B")  # Full month name
                
                # Print file info
                print(f"File: {file_path.name}")
                print(f"Year: {year}")
                print(f"Month: {month}")

                # Create target directory path
                target_dir = target_dir / year / month
                
                # Create directory if it doesn't exist
                target_dir.mkdir(parents=True, exist_ok=True)
                
                # Move file to new location
                shutil.move(str(file), str(target_dir / file.name))

            else:
                print("Creation date not found in metadata.")
                exceptions += 1
            
    print(f"Process completed with {exceptions} files with exceptions.")

process_folder(source_dir)