import requests
import json


def insert():
    URL = "http://127.0.0.1:8000/api/insert"
    data = {
        'name': 'S3',
        'age': 25,
        'roll': '233',
    }
    json_data = json.dumps(data)
    r = requests.post(
        URL, headers={"content-Type": "application/json"}, data=json_data)
    data = r.json()
    print(data)


def remove(id):
    URL = f"http://127.0.0.1:8000/api/remove/{id}"
    r = requests.delete(url=URL)
    data = r.json()
    print(data)


def get():
    URL = "http://127.0.0.1:8000/api/"
    r = requests.get(URL)
    data = r.json()
    for val in data:
        print(val)


def get_by_id(id):
    URL = f"http://127.0.0.1:8000/api/{id}"
    r = requests.get(URL)
    data = r.json()
    print(data)


def insert_view():
    URL = "http://127.0.0.1:8000/view/"
    data = {
        'name': 'S7',
        'age': 28,
        'roll': '03',
    }
    json_data = json.dumps(data)
    r = requests.post(
        URL, headers={"content-Type": "application/json"}, data=json_data)
    data = r.json()
    print(data)


def get_view():
    URL = "http://127.0.0.1:8000/view/"
    r = requests.get(URL)
    data = r.json()
    for val in data:
        print(val)


# get()
# get_by_id(24)
remove(24)
# insert()
