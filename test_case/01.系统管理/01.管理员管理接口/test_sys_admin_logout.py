from api.api_get_data import getter
import pytest
import allure


@pytest.mark.skip(reason='接口无作用')
class TestSysAdminLogout(object):
    """
    参数列表：
    "token": token唯一标识
    "userid": 用户id唯一标识
    """
    def test_user_logout(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_sys_admin_logout.py'])
