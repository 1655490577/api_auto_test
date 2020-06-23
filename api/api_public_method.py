import requests
from config.config import server_ip


def login(**kwargs):
    url = server_ip() + '/admin/sysadmin/login'
    headers = {'Content-Type': 'application/json'}
    jsons = kwargs
    r = requests.post(url=url, json=jsons, headers=headers)
    return r


def change_password(cookies, **kwargs):
    url = server_ip() + '/admin/sysadmin/update'
    headers = {'Content-Type': 'application/json'}
    cookies = cookies
    jsons = kwargs
    r = requests.post(url=url, json=jsons, headers=headers, cookies=cookies)
    return r
