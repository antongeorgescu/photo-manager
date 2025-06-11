import os
import subprocess
from pathlib import Path

def add_ffmpeg_to_path():
    """
    Adds the ffmpeg binary path to the system PATH environment variable.
    This allows the use of ffmpeg commands in the terminal or scripts.
    """
    
    # Path to the folder containing ffprobe.exe
    current_folder = Path.cwd()
    # Construct the path to the ffmpeg binary
    if not (current_folder / "ffmpeg-7.1.1-essentials_build" / "bin").exists():
        print("ERROR: ffmpeg directory not found in the current folder.", flush=True)
        return
    ffmpeg_bin_path = f"{current_folder}\\ffmpeg-7.1.1-essentials_build\\bin"
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
        print("ffprobe output:\n", result.stdout, flush=True)
    except FileNotFoundError:
        print("ERROR:ffprobe not found. Check the path.",flush=True)
