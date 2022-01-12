<!-- auto generated dont edit-->

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
  "status": "ok",
  "image_name": "example",
  "image_path": "IRPI.com/img/place",
  "location": "example location",
  "photographer": "the photographer",
  "description": "a description"
}
```

### Find img by name

```
$ curl IRPI.com/v1/find/example
```

```json
{
  "status": "ok",
  "image_name": "example",
  "image_path": "api.com/img/place",
  "location": "example location",
  "photographer": "the photographer",
  "description": "a description"
}
```

## Photos

| Name | Location | Photographer | sender | description | view  |
|------|----------|--------------|--------|-------------|-------|
