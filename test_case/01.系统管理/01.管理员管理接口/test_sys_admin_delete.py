from api.api_get_data import getter
from common.read_data import data
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("clear_sysRole")
@pytest.mark.usefixtures("clear_sysAdmin")
class TestSysAdminDelete(object):
    """
    参数列表
    "id": "string",
    "token": "string",
    "userid": "string"
    """
    @pytest.mark.parametrize(('login_phone', 'login_password', 'update_user_id',
                              'update_user_phone', 'update_user_password'),
                             data.load_yaml('sys_delete_data.yml')['delete_success'])
    def test_delete_success(self, login_phone, login_password, update_user_id, update_user_phone, update_user_password):
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password, True)
        with allure.step("step1: 步骤2 ==>> 删除其他用户"):
            rsp_delete = getter.user_delete(cookies, id=update_user_id, token=token, userid=userId)
        with allure.step("step1: 步骤3 ==>> 登录被删除的用户账号"):
            rsp_login = getter.user_login(phone=update_user_phone, password=update_user_password, rememberMe=True)

        assert rsp_delete.json()
        assert rsp_login.json()

    def test_delete_fail(self):
        pass


if __name__ == '__main__':
    pytest.main('-s', 'test_sys_admin_delete.py')
