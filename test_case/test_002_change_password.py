import pytest
import allure
from common.get_data import get_data
from common.get_token_cookies import get_login_token_cookies
from api.api_public_method import change_password, login


class Test_change_password(object):

    @pytest.mark.skipif(login(phone="admin", password="admin", rememberMe=True).json()["status"] != "0",
                        reason="admin用户登录失败")
    @pytest.mark.parametrize('id,name,change_pwd,change_phone,login_pwd,login_phone,userId',
                             get_data('change_password_data.yml')["test_change_password_success"])
    def test_update_password_system(self, id, name, change_pwd, change_phone, login_pwd, login_phone, userId):
        """
        用例描述：
        1.使用系统管理员账号登录并修改自己的密码
        2.使用公司管理员账号登录并修改自己的密码
        3.使用部门用户账号登录并修改自己的密码
        4.使用组用户账号登录并修改自己的密码
        5.系统管理员修改系统管理员密码
        6.系统管理员修改公司管理员密码
        7.系统管理员修改部门用户密码
        8.系统管理员修改组用户密码
        """
        with allure.step("step1: 步骤1 ==>> 登录并获取token,cookies"):
            token, cookies = get_login_token_cookies(phone=login_phone, password=login_pwd, rememberMe=True)
        with allure.step("step2: 步骤2 ==>> 系统管理员直接开始修改其他人的密码为原密码+‘123’"):
            r1 = change_password(cookies, id=id, name=name, password=change_pwd + '123',
                                 phone=login_phone, token=token, userid=userId)
        with allure.step("step3: 步骤3 ==>> 被修改的用户使用新密码登录系统"):
            r2 = login(phone=change_phone, password=change_pwd + '123', rememberMe=True)
        if login_phone == change_phone:
            with allure.step("step4: 重新登录并获取token,cookies"):
                token2, cookies2 = get_login_token_cookies(phone=login_phone, password=login_pwd + "123",
                                                           rememberMe=True)
            with allure.step("step5: 步骤5 ==>> 用户再把自己的密码由原密码+‘123’变回原密码"):
                r3 = change_password(cookies2, id=id, name=name, password=login_pwd, phone=login_phone,
                                     token=token2, userid=userId)
        else:
            with allure.step("step4: 重新登录并获取token,cookies"):
                token2, cookies2 = get_login_token_cookies(phone=login_phone, password=login_pwd, rememberMe=True)
            with allure.step("step5: 步骤5 ==>> 系统管理员再把各用户的密码由原密码+‘123’变回原密码"):
                r3 = change_password(cookies2, id=id, name=name, password=change_pwd, phone=login_phone,
                                     token=token2, userid=userId)

        assert r1.status_code == 200
        assert r1.json()["data"] is None
        assert r1.json()["message"] == "成功"
        assert r1.json()["status"] == "0"
        assert r2.status_code == 200
        assert r2.json()["data"] is not None
        assert r2.json()["message"] == "成功"
        assert r2.json()["status"] == "0"

    @pytest.mark.parametrize('id,name,change_pwd,login_pwd,phone,userId',
                             get_data('change_password_data.yml')["test_change_password_noLogin"])
    def test_update_password_no_login_001(self, id, name, change_pwd, login_pwd, phone, userId):
        """
        用例描述：
        1.未登录状态，系统管理员修改组用户密码
        2.未登录状态，组用户修改系统管理员密码
        3.未登录状态，修改自己的密码
        """
        with allure.step("step1: 步骤1 ==>> 不获取cookie,仅获取token"):
            token = get_login_token_cookies(phone=phone, password=login_pwd, rememberMe=True)[0]
        with allure.step("step2: 步骤2 ==>> 直接修改密码"):
            r = change_password(None, id=id, name=name, password=change_pwd, userid=userId, token=token)

        assert r.status_code == 200
        assert r.json()["message"] == "请登录后进行操作!"
        assert r.json()["status"] == "200006"


if __name__ == '__main__':
    pytest.main('-s', 'test_002_change_password')
