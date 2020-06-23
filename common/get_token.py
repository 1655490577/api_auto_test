from api.api_public_method import login


def get_login_token(phone, password, rememberMe):
    r = login(phone=phone, password=password, rememberMe=rememberMe)
    return r.json()['data']['token'], r.cookies


system_token, system_cookies = get_login_token("13168775546", "123456", True)
company_token, company_cookies = get_login_token("13168775547", "123456", True)
department_token, department_cookies = get_login_token("13168775548", "123456", True)
group_token, group_cookies = get_login_token("13168775549", "123456", True)