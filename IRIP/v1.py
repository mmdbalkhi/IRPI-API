"""
    IRPI
    ~~~~~

    An api based on the flask. this API Publish
    images from  the Iran beautiful places

    :license: GPL-3

    * The Images have copyright license *
"""
import os
import random
from json import load as json_load
from typing import Dict
from uuid import uuid4

from flask import Blueprint
from flask import jsonify
from flask import request

image_path = os.path.dirname(os.path.abspath(__file__)) + "/img/"

bp = Blueprint("v1", __name__)


def find_img_date(img_name: str) -> Dict:
    path = f"{image_path}{img_name}"
    try:
        with open(f"{path}/info.json") as file:
            return json_load(file)
    except ValueError:
        return


@bp.route("/v1/random", methods=["GET"])
def find_random():

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
def find_by_name(img_name):

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
def internal_server_error(e):
    return (
        jsonify({"status": "failed", "msg": "500 Internal Server Error"}),
        500,
    )
