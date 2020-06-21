import requests
import pytest
import allure
from common.get_data import api_date
from config.config import server_ip


class TestLogin():

    url = server_ip() + '/admin/sysadmin/login'
    headers = {'Content-Type': 'application/json'}
    json = {
        "password": "string",
        "phone": "string",
        "rememberMe": True
    }

    @pytest.mark.parametrize('phone, password', api_date["login_success"])
    def test_login_001(self, phone, password):
        """
        用例描述：
        参数可以登录成功(管理员账号)
        :param phone: 登录手机号
        :param password: 登录密码
        :return:
        """
        json_date = {
            "password": password,
            "phone": phone,
            "rememberMe": True
        }

        r = requests.post(url=self.url, json=json_date, headers=self.headers)

        assert r.status_code == 200
        assert r.json()["data"] is not None
        assert r.json()["message"] == "成功"
        assert r.json()["status"] == "0"

    @pytest.mark.parametrize('phone, password', api_date["login_fail"])
    def test_login_002(self, phone, password):
        """
        用例描述：
        参数登录失败
        :param phone: 登录手机号
        :param password: 登录密码
        :return:
        """
        json_date = {
            "password": password,
            "phone": phone,
            "rememberMe": True
        }
        r = requests.post(url=self.url, json=json_date, headers=self.headers)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert r.json()["message"] == "手机号或密码不存在" or "password,不能为空" or "phone,不能为空"
        assert r.json()["status"] == "100005" or "100001"


if __name__ == '__main__':
    pytest.main()
