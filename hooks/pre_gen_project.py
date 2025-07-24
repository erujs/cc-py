import os
import shutil
import sys

def copy_template(src, dest):
    if not os.path.exists(src):
        print(f"[ERROR] Source folder does not exist: {src}")
        sys.exit(1)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def remove_placeholder(dest):
    placeholder_path = os.path.join(dest, '.placeholder')
    if os.path.exists(placeholder_path):
        os.remove(placeholder_path)

# Cookiecutter context variables
project_type = "{{ cookiecutter.project_type }}"
project_slug = "{{ cookiecutter.project_slug }}"

# Directory paths
# Current working directory is the generated project root
project_dir = os.path.abspath(os.getcwd())
template_root = os.path.abspath(os.path.join(project_dir, ".."))

src_dir = os.path.join(template_root, project_type, project_slug)
dest_dir = os.path.join(project_dir, project_slug)

# Step 1: Copy from cli/ or fastapi/ template
copy_template(src_dir, dest_dir)

# Step 2: Remove placeholder
remove_placeholder(dest_dir)
