from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.main:main",
        ],
    },
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    python_requires=">={{cookiecutter.python_version}}",
)
