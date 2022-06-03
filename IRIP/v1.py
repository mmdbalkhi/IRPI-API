"""
    IRPI
    ~~~~~

    An api based on the flask. this API Publish
    images from  the Iran beautiful places

    :license: GPL-3

    * The Images have copyright license *
"""
import random
import re
from uuid import uuid4

from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response

from .typing import Tuple
from .utils import find_img_date
from .utils import image_path
from .utils import os

bp = Blueprint("v1", __name__)
list_files = os.listdir(image_path)


@bp.route("/v1/random", methods=["GET"])
def find_random() -> Tuple[Response, int]:
    """Find Random Image From Images And Return this img's data

    Returns:
        Json: Json data images

        *    JSON Data with the image are name, location, photographer, etc.
    """
    img_name = random.choice(os.listdir(image_path))
    img_data = find_img_date(img_name)
    img_path = f"{request.host_url}img/{img_name}/image.jpg"

    return (
        jsonify(
            {
                "id": uuid4(),
                "status": "ok",
                "image_name": img_name,
                "data": img_data,
                "image_path": img_path,
            }
        ),
        200,
    )


@bp.route("/v1/find/<img_name>", methods=["GET"])
def find_by_name(img_name: str) -> Tuple[Response, int]:
    """get a name from the user and if this
    image exists, return this image data for users

    Args:
        img_name (str): name of the image

    Returns:
        Json: return image info and image path to the user
    """

    img_name = img_name.lower()
    if any([img for img in list_files if re.findall(img_name, img)]):
        img_data = find_img_date(img_name)
        img_path = f"{request.host_url}img/{img_name}/image.jpg"

        return (
            jsonify(
                {
                    "id": uuid4(),
                    "status": "ok",
                    "img name": img_name,
                    "data": img_data,
                    "img url": img_path,
                }
            ),
            200,
        )
    return (
        jsonify(
            {
                "id": uuid4(),
                "status": "failed",
                "img name": img_name,
                "msg": "img not exists",
            }
        ),
        404,
    )
