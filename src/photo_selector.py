from datetime import datetime
from pathlib import Path
import shutil
import os
from pathlib import Path
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Nano version

# Source directory with photos
source_dir = Path(os.getenv("MEDIA_SOURCE_PATH"))

def create_target_directories():
    """
    Create target directories for organizing photos.
    """
    selections = ["People", "Others"]
    for selection in selections:
        target_dir = source_dir / selection
        # Create directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)

def process_folder(folder_path):
    total_people_pics = 0
    total_other_pics = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mov', '.mp4')):
            print(f"Skipping video file: {filename}")
            continue
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)

            results = model(image_path, show=True, save=True, save_txt=True)
            includes_people = False
            for result in results:
                if result.boxes:
                    for box in result.boxes:
                        if box.cls[0] == 0:  # Class ID for 'person'
                            includes_people = True
                            break
            if includes_people:
                # If the image includes people, move it to the 'People' folder
                shutil.move(image_path, source_dir / "People" / filename)
                total_people_pics += 1
                print(f"Moved {filename} to People folder.")    
            else:
                # If the image does not include people, move it to the 'Others' folder
                shutil.move(image_path, source_dir / "Others" / filename)
                total_other_pics += 1
                print(f"Moved {filename} to Others folder.")

    return total_people_pics, total_other_pics

if __name__ == "__main__":
    try:
        create_target_directories()
        print("Target directories created successfully!")
        
        total_people_pics, total_other_pics = process_folder(source_dir)
        files_processed = total_people_pics + total_other_pics
        print(f"Photo selection completed successfully: {files_processed} files processed, with {total_people_pics} people pics identified.")
    except Exception as e:
        print(f"ERROR:An error occurred: {str(e)}")