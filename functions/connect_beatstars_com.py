import http.client
import json


def connect_beatstars_com(url_from_request: str) -> json:
    connect = http.client.HTTPSConnection("main.v2.beatstars.com")
    connect.request("GET", url_from_request)
    response = connect.getresponse()
    data = response.read().decode("utf-8")
    data_json = json.loads(data)
    return data_json
