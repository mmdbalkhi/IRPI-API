# -*- coding: utf-8 -*-
"""
    IRPI
    ~~~~~

    An api based on the flask. this API Publish
    images from  the Iran beautiful places 
    
    :license: GPL-3
    
    * The Images have copyright license *
"""
import random
import os

from flask import Config, Flask, Markup, abort, jsonify, request
app = Flask(__name__, static_folder='img')

app.secret_key = "dev"

image_path = os.getcwd()+"/img" if "app" in os.getcwd() else os.getcwd()+"/app/img/"

def place(): #TODO: work it
    return None

@app.route("/v1/random", methods=["GET"])
def v1_random():
    img_name = random.choice(os.listdir(image_path))
    img_place = place()
    img_path = f"{request.host_url}/img/{img_name}"

    return jsonify(
        {
            "status": "ok",
            "image_name" : img_name,
            "place" : img_place,
            "image_path" : img_path
        }
    ), 200
    
@app.route("/v1/find/<img_name>", methods=["GET"])
def v1_by_name(img_name):
    
    if ".jpg" not in img_name:
        img_name += ".jpg"

    if os.path.exists(f"{image_path}{img_name}"):
        img_place = place()
        img_path = f"{request.host_url}img/{img_name}"

        return jsonify(
            {
                "status": "ok",
                "img name" : img_name,
                "place" : img_place,
                "img url" : img_path
            }
        ), 200
    return jsonify(
            {
                "status" : "failed",
                "img name" : img_name,
                "msg" : "img not exists"
            }
        ), 404


app.run(debug=True)