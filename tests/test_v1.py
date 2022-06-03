import json

import pytest

from IRIP import create_app


def test_find_random(client):

    response = json.loads(client.get("/v1/random").data)

    assert client.get("/v1/random").status_code == 200
    assert response["status"] == "ok"


def test_find_by_name_404(client):

    response = json.loads(client.get("/v1/find/example").data)

    assert client.get("/v1/find/example").status_code == 404
    assert response["status"] == "failed"
    assert response["msg"] == "img not exists"


def test_find_by_name_200(client):

    response = json.loads(client.get("/v1/find/azadi_tower").data)

    assert client.get("/v1/find/azadi_tower").status_code == 200
    assert response["status"] == "ok"
