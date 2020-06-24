import pytest
import allure
from common.get_data import get_data
from api.api_public_method import login


@allure.feature('登录功能')
class TestLogin(object):

    @allure.story('正确账号，正确密码，登录成功')
    @pytest.mark.parametrize('phone, password, remember', get_data('login_data.yml')["login_success"])
    def test_login_001(self, phone, password, remember):
        """
        用例描述：
        参数可以登录成功
        :param phone: 登录手机号
        :param password: 登录密码
        """
        r = login(phone=phone, password=password, rememberMe=remember)
        assert r.status_code == 200
        assert r.json()["data"] is not None
        assert r.json()["message"] == "成功"
        assert r.json()["status"] == "0"

    @allure.story('正确手机号，错误密码/错误手机号，正确密码，登录失败')
    @pytest.mark.parametrize('phone, password, remember', get_data('login_data.yml')["login_error_fail"])
    def test_login_002(self, phone, password, remember):
        """
        用例描述：
        参数输入错误
        :param phone: 登录手机号
        :param password: 登录密码
        :return:
        """
        r = login(phone=phone, password=password, rememberMe=remember)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert r.json()["message"] == "手机号或密码不存在"
        assert r.json()["status"] == "100005"

    @allure.story('phone或password或rememberMe为空，登录失败')
    @pytest.mark.parametrize('phone, password, remember', get_data('login_data.yml')["login_null_fail"])
    def test_login_003(self, phone, password, remember):
        """
        用例描述：
        参数输入为空
        :param phone: 登录手机号
        :param password: 登录密码
        :return:
        """
        r = login(phone=phone, password=password, rememberMe=remember)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert ",不能为空" in r.json()["message"]
        assert r.json()["status"] == "100001"

    @allure.story('参数password不传，登录失败')
    @pytest.mark.parametrize('phone, remember', get_data('login_data.yml')["login_nopassword_fail"])
    def test_login_004(self, phone, remember):
        """
        用例描述：
        参数password不传
        :param phone: 登录手机号
        :return:
        """
        r = login(phone=phone, rememberMe=remember)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert r.json()["message"] == "password,不能为空!"
        assert r.json()["status"] == "100001"

    @allure.story('参数phone不传，登录失败')
    @pytest.mark.parametrize('password, remember', get_data('login_data.yml')["login_nophone_fail"])
    def test_login_005(self, password, remember):
        """
        用例描述：
        参数phone不传
        :param password: 登录密码
        :return:
        """
        r = login(password=password, rememberMe=remember)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert r.json()["message"] == "phone,不能为空!"
        assert r.json()["status"] == "100001"

    @allure.story('参数rememberMe不传，登录失败')
    @pytest.mark.parametrize('phone, password', get_data('login_data.yml')["login_norememberme_fail"])
    def test_login_006(self, phone, password):
        """
        用例描述：
        参数rememberMe不传
        :param phone: 登录手机号
        :param password: 登录密码
        :return:
        """
        r = login(phone=phone, password=password)
        assert r.status_code == 200
        assert r.json()['data'] is None
        assert r.json()["message"] == "rememberMe,不能为空!"
        assert r.json()["status"] == "100001"


if __name__ == '__main__':
    pytest.main()
