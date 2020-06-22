import requests
import pytest
import allure
from common.get_data import api_date
from config.config import server_ip


class Test_change_password(object):

    url = server_ip() + '/admin/sysadmin/update'
    headers = {'Content-Type': 'application/json'}
    url2 = server_ip() + '/admin/sysadmin/login'
    json = {
        "id": '',
        "name": "string",
        "password": "string",
        "token": "string",
        "userid": "string"
    }

    def test_update_password(self, login):
        json1 = {
            "id": login[1],
            "name": login[0],
            "password": "123456",
            "token": login[2],
            "userid": login[1]
        }
        r = requests.post(url=self.url, json=json1, headers=self.headers)
        json2 = {
            "password": "13168775546",
            "phone": "123456",
            "rememberMe": True
        }
        r2 = requests.post(url=self.url2, json=json2, headers=self.headers)
        assert r.status_code == 200
        assert r.json()["data"] is not None
        assert r.json()["message"] == "成功"
        assert r.json()["status"] == "0"
        assert r2.status_code == 200
        assert r2.json()["data"] is not None
        assert r2.json()["message"] == "成功"
        assert r2.json()["status"] == "0"


if __name__ == '__main__':
    pytest.main('-s', 'test_002_change_password')
