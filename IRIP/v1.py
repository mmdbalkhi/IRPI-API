"""
    IRPI
    ~~~~~

    An api based on the flask. this API Publish
    images from  the Iran beautiful places

    :license: GPL-3

    * The Images have copyright license *
"""
import random
from uuid import uuid4

from flask import Blueprint, jsonify, request

from .typing import Json
from .utils import find_img_date, image_path, os

bp = Blueprint("v1", __name__)


@bp.route("/v1/random", methods=["GET"])
def find_random() -> Json:
    """Find Random Image From Images And Return this img's data

    Returns:
        Json: Json data images

        *    JSON Data with the image are name, location, photographer, etc.
    """
    img_name = random.choice(os.listdir(image_path))
    img_data = find_img_date(img_name)
    img_path = f"{request.host_url}img/{img_name}/image.jpg"  # FIX: HARD CODE!

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
def find_by_name(img_name: str) -> Json:  # TODO: add regex to search
    """get a name from the user and if this
    image exists, return this image data for users

    Args:
        img_name (str): name of the image

    Returns:
        Json: return image info and image path to the user
    """

    if os.path.exists(f"{image_path}{img_name}/image.jpg"):
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


@bp.errorhandler(500)
def internal_server_error(e: int) -> Json:
    """handle 500 http error

    Args:
        e (int): http error from the server

    Returns:
        Json: error details
    """
    return (
        jsonify({"status": "failed", "msg": "500 Internal Server Error"}),
        e,
    )
