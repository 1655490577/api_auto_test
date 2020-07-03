from config.config import *


class baseApi(object):

    def __init__(self):
        # 基础配置
        self.ip = server_ip()
        self.headers = {'Content-Type': 'application/json'}



