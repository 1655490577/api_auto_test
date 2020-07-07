from api.api_requests import Requester
from common.read_data import ReadFileData


class get_data(Requester, ReadFileData):
    def __init__(self):
        super().__init__()
        self.BASE_PATH = ReadFileData().BASE_PATH

    def get_login_token_cookies(self, phone, password, rememberMe):
        """
        获取用户登录成功后的token和cookies
        """
        r = self.user_login(phone=phone, password=password, rememberMe=rememberMe)
        token, userId, cookies = r.json()['data']['token'], r.json()['data']['sysAdmin']['id'], r.cookies.get_dict()
        return token, userId, cookies


getter = get_data()
