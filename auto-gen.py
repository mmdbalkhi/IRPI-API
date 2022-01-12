# -*- coding: utf-8 -*-
"""
a script for Auto genarate README file
"""


import os.path
from json import load
from os import listdir

repo_address = "https://github/mmdbakhi/IRPI/"
project_name = "IRPI"

def generate_img_table(img_dir=None) -> str:

    if not img_dir:
        img_dir = os.path.dirname(os.path.abspath(__file__)) + '/img'


    output = """
## Photos

| Name | Location | Photographer | sender | description | view  |
|------|----------|--------------|--------|-------------|-------|
"""
    items = os.listdir(img_dir)
    items.sort()

    for item in items:
        if item[0] not in [".", "_"] and os.path.exists(img_dir + "/" + item + '/image.jpg'):
            try:
                with open(img_dir + '/' + item + '/info.json') as file:
                    json_file = load(file)

                img_path = f"{repo_address}img/{item}.jpg"

                output += f'| {json_file["name"]} | {json_file["location"]} '
                output += f'| {json_file["photographer"]} | {json_file["sender"]} '
                output += f'| {json_file["description"]} '
                output += f'| <a href= "{img_path}"> <img src="{img_path}" sizes="32x32"> </a> |'

                output += '\n'
                print(f"{item} output is writed")
            except:
                print(f"{item} not exists or have a problem in syntax")

    return output




readme = """<!-- auto generated dont edit-->

# IRPI API

> IRan Place Img API

IRPI is a RESTful API. your can download Iran beautiful Place img.

## Example

### Find Random img

```
$ curl IRPI.com.api/v1/random
```

```json
{
  "data": {
    "description": "description", 
    "location": "location", 
    "name": "example", 
    "photographer": "the photographer", 
    "sender": "sender"
  }, 
  "id": "uuid4", 
  "img name": "example", 
  "img url": "http://localhost:5000/img/example/image.jpg", 
  "status": "ok"
}

```

### Find img by name

```
$ curl IRPI.com/v1/find/example
```

```json
{
  "data": {
    "description": "description", 
    "location": "location", 
    "name": "example", 
    "photographer": "the photographer", 
    "sender": "sender"
  }, 
  "id": "uuid4", 
  "img name": "example", 
  "img url": "http://localhost:5000/img/example/image.jpg", 
  "status": "ok"
}

```
"""

readme += generate_img_table()

with open(os.path.dirname(os.path.abspath(__file__)) + '/README.md',"w") as file:

    file.write(readme)
    print("done!")