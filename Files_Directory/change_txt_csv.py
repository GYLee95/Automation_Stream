# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:52:48 2024

@author: gangylee

Description: Change the file extension of all the file within a dir from txt to csv and vice versa.

"""

from pathlib import Path

from_file_extension = "csv"
to_file_extension = "txt"

root_dir = Path('files')

for path in root_dir.rglob(f"*.{from_file_extension}"):
    if path.is_file():
        print(f"Before : {path}")
        new_filepath = path.with_suffix(f".{to_file_extension}")
        print(f"After : {new_filepath}\n")
        path.rename(new_filepath)
