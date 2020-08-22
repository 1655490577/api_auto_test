from api.api_get_data import getter
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminResetSuccess(object):
    """
    重置密码成功
    参数列表：
    id              id
    token           token唯一标识
    userid          用户id唯一标识
    """

    @pytest.mark.parametrize(('login_phone', 'login_password', 'update_user_phone', 'update_user_password',
                              'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_reset'][
                                 'test_sys_admin_reset_success'])
    def test_user_reset_success(self, login_phone, login_password, update_user_phone, update_user_password,
                                except_message, except_status):
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 登录被重置用户，获取该用户id"):
            update_user_id = getter.user_login(phone=update_user_phone, password=update_user_password,
                                               rememberMe=False).json()['data']['sysAdmin']['id']

        with allure.step("step3: 步骤3 ==>> 重置用户密码"):
            rsp_reset = getter.user_reset(cookies, id=update_user_id, token=token, userid=userId)

        assert rsp_reset.status_code == 200
        assert rsp_reset.json()['data'] is None
        assert rsp_reset.json()['message'] == except_message
        assert rsp_reset.json()['status'] == except_status


@pytest.mark.usefixtures('add_user')
class TestSysAdminResetFail(object):
    """
    重置密码失败
    参数列表：
    id              id
    token           token唯一标识
    userid          用户id唯一标识
    """

    @pytest.mark.parametrize(('login_phone', 'login_password', 'update_user_phone', 'update_user_password',
                              'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_reset'][
                                 'test_sys_admin_reset_fail'])
    def test_user_reset_fail(self, login_phone, login_password, update_user_phone, update_user_password,
                             except_message, except_status):
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 登录被重置用户，获取该用户id"):
            update_user_id = getter.user_login(phone=update_user_phone, password=update_user_password,
                                               rememberMe=False).json()['data']['sysAdmin']['id']

        with allure.step("step3: 步骤3 ==>> 重置用户密码"):
            rsp_reset = getter.user_reset(cookies, id=update_user_id, token=token, userid=userId)

        assert rsp_reset.status_code == 200
        assert rsp_reset.json()['data'] is None
        assert rsp_reset.json()['message'] == except_message
        assert rsp_reset.json()['status'] == except_status


if __name__ == '__main__':
    pytest.main(['-s', 'test_sys_admin_reset.py'])
