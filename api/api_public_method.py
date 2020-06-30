import requests
from config.config import server_ip


class User(object):

    def __init__(self):
        self.ip = server_ip()
        self.headers = {'Content-Type': 'application/json'}

    def login(self, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/login', json=kwargs, headers=self.headers)

    def update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/update', json=kwargs, headers=self.headers, cookies=cookies)

    def save(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysadmin/save', json=kwargs, headers=self.headers, cookies=cookies)


user = User()
