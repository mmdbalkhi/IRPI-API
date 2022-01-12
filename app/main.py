# -*- coding: utf-8 -*-
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
from json import load
from typing import Dict
from uuid import uuid4

from flask import Config, Flask, Markup, abort, jsonify, request

app = Flask(__name__, static_folder='img')

app.secret_key = "dev"

image_path = os.getcwd()+"/img" if "app" in os.getcwd() else os.getcwd()+"/app/img/"

def find_img_date(img_name:str) -> Dict:
    
    try:
        with open(f"{image_path}{img_name}/info.json") as file:
            return load(file)
    except:
        return


@app.route("/v1/random", methods=["GET"])
def v1_random():

    img_name = random.choice(os.listdir(image_path))
    img_data = find_img_date(img_name)
    img_path = f"{request.host_url}img/{img_name}/image.jpg" # FIX: HARD CODE! 

    return jsonify(
        {
            "id":uuid4(),
            "status": "ok",
            "image_name" : img_name,
            "data" : img_data,
            "image_path" : img_path
        }
    ), 200
    
@app.route("/v1/find/<img_name>", methods=["GET"])
def v1_by_name(img_name):


    if os.path.exists(f"{image_path}{img_name}/image.jpg"):
        img_data = find_img_date(img_name)
        img_path = f"{request.host_url}img/{img_name}/image.jpg"

        return jsonify(
            {
                "id":uuid4(),
                "status": "ok",
                "img name" : img_name,
                "data" : img_data,
                "img url" : img_path
            }
        ), 200
    return jsonify(
            {
                "id":uuid4(),
                "status" : "failed",
                "img name" : img_name,
                "msg" : "img not exists"
            }
        ), 404
