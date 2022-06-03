import os
from json import load as json_load

from .typing import Dict
from .typing import Union

image_path = os.path.dirname(os.path.abspath(__file__)) + "/img/"


def find_img_date(img_name: str) -> Union[Dict, None]:
    """find image data from json file in the image Directory

    Args:
        img_name (str): name of the img

    Returns:
        Dict: the json data from the file
    """
    path = f"{image_path}{img_name}"  # TODO: img_name = path in img directory
    try:
        with open(f"{path}/info.json", encoding="utf-8") as file:
            return json_load(file)
    except FileNotFoundError:
        return None


def search_with_regex(name: str) -> None:
    return
