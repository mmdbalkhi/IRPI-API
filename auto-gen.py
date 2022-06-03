"""
a script for Auto genarate README file
"""
import os
from json import load as json_load
from os import listdir

repo = "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main"
project_name = "IRPI"
main_tree = os.path.dirname(os.path.abspath(__file__))


def generate_img_table(img_dir=None) -> str:

    if not img_dir:
        img_dir = main_tree + "/IRIP/img"

    output = """
## Photos

| Name | Location | Photographer | source | description | view  |
|------|----------|---------|--------|---------------------------|-------|
"""
    items = listdir(img_dir)
    items.sort()

    for item in items:
        if item[0] not in [".", "_"] and os.path.exists(
            img_dir + "/" + item + "/image.jpg"
        ):
            try:
                with open(img_dir + "/" + item + "/info.json") as file:
                    json_file = json_load(file)

                img_path = f"{repo}/IRIP/img/{item}/image.jpg"

                output += f'| {json_file["name"]} |'
                output += f' {json_file["location"]} |'
                output += f' {json_file["photographer"]} |'
                output += f' {json_file["source"]} |'
                output += f' {json_file["description"]} |'
                output += f' <a href= "{img_path}">\
<img src="{img_path}" sizes="32x32"> </a> |'
                output += "\n"

                print(f"{item} output is writed")
            except (KeyError, ValueError):
                print(f"{item} not exists or have a problem in syntax")

    return output


readme = r"""<!-- auto generated dont edit-->

<div align="center">

[![codecov](https://codecov.io/gh/mmdbalkhi/IRPI-API/branch/main/graph/badge.svg?token=t4lclUtmvC)](https://codecov.io/gh/mmdbalkhi/IRPI-API)
[![Test](https://github.com/mmdbalkhi/IRPI-API/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/mmdbalkhi/IRPI-API/actions/workflows/test.yml)

</div>

# IRPI API

> **IR**AN **P** LECE **I** MAGE **API**

IRPI is a RESTful API. you can download Iran's beautiful Places image.

## Run

Please first create a virtual environment with the following command.

### MacOs/Linux

```sh
$ python3 -m venv env
$ . env/bin/activate
```

### Windwons

```batch
> py -3 -m venv env
> env\Scripts\activate
```

then install requirements:

```sh
$ pip install -e .
```

and run the app:

### bash

```sh
$ export FLASK_APP=IRIP/main.py
$ flask run
```

### cmd

```cmd
> set FLASK_APP=IRIP/main.py
> flask run
```

### powershell

```
> $env:FLASK_APP = "IRIP/main.py"
> flask run
```

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

## TODO:

- [ ] Add more images
- [ ] use flask-restful or etc
- [ ] add more features

"""

readme += generate_img_table()

with open(main_tree + "/README.md", "w") as file:

    file.write(readme)
    print("done!")
