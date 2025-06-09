import os
import re
import subprocess

def get_imported_packages(project_dir):
    imported_packages = set()
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    imports = re.findall(r'^\\s*import\\s+(\\w+)', content, re.MULTILINE)
                    from_imports = re.findall(r'^\\s*from\\s+(\\w+)', content, re.MULTILINE)
                    imported_packages.update(imports)
                    imported_packages.update(from_imports)
    return imported_packages

def get_installed_packages(pip_path):
    result = subprocess.run([pip_path, 'list'], capture_output=True, text=True)
    installed_packages = set()
    for line in result.stdout.splitlines()[2:]:  # Skip header lines
        package = line.split()[0]
        installed_packages.add(package)
    return installed_packages

def uninstall_packages(packages, pip_path):
    for package in packages:
        subprocess.run([pip_path, 'uninstall', '-y', package])

# Set your paths here
project_dir = r'C:\\Users\\alvianda\\Documents\\Projects\\Pipelines\\photo-manager\\src'
pip_path = r'C:\\Users\\alvianda\\Documents\\Projects\\Pipelines\\photo-manager\\.venv\\Scripts\\pip.exe'

# Run the cleanup
imported = get_imported_packages(project_dir)
installed = get_installed_packages(pip_path)
unused = installed - imported

print(f"Unused packages: {unused}")
uninstall_packages(unused, pip_path)
