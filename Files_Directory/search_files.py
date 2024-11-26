# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:44:56 2024

@author: gangylee

Description: Search file with given filename across folders in a dir.

"""

from pathlib import Path

root_dir = Path('.')
search_term = '14'

for path in root_dir.rglob("*"):
  if path.is_file():
    if search_term in path.stem:
      print(path.absolute())