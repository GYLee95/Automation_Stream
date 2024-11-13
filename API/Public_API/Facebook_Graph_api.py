# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:06:31 2024

@author: gangylee

ref link : https://developers.facebook.com/

token :
EAAJIitQMcZBABAEZBMY7shwy9brRQzgC3WmRdST9b4oXy0t24
LSZC0KEaVCvVQ4PmQwtrx0tUsv64dg5gT4FEN5UCfZAaJwSDLr
qdXAjyZAJKCNHsomPBBKgtVQDdWnr301GumkMi266I3xIzPKJT
cbr2ybMiwGVE9pMyZAWVyuYaKgKFegmwKtvd0geqijSCYlfgSZ
CrP17BnHUek8BslsJqqQ5ygMQLHLMK4HDScV1dn1jdCUBxq2ZBmkfLZB8u6HsZD

"""

import requests
import json

token = "token"

url = f"https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token={token}"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
  file.write(image_bytes)