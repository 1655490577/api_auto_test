import pytest
import os
from common.get_data_object import data


BASE_PATH = os.path.dirname(os.path.abspath(__file__))  # 获取当前项目的绝对路径


def get_data(yaml_file_name):
    """
    拼接读取的yaml文件的绝对路径
    """
    try:
        data_file_path = os.path.join(BASE_PATH, "Data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))    # 读取文件失败时，跳过该用例
    else:
        return yaml_data


api_date = get_data('api_data.yml')
