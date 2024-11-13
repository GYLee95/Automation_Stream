# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:34:45 2024

@author: gangylee

ref link : https://languagetool.org/http-api/#/default

"""

import requests
import json

url = "https://api.languagetool.org/v2/check"

data = {
        'text' : "Tis is a nixe day!",
        'language' : "auto"
}

response = requests.post(url, data=data)
result = response.json()
# result = json.loads(response.text)

print(json.dumps(result, indent=4))