# 接口列表定义
import requests


class User(object):

    def __init__(self, url, headers, date=None, json=None, **kwargs):
        self.url = url
        self.headers = headers
        self.date = date
        self.json = json
        self.list = kwargs

    def user_login(self):
        return requests.post(url=self.url+'/admin/sysadmin/login', headers=self.headers, json=self.json)

user = User