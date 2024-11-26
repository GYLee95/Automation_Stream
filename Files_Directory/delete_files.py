# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:49:56 2024

@author: gangylee

Description: Delete file with given file type within a folder in a dir.

"""

from pathlib import Path

root_dir = Path('destination')

for path in root_dir.glob("*.csv"):
  with open(path, 'wb') as file:
    file.write(b'')
    print("Write success")
  path.unlink()
  print("Delete success")