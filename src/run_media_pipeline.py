import subprocess
import sys
from pathlib import Path

def run_script(script_path: Path) -> bool:
    """Run a Python script and return True if successful."""
    try:
        print(f"\nExecuting: {script_path.name}")
        print("-" * 50)
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path.name}:")
        print(f"Exit code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False

def run_pipeline():
    """Execute pipeline of scripts in sequence."""
    # Define script paths
    scripts_dir = Path(__file__).parent
    scripts = [
        scripts_dir / "photo_organizer.py",
        scripts_dir / "video_organizer.py"
    ]
    
    # Execute scripts in sequence
    for script in scripts:
        if not script.exists():
            print(f"Error: Script not found - {script}")
            return
            
        success = run_script(script)
        if not success:
            print(f"Pipeline failed at {script.name}")
            return
    
    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()