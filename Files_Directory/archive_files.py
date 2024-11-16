# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:46:56 2024

@author: gangylee

Description: Archive all the file within a dir in a folder.

"""

from pathlib import Path 
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink()