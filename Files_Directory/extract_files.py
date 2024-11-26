# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:35:24 2024

@author: gangylee

Description: Extract all the zip file within a dir into a destination folder and subsequent folder named according to zip file.

"""

from pathlib import Path 
import zipfile

root_dir = Path('files')
destination_path = Path('destination')

for path in root_dir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = destination_path / Path(path.stem)
    zf.extractall(path=final_path)