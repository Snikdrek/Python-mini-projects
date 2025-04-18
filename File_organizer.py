import os
import shutil
import sys

download_folder=input("Enter the directory containing the files: ")
os.chdir(download_folder)
files = os.listdir(os.curdir)
extensions = set()
for file in files:
    if os.path.isfile(file):
        extensions.add(file.split(".")[-1])
for ext in extensions:
    if not os.path.isfile(ext):  # Ensure no conflict with existing files
        os.makedirs(ext, exist_ok=True)
for file in files:
    if os.path.isfile(file):
        ext = file.split(".")[-1]
        target_dir = os.path.join(download_folder, ext)
        if not os.path.isfile(target_dir):  # Ensure no conflict with existing files
            os.makedirs(target_dir, exist_ok=True)  # Ensure the directory exists
        shutil.move(file, os.path.join(target_dir, file))
print("Files have been organized by extension.")
