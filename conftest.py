import requests
from config.config import server_ip
import pytest


@pytest.fixture(scope='class')
def login():
    url = server_ip() + '/admin/sysadmin/login'
    headers = {'Content-Type': 'application/json'}
    json = {
        "password": '123456',
        "phone": '13168775546',
        "rememberMe": True
    }
    r = requests.post(url=url, headers=headers, json=json)
    # token = r.json()['data']['token']
    # userid = r.json()['data']['sysAdmin']['id']
    # name = r.json()['data']['sysAdmin']['name']

