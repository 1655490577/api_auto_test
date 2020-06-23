import requests
from api.api_public_method import login
import pytest


def get_login_token(phone, password, rememberMe):
    r = login(phone=phone, password=password, rememberMe=rememberMe)
    return r.json()['data']['token']


system_token = get_login_token("13168775546", "123456", True)
company_token = get_login_token("13168775547", "123456", True)
department_token = get_login_token("13168775548", "123456", True)
group_token = get_login_token("13168775549", "123456", True)
