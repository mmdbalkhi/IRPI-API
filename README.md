<!-- auto generated dont edit-->

# IRPI API

> IRan Place Img API

IRPI is a RESTful API. your can download Iran beautiful Place img.

## Run

first plase install requirements:

```sh
$ pip install -r requirements/requirements.txt
$ pip install -e .
```

and run the app:

- bash

```sh
$ export FLASK_APP=src/main.py
$ flask run
```

- cmd

```cmd
> set FLASK_APP=hello
> flask run
```

- powershell
```
> $env:FLASK_APP = "hello"
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

## Photos

| Name | Location | Photographer | sender | description | view  |
|------|----------|--------------|--------|-------------|-------|
