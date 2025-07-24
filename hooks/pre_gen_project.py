import os
import shutil
import sys

def copy_template(source_folder, destination_folder):
    """
    Copy contents from the selected template (cli or fastapi)
    into the final project folder.
    """
    if not os.path.exists(source_folder):
        print(f"[ERROR] Source folder does not exist: {source_folder}")
        sys.exit(1)

    for item in os.listdir(source_folder):
        s = os.path.join(source_folder, item)
        d = os.path.join(destination_folder, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def remove_placeholder(project_slug):
    """
    Remove the placeholder file used to satisfy Cookiecutter’s initial structure requirement.
    """
    placeholder_file = os.path.join(os.getcwd(), project_slug, '.placeholder')
    if os.path.exists(placeholder_file):
        os.remove(placeholder_file)

# Read values from cookiecutter
project_type = "{{ cookiecutter.project_type }}"
project_slug = "{{ cookiecutter.project_slug }}"

# Define paths
template_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_dir = os.path.join(template_base_dir, project_type, project_slug)
dest_dir = os.path.join(template_base_dir, project_slug)

# Step 1: Copy template files
copy_template(src_dir, dest_dir)

# Step 2: Remove the dummy placeholder file
remove_placeholder(project_slug)
