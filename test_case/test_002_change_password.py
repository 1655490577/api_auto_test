import pytest
import allure
from common.get_data import get_data
from common.get_token_cookies import get_login_token_cookies
from api.api_public_method import change_password, login


class Test_change_password(object):

    # @pytest.mark.parametrize('id,name,password,phone,userid',
    #                          get_data('change_password_data.yml')["test_change_password_myself"])
    # def test_update_password_myself(self, id, name, password, phone, userid):
    #     """
    #     用例描述：
    #     1.使用系统管理员账号登录并修改自己的密码，最后再修改回原密码；
    #     2.使用公司管理员账号登录并修改自己的密码，最后再修改回原密码；
    #     3.使用部门用户账号登录并修改自己的密码，最后再修改回原密码；
    #     4.使用组用户账号登录并修改自己的密码，最后再修改回原密码；
    #     """
    #     with allure.step("step1: 步骤1 ==>> 登录并获取token,cookies"):
    #         token, cookies = get_login_token_cookies(phone=phone, password=password, rememberMe=True)
    #     with allure.step("step2: 步骤2 ==>> 修改密码为：原密码+'123'"):
    #         r1 = change_password(cookies,id=id, name=name, password=password+'123',
    #                              phone=phone, token=token, userid=userid)
    #     with allure.step("step3: 步骤3 ==>> 使用新密码重新登录系统"):
    #         r2 = login(phone=phone, password=password+'123', rememberMe=True)
    #     with allure.step("step4: 重新登录并获取token,cookies"):
    #         token2, cookies2 = get_login_token_cookies(phone=phone, password=password+"123", rememberMe=True)
    #     with allure.step("step5: 步骤5 ==>> 把密码改回原来的密码"):
    #         change_password(cookies2,id=id, name=name, password=password, phone=phone, token=token2, userid=userid)
    #
    #     assert r1.status_code == 200
    #     assert r1.json()["data"] is None
    #     assert r1.json()["message"] == "成功"
    #     assert r1.json()["status"] == "0"
    #     assert r2.status_code == 200
    #     assert r2.json()["data"] is not None
    #     assert r2.json()["message"] == "成功"
    #     assert r2.json()["status"] == "0"
    #
    # @pytest.mark.parametrize('id,name,password,phone,userid',
    #                          get_data('change_password_data.yml')["test_change_password_nologin01"])
    # def test_update_password_no_login_001(self, id, name, password, phone, userid):
    #     """
    #     用例描述：
    #     未登录获取cookies，直接修改自己的密码
    #     """
    #     with allure.step("step1: 步骤1 ==>> 不获取cookie,仅获取token"):
    #         token = get_login_token_cookies(phone=phone, password=password, rememberMe=True)[0]
    #     with allure.step("step2: 步骤2 ==>> 直接修改密码"):
    #         r = change_password(None, id=id, name=name, password=password, userid=userid, token=token)
    #
    #     assert r.status_code == 200
    #     assert r.json()["message"] == "请登录后进行操作!"
    #     assert r.json()["status"] == "200006"
    #
    # @pytest.mark.parametrize('id,name,password_updata,password_login,phone,userid',
    #                          get_data('change_password_data.yml')["test_change_password_nologin02"])
    # def test_update_password_no_login_002(self, id, name, password_updata, password_login, phone, userid):
    #     """
    #     用例描述：
    #     1.未登录状态，系统管理员修改组用户密码
    #     2.未登录状态，组用户修改系统管理员密码
    #     """
    #     with allure.step("step1: 步骤1 ==>> 不获取cookie,仅获取token"):
    #         token = get_login_token_cookies(phone=phone, password=password_login, rememberMe=True)[0]
    #     with allure.step("step2: 步骤2 ==>> 直接修改密码"):
    #         r = change_password(None, id=id, name=name, password=password_updata, userid=userid, token=token)
    #         print(r.json())
    #
    #     assert r.status_code == 200
    #     assert r.json()["message"] == "请登录后进行操作!"
    #     assert r.json()["status"] == "200006"

    @pytest.mark.parametrize('id,name,password_updata,password_login,phone,userid',
                             get_data('change_password_data.yml')["test_change_password_nologin02"])
    def test_update_password_no_login_002(self, id, name, password_updata, password_login, phone, userid):
        """
        用例描述：
        1.未登录状态，系统管理员修改组用户密码
        2.未登录状态，组用户修改系统管理员密码
        """
        with allure.step("step1: 步骤1 ==>> 不获取cookie,仅获取token"):
            token = get_login_token_cookies(phone=phone, password=password_login, rememberMe=True)[0]
        with allure.step("step2: 步骤2 ==>> 直接修改密码"):
            r = change_password(None, id=id, name=name, password=password_updata, userid=userid, token=token)
            print(r.json())

        assert r.status_code == 200
        assert r.json()["message"] == "请登录后进行操作!"
        assert r.json()["status"] == "200006"


if __name__ == '__main__':
    pytest.main('-s', 'test_002_change_password')
