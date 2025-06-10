import os
import subprocess
from pathlib import Path

# Path to the folder containing ffprobe.exe
current_folder = Path.cwd()
ffmpeg_bin_path = f"{current_folder}\\ffmpeg\\bin"
print(f"ffmpeg path: {current_folder}")

# Add it to the PATH environment variable
os.environ["PATH"] += os.pathsep + ffmpeg_bin_path

# Now you can call ffprobe
try:
    result = subprocess.run(
        ['ffprobe', '-version'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("ffprobe output:\n", result.stdout)
except FileNotFoundError:
    print("ffprobe not found. Check the path.")
