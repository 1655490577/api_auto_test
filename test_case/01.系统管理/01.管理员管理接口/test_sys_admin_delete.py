from api.api_get_data import getter
import pytest


class TestSysAdminDelete(object):
    """
    参数列表
    "id": "string",
    "token": "string",
    "userid": "string"
    """

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_delete_success(self):
        pass

    def test_delete_fail(self):
        pass


if __name__ == '__main__':
    pytest.main('-s', 'test_sys_admin_delete.py')
