# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:26:21 2024

@author: gangylee

Description: Rename all the file within a dir according to parent-dirname.

"""

from pathlib import Path

root_dir = Path('files')
# --- include dir inside dir as path
file_paths = root_dir.glob("**/*")

print(f"Current directory : {Path.cwd()}\n")

for path in file_paths:
    if path.is_file():
        print(f"Before : {path}")
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_filename)
        print(f"After : {new_filepath}\n")
        
        path.rename(new_filepath)