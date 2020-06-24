import requests
import pytest
from common.get_token_cookies import get_login_token_cookies


def data_preparation():
    token, cookies = get_login_token_cookies("admin", "admin", True)

