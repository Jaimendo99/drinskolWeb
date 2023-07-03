import requests

base_url = "https://dev.drinskol.fun/api/" 

def login(username, password):
    endpoint = "user/login"
    data = {
    "username": username,
    "password": password
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url + endpoint, json=data, headers=headers)
    return response


def create_user(username, password, email, name, last_name, birth_date, img_url, is_admin=False, token=None):
    endpoint = "user/create/"
    new_user = {
        "password": password,
        "last_name": last_name,
        "username": username,
        "birth_date": birth_date,
        "image_src": img_url,
        "name": name,
        "email": email,
        "is_admin": is_admin
    }

    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token


    response = requests.post(base_url + endpoint, json=new_user, headers=headers)
    return response


