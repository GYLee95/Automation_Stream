# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:01:40 2024

@author: gangylee

Description: Create new empty text file within the dir.

"""

from pathlib import Path

root_dir = Path('files')

for i in range(10, 16):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    print(root_dir)
    print(filepath)
    filepath.touch()