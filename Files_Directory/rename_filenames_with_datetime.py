# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:44:48 2024

@author: gangylee

Description: Rename all the file within a dir according with datetime.

"""

from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
      print(f"Before : {path}")
      created_date = datetime.fromtimestamp(path.stat().st_ctime)
      created_date_str = created_date.strftime("%Y-%m-%d_%H%M%S")
      
      new_filename = created_date_str + '_' + path.name
      new_filepath = path.with_name(new_filename)
      print(f"After : {new_filepath}\n")
      path.rename(new_filepath)