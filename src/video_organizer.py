from pathlib import Path
import subprocess
import json
import sys
import os
import datetime
import shutil
import init_ffmpeg

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
    total_files = 0
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
                    creation_date_upd = datetime.datetime.fromisoformat(creation_date)
                except AttributeError:
                    # For Python < 3.7, fallback to strptime
                    creation_date_upd = datetime.datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
                year = str(creation_date_upd.year)
                month = creation_date_upd.strftime("%B")  # Full month name
                
                # Print file info
                print(f"File: {file}")
                print(f"Year: {year}")
                print(f"Month: {month}")

                # Create target directory path
                target_dir_new = f"{target_dir}/{year}/{month}"
                
                # Create directory if it doesn't exist
                os.makedirs(target_dir_new, exist_ok=True)
                
                # Move file to new location; only move if destination doesn't exist
                destination_file = Path(f"{target_dir_new}/{file}")

                if not destination_file.exists():
                    shutil.move(str(file_path), f"{target_dir_new}/{file}")

                total_files += 1

            else:
                print("Creation date not found in metadata.")
                exceptions += 1
    if exceptions > 0:
        print(f"Process completed with {exceptions} files with exceptions.")
    return total_files
            
if __name__ == "__main__":
    try:
        init_ffmpeg.add_ffmpeg_to_path()
        
        files_processed = process_folder(source_dir)
        print(f"Video files processing completed successfully: {files_processed} files organized.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
