import os
import shutil
import sys

def copy_template(template_name, target_name):
    src = os.path.join(os.path.dirname(__file__), '..', template_name)
    dest = os.path.join(os.getcwd(), target_name)

    if not os.path.exists(src):
        print(f"Error: Template '{template_name}' not found.")
        sys.exit(1)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

project_type = '{{ cookiecutter.project_type }}'
project_slug = '{{ cookiecutter.project_slug }}'

copy_template(project_type, project_slug)
