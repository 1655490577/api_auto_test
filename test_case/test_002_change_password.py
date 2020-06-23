import pytest
import allure
from common.get_data import api_date
from common.get_token import *
from api.api_public_method import change_password, login


class Test_change_password(object):

    @pytest.mark.parametrize('id,name,password,phone,userid', api_date["test_system"])
    def test_update_password(self, id, name, password, phone, userid):

        r1 = change_password(system_cookies, id=id,name=name,password=password,phone=phone,token=system_token,userid=userid)
        r2 = login(phone=phone, password=password, rememberMe=True)

        assert r1.status_code == 200
        assert r1.json()["data"] is None
        assert r1.json()["message"] == "成功"
        assert r1.json()["status"] == "0"
        assert r2.status_code == 200
        assert r2.json()["data"] is not None
        assert r2.json()["message"] == "成功"
        assert r2.json()["status"] == "0"


if __name__ == '__main__':
    pytest.main('-s', 'test_002_change_password')
