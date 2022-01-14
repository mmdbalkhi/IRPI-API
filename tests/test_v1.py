import json

from IRIP import create_app

client = create_app().test_client()


def test_find_random():

    response = json.loads(client.get("/v1/random").data)

    assert client.get("/v1/random").status_code == 200
    assert response["status"] == "ok"


def test_find_by_name():

    response = json.loads(client.get("/v1/find/example").data)

    assert client.get("/v1/find/example").status_code == 404
    assert response["status"] == "failed"
    assert response["msg"] == "img not exists"

    response = json.loads(client.get("/v1/find/iran_map").data)

    assert client.get("/v1/find/iran_map").status_code == 200
    assert response["status"] == "ok"
