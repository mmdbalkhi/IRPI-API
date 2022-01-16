<!-- auto generated dont edit-->

# IRPI API

> IRan Place Img API

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
> env\Scriptsctivate
```

then install requirements:

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

| Name | Location | Photographer | source | description | view  |
|------|----------|---------|--------|---------------------------|-------|
| Azadi Tower | Tehran | muhammad muhammadi | [iran.ir](http://gallery.iran.ir/home?p_p_id=gallery_WAR_galleryportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_gallery_WAR_galleryportlet_cmd=load-page&_gallery_WAR_galleryportlet_page=%2Fhtml%2Fportlet%2Fgallery%2Fgallery_details.jsp&_gallery_WAR_galleryportlet_assetCategoryId=1281488&_gallery_WAR_galleryportlet_assetFileEntryId=803807) | The Azadi Tower (Persian: برج آزادی, Borj-e Āzādi; 'Freedom Tower'), formerly known as the Shahyad Tower (برج شهیاد, Borj-e Šahyād; 'Shah's Memorial Tower'), is a monument located on Azadi Square in Tehran, Iran. It is one of the landmarks of Tehran, marking the west entrance to the city, and is part of the Azadi Cultural Complex, which also includes an underground museum. [wikipedia](https://en.wikipedia.org/wiki/Azadi_Tower) | <a href= "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/azadi_tower/image.jpg"><img src="https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/azadi_tower/image.jpg" sizes="32x32"> </a> |
| Jamkaran Mosque | Qom | Haji | [iran.ir](http://gallery.iran.ir/home?p_p_id=gallery_WAR_galleryportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_gallery_WAR_galleryportlet_cmd=load-page&_gallery_WAR_galleryportlet_page=%2Fhtml%2Fportlet%2Fgallery%2Fgallery_details.jsp&_gallery_WAR_galleryportlet_assetCategoryId=1281492&_gallery_WAR_galleryportlet_itemNumber=5&_gallery_WAR_galleryportlet_assetFileEntryId=809984) | The Jamkaran Mosque (Persian: مسجد جمکران, Masjed-e Jamkarân) is one of the primary significant mosques in Jamkaran, a village in the outskirts of the city of Qom, Iran. [wikipedia](https://en.wikipedia.org/wiki/Jamkaran_Mosque) | <a href= "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/jamkaran_mosque/image.jpg"><img src="https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/jamkaran_mosque/image.jpg" sizes="32x32"> </a> |
| Nature of Ardabil | Ardabil | Naser Esmaili | [iran.ir](http://gallery.iran.ir/home?p_p_id=gallery_WAR_galleryportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_gallery_WAR_galleryportlet_cmd=load-page&_gallery_WAR_galleryportlet_page=%2Fhtml%2Fportlet%2Fgallery%2Fgallery_details.jsp&_gallery_WAR_galleryportlet_assetCategoryId=1281489&_gallery_WAR_galleryportlet_assetFileEntryId=1481641) | Ardabil city is the center of Ardabil province and it is considered to be one of the ancient regions of Iran with about 5000 years of history. Ardabil city is at the northwest of Iran near Iran’s border with the Republic of Azerbaijan.  Having a pleasant climate, cool summers and having the beautiful Savalan (Sabalan) mountain with its high and attractive peaks next to it which makes the climate of this city ever more pleasant, has added to the extraordinary beauty of this city, making it one of the tourism centers in the country. Tisazvasvari in Hungary and Erzurum in Turkey are the sister cities of Ardabil. [educationiran](http://educationiran.com/en/Ardabil/arums/page/21393/About-Ardabil) | <a href= "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/nature_of_ardabil/image.jpg"><img src="https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/nature_of_ardabil/image.jpg" sizes="32x32"> </a> |
| Persepolis | Shiraz | muhammad muhammadi | [iran.ir](http://gallery.iran.ir/home?p_p_id=gallery_WAR_galleryportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_gallery_WAR_galleryportlet_cmd=load-page&_gallery_WAR_galleryportlet_page=%2Fhtml%2Fportlet%2Fgallery%2Fgallery_details.jsp&_gallery_WAR_galleryportlet_assetCategoryId=1281488&_gallery_WAR_galleryportlet_assetFileEntryId=803744) | Persepolis (/pərˈsɛpəlɪs/; Old Persian: 𐎱𐎠𐎼𐎿, Pārsa; New Persian: تخت جمشید, romanized: Takht-e Jamshīd, lit. 'Throne of Jamshid') was the ceremonial capital of the Achaemenid Empire (c. 550–330 BC). It is situated in the plains of Marvdasht, encircled by southern Zagros mountains of Iran. Modern day Shiraz is situated 60 kilometres (37 mi) southwest of the ruins of Persepolis. The earliest remains of Persepolis date back to 515 BC. It exemplifies the Achaemenid style of architecture. UNESCO declared the ruins of Persepolis a World Heritage Site in 1979.[2]  [wikipedia](https://en.wikipedia.org/wiki/Persepolis) | <a href= "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/persepolis/image.jpg"><img src="https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/persepolis/image.jpg" sizes="32x32"> </a> |
| Si-o-se-pol | Isfahan | muhammad muhammad nia | [iran.ir](http://gallery.iran.ir/home?p_p_id=gallery_WAR_galleryportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_gallery_WAR_galleryportlet_cmd=load-page&_gallery_WAR_galleryportlet_page=%2Fhtml%2Fportlet%2Fgallery%2Fgallery_details.jsp&_gallery_WAR_galleryportlet_assetCategoryId=1281488&_gallery_WAR_galleryportlet_assetFileEntryId=803786) | The Allahverdi Khan Bridge (Persian: پل الله‌وردی خان), popularly known as Si-o-se-pol (Persian: سی‌وسه‌پل, lit. '[the] bridge of thirty-three [spans]'),[1] is the largest of the eleven historical bridges on the Zayanderud, the largest river of the Iranian Plateau, in Isfahan, Iran.[2] The bridge was built in the early 17th century to serve as both a bridge and a dam.[3] It is a popular recreational gathering place, and is one of the most famous examples of Iran's Safavid architecture.   [wikipedia](https://en.wikipedia.org/wiki/Si-o-se-pol) | <a href= "https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/si-o-se-pol/image.jpg"><img src="https://raw.githubusercontent.com/mmdbalkhi/IRPI-API/main/IRIP/img/si-o-se-pol/image.jpg" sizes="32x32"> </a> |
