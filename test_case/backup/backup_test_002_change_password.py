import pytest
import allure
from api.api_get_data import getter


@pytest.mark.skip("不管了")
@allure.feature('修改密码功能')
class Test_change_password(object):

    @pytest.mark.skipif(getter.user_login(phone="admin", password="admin", rememberMe=True).json()["status"] != "0",
                        reason="admin用户登录失败")
    @pytest.mark.parametrize('id,name,change_pwd,change_phone,login_pwd,login_phone',
                             getter.load_yaml('change_password_data.yml')["test_change_password_success"])
    def test_update_password_system_success(self, id, name, change_pwd, change_phone, login_pwd, login_phone):
        """
        用例描述：
        用户修改密码（有效等价类）
        """
        with allure.step("step1: 步骤1 ==>> 登录并获取token,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(phone=login_phone, password=login_pwd,
                                                                    rememberMe=True)
        with allure.step("step2: 步骤2 ==>> 系统管理员直接开始修改其他人的密码为原密码+‘123’"):
            r1 = getter.user_update(cookies, id=id, name=name, password=change_pwd + '123',
                                    phone=login_phone, token=token, userid=userId)
        with allure.step("step3: 步骤3 ==>> 被修改的用户使用新密码登录系统"):
            r2 = getter.user_login(phone=change_phone, password=change_pwd + '123', rememberMe=True)
        #   登录手机号与被修改手机号相等为用户修改自己的密码，不相等为修改其他用户密码
        if login_phone == change_phone:
            with allure.step("step4: 重新登录并获取token,cookies"):
                token2, userId, cookies2 = getter.get_login_token_cookies(phone=login_phone, password=login_pwd + "123",
                                                                          rememberMe=True)
            with allure.step("step5: 步骤5 ==>> 用户再把自己的密码由原密码+‘123’变回原密码"):
                getter.user_update(cookies2, id=id, name=name, password=login_pwd, phone=login_phone,
                                   token=token2, userid=userId)
        else:
            with allure.step("step4: 重新登录并获取token,cookies"):
                token2, userId, cookies2 = getter.get_login_token_cookies(phone=login_phone, password=login_pwd,
                                                                          rememberMe=True)
            with allure.step("step5: 步骤5 ==>> 系统管理员再把各用户的密码由原密码+‘123’变回原密码"):
                getter.user_update(cookies2, id=id, name=name, password=change_pwd, phone=login_phone,
                                   token=token2, userid=userId)
        try:
            assert r1.status_code == 200
            assert r1.json()["data"] is None
            assert r1.json()["message"] == "成功"
            assert r1.json()["status"] == "0"
            assert r2.status_code == 200
            assert r2.json()["data"] is not None
            assert r2.json()["message"] == "成功"
            assert r2.json()["status"] == "0"
        except AssertionError as error:
            print(r1.json()["message"], r2.json()["message"])
            raise error

    @pytest.mark.skipif(getter.user_login(phone="admin", password="admin", rememberMe=True).json()["status"] != "0",
                        reason="admin用户登录失败")
    @pytest.mark.parametrize('id,name,change_pwd,change_phone,login_pwd,login_phone',
                             getter.load_yaml('change_password_data.yml')["test_change_password_fail"])
    def test_update_password_system_fail(self, id, name, change_pwd, change_phone, login_pwd, login_phone):
        """
        用例描述：
        用户修改密码（无效等价类）
        """
        with allure.step("step1: 步骤1 ==>> 登录并获取token,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(phone=login_phone, password=login_pwd,
                                                                    rememberMe=True)
        with allure.step("step2: 步骤2 ==>> 系统管理员直接开始修改其他人的密码为原密码+‘123’"):
            r = getter.user_update(cookies, id=id, name=name, password=change_pwd + '123',
                                   phone=login_phone, token=token, userid=userId)
        try:
            assert r.json()["data"] is None
            assert r.json()["message"] == "用户没有权限"
            assert r.json()["status"] == "100011"
        except AssertionError as error:
            print(r.json()["message"])
            raise error

    @pytest.mark.parametrize('id,name,change_pwd,login_pwd,phone,userId',
                             getter.load_yaml('change_password_data.yml')["test_change_password_noLogin"])
    def test_update_password_no_login(self, id, name, change_pwd, login_pwd, phone, userId):
        """
        用例描述：
        1.未登录状态，系统管理员修改组用户密码
        2.未登录状态，组用户修改系统管理员密码
        3.未登录状态，修改自己的密码
        """
        with allure.step("step1: 步骤1 ==>> 不获取cookie,仅获取token"):
            token = getter.get_login_token_cookies(phone=phone, password=login_pwd, rememberMe=True)[0]
        with allure.step("step2: 步骤2 ==>> 直接修改密码"):
            r = getter.user_update(None, id=id, name=name, password=change_pwd, userid=userId, token=token)
        try:
            assert r.status_code == 200
            assert r.json()["message"] == "请登录后进行操作!"
            assert r.json()["status"] == "200006"
        except AssertionError as error:
            print(r.json()["message"])
            raise error


if __name__ == '__main__':
    pytest.main('-s', 'test_002_change_password')