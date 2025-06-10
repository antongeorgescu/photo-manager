from pathlib import Path
import subprocess
import json
import sys
import datetime

SAMPLE_MEDIA_FILE = "sample_media\\IMG_4074.mov"

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

if __name__ == "__main__":
    file_dir = Path.cwd() # Get the current working directory
    if not file_dir.exists():
        print(f"Directory {file_dir} does not exist.")
        sys.exit(1)
    file_path = file_dir / SAMPLE_MEDIA_FILE
    if not file_path.exists():
        print(f"File {file_path} does not exist.")
        sys.exit(1)
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
    else:
        print("Creation date not found in metadata.")
