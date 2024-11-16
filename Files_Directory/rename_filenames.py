# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:12:59 2024

@author: gangylee

Description: Rename all the file within a dir.

"""

from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.iterdir()

print(f"Current directory : {Path.cwd()}\n")

for path in file_paths:
    print(f"Before : {path}")
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(f"After : {new_filepath}\n")

    path.rename(new_filepath)