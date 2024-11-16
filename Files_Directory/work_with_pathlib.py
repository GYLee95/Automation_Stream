# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:04:24 2024

@author: gangylee
"""

from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

if not p1.exists():
  with open(p1, 'w') as file:
    file.write('Content 3')
    print("Create new txt file")


print(f"Name : {p1.name}")
print(f"Stem : {p1.stem}")
print(f"Suffix : {p1.suffix}")

# --- path to dir
p2 = Path('files')
# --- get list of files inside the dir
print(list(p2.iterdir()))