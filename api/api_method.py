# 接口请求实现
import requests
from config.config import server_ip


def user_login():
    url = server_ip() + '/admin/sysadmin/login'
    headers = {"Content-Type": "application/json"}
