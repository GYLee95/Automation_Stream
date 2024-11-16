# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:38:27 2024

@author: gangylee

Description: Rename all the file within a dir according to Sub-Sub-Folder name.

"""

from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    path_parts = path.parts
    subfolders = path.parts[1:-1]

    new_filename = "-".join(subfolders) + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)