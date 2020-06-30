from api.api_public_method import user


def get_login_token_cookies(phone, password, rememberMe):
    r = user.login(phone=phone, password=password, rememberMe=rememberMe)
    return r.json()['data']['token'], r.cookies.get_dict()
