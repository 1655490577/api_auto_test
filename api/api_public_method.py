import requests
from config.config import server_ip


def login(**kwargs):
    """
    登录接口
    """
    url = server_ip() + '/admin/sysadmin/login'
    headers = {'Content-Type': 'application/json'}
    jsons = kwargs
    r = requests.post(url=url, json=jsons, headers=headers)
    return r


def change_password(cookies, **kwargs):
    """
    修改管理员/修改密码
    """
    url = server_ip() + '/admin/sysadmin/update'
    headers = {'Content-Type': 'application/json'}
    cookies = cookies
    jsons = kwargs
    r = requests.post(url=url, json=jsons, headers=headers, cookies=cookies)
    return r


def add_user(cookies, **kwargs):
    """
    新增用户
    """
    url = server_ip() + '/admin/sysadmin/save'
    headers = {'Content-Type': 'application/json'}
    cookies = cookies
    jsons = kwargs
    r = requests.post(url=url, json=jsons, headers=headers, cookies=cookies)
    return r
