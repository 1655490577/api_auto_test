import requests
from config.config import server_ip


class User(object):

    def __init__(self):
        self.ip = server_ip()
        self.headers = {'Content-Type': 'application/json'}

    def user_login(self, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/login', json=kwargs, headers=self.headers)

    def user_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/update', json=kwargs, headers=self.headers, cookies=cookies)

    def user_save(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/save', json=kwargs, headers=self.headers, cookies=cookies)

    def user_reset(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/reset', json=kwargs, headers=self.headers, cookies=cookies)

    def user_logout(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/logout', json=kwargs, headers=self.headers, cookies=cookies)

    def user_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/list', json=kwargs, headers=self.headers, cookies=cookies)

    def user_delete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/delete', json=kwargs, headers=self.headers, cookies=cookies)


user = User()
