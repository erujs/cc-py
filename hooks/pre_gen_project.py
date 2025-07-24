import os
import shutil
import sys

def copy_template(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"ERROR: Source folder {source_folder} does not exist.")
        sys.exit(1)

    for item in os.listdir(source_folder):
        s = os.path.join(source_folder, item)
        d = os.path.join(destination_folder, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

# Values from cookiecutter.json
project_type = "{{ cookiecutter.project_type }}"
project_slug = "{{ cookiecutter.project_slug }}"

src = os.path.join(os.path.dirname(__file__), "..", project_type, project_slug)
dest = os.path.join(os.getcwd(), project_slug)

copy_template(src, dest)
