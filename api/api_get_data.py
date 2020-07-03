import os
from common.read_data import data
from api.api_requests import User


class getter(User):
    def __init__(self):
        super().__init__()
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取当前项目的绝对路径

    def get_yaml_data(self, yaml_file_name):
        """
        拼接读取的yaml文件的绝对路径
        """
        try:
            data_file_path = os.path.join(self.BASE_PATH, "data", yaml_file_name)
            yaml_data = data.load_yaml(data_file_path)
        except Exception as ex:
            raise ex
        else:
            return yaml_data

    def get_login_token_cookies(self, phone, password, rememberMe):
        """
        获取用户登录成功后的token和cookies
        """
        r = self.user_login(phone=phone, password=password, rememberMe=rememberMe)
        token, userId, cookies = r.json()['data']['token'], r.json()['data']['sysAdmin']['id'], r.cookies.get_dict()
        return token, userId, cookies


getEr = getter()
