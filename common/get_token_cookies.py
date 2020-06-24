from api.api_public_method import login


def get_login_token_cookies(phone, password, rememberMe):
    r = login(phone=phone, password=password, rememberMe=rememberMe)
    return r.json()['data']['token'], r.cookies.get_dict()


# system_token, system_cookies = get_login_token(api_date['test_system'][0][3], api_date['test_system'][0][2], True)
# company_token, company_cookies = get_login_token(api_date['test_system'][1][3], api_date['test_system'][1][2], True)
# department_token, department_cookies = get_login_token(api_date['test_system'][2][3], api_date['test_system'][2][2], True)
# group_token, group_cookies = get_login_token(api_date['test_system'][3][3], api_date['test_system'][3][2], True)
