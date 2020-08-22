from api.api_get_data import getter
import pytest
import allure


@pytest.mark.usefixtures('add_base_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminLogin(object):
    """
    "password": 密码
    "phone": 登录手机号
    "rememberMe": 是否记住
    """

    @pytest.mark.parametrize(('phone', 'password', 'rememberMe', 'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_login'][
                                 'test_user_login_success'])
    def test_user_login_success(self, phone, password, rememberMe, except_message, except_status):
        #   正确参数，登录成功
        with allure.step("step1: 步骤1 ==>> 使用用户名密码登录系统"):
            rsp_login = getter.user_login(phone=phone, password=password, rememberMe=rememberMe)

        assert rsp_login.status_code == 200
        assert rsp_login.json()['data'] is not None
        assert rsp_login.json()['message'] == except_message
        assert rsp_login.json()['status'] == except_status

    @pytest.mark.parametrize(('phone', 'password', 'rememberMe', 'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_login'][
                                 'test_user_login_fail'])
    def test_user_login_fail(self, phone, password, rememberMe, except_message, except_status):
        #   错误参数，登录失败
        with allure.step("step1: 步骤1 ==>> 使用用户名密码登录系统"):
            rsp_login = getter.user_login(phone=phone, password=password, rememberMe=rememberMe)

        assert rsp_login.status_code == 200
        assert rsp_login.json()['data'] is None
        assert rsp_login.json()['message'] in except_message
        assert rsp_login.json()['status'] == except_status


if __name__ == '__main__':
    pytest.main('-s', 'test_sys_admin_login.py')
