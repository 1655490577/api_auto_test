import requests
import pytest

url = 'http://192.168.30.11:10060/supervisor' + '/admin/sysadmin/login'
headers = {'Content-Type': 'application/json'}
json = {
    "password": "string",
    "phone": "string",
    "rememberMe": True
}


@pytest.mark.parametrize('phone, password', [('admin', 'admin'), ('13168775547', '123456'), ('13168775548', '123456')])
def test_login_001(phone, password):
    """
    参数可以登录成功(管理员账号)
    :param phone: 登录手机号
    :param password: 登录密码
    :return:
    """
    json_date = {
        "password": password,
        "phone": phone,
        "rememberMe": True
    }
    r = requests.post(url=url, json=json_date, headers=headers)
    assert r.status_code == 200
    assert '用户列表', '角色列表' in r.text
    assert '单位列表', '参建单位列表' in r.text


@pytest.mark.parametrize('phone, password', [(' ', ' '), ('admin', '123'), ('13168775547', None)])
def test_login_002(phone, password):
    """
    参数登录失败
    :param phone: 登录手机号
    :param password: 登录密码
    :return:
    """
    json_date = {
        "password": password,
        "phone": phone,
        "rememberMe": True
    }
    r = requests.post(url=url, json=json_date, headers=headers)
    assert r.status_code == 200
    assert r.json()['date'] == 0


if __name__ == '__main__':
    pytest.main()
