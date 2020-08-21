from api.api_get_data import getter
from common.read_data import data
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminDeleteFail(object):
    """
    不能删除的情况
    参数列表
    "id": "string",
    "token": "string",
    "userid": "string"
    """
    @pytest.mark.parametrize(('login_phone', 'login_password', 'update_user_phone', 'update_user_password'),
                             data.load_yaml('userDeleteData.yml')['delete_fail'])
    def test_delete_fail(self, login_phone, login_password, update_user_phone, update_user_password):
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password, True)

        with allure.step("step2: 步骤2 ==>> 登录被删除用户，获取该用户id,特殊情况判断，自己删除自己账号"):
            if login_phone == update_user_phone:
                update_user_id = userId
            else:
                update_user_id = getter.user_login(phone=update_user_phone, password=update_user_password,
                                                   rememberMe=False).json()['data']['sysAdmin']['id']

        with allure.step("step3: 步骤3 ==>> 删除其他用户"):
            rsp_delete = getter.user_delete(cookies, id=update_user_id, token=token, userid=userId)
            print(rsp_delete.json())

        assert rsp_delete.json()['data'] is None
        assert rsp_delete.json()['message'] == '用户没有权限'
        assert rsp_delete.json()['status'] == '100011'


@pytest.mark.usefixtures('add_user')
class TestSysAdminDeleteSuccess(object):
    """
    可以成功删除的情况
    参数列表S
    "id": "string",
    "token": "string",
    "userid": "string"
    """
    @pytest.mark.parametrize(('login_phone', 'login_password','update_user_phone', 'update_user_password'),
                             data.load_yaml('userDeleteData.yml')['delete_success'])
    def test_delete_success(self, login_phone, login_password, update_user_phone, update_user_password):
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password, True)

        with allure.step("step2: 步骤2 ==>> 登录被删除用户，获取该用户id"):
            update_user_id = getter.user_login(phone=update_user_phone, password=update_user_password,
                                               rememberMe=False).json()['data']['sysAdmin']['id']

        with allure.step("step3: 步骤3 ==>> 删除其他用户"):
            rsp_delete = getter.user_delete(cookies, id=update_user_id, token=token, userid=userId)

        with allure.step("step4: 步骤4 ==>> 登录被删除的用户账号"):
            rsp_login = getter.user_login(phone=update_user_phone, password=update_user_password, rememberMe=True)

        assert rsp_delete.json()['data'] is None
        assert rsp_delete.json()['message'] == '成功'
        assert rsp_delete.json()['status'] == '0'
        assert rsp_login.json()['data'] is None
        assert rsp_login.json()['message'] == '手机号或密码不存在'
        assert rsp_login.json()['status'] == '100005'


if __name__ == '__main__':
    pytest.main('-s', 'test_sys_admin_delete.py')
