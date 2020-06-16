import requests
import pytest
import allure
from conftest import api_date
from config.config import server_ip

url = server_ip() + '/admin/sysadmin/login'
headers = {'Content-Type': 'application/json'}
json = {
    "password": "string",
    "phone": "string",
    "rememberMe": True
}


@allure.suite("测试套件")
@allure.title("登录成功")  # 用例标题自定义
@allure.step("使用不同的正确账号登录系统")  # 测试步骤描述
@allure.feature('测试模块01')  # 对应特性场景
@allure.description('登录成功测试用例')  # 对应用例里面的描述
@allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
@pytest.mark.parametrize('phone, password', api_date["login_success"])
@allure.severity('critical')  # 用例优先级
def test_login_001(phone, password):
    """
    用例描述：
    参数可以登录成功(管理员账号)
    :param phone: 登录手机号
    :param password: 登录密码
    :return:
    """
    json_date = {
        "password": password,
        "phone": phone,
        "rememberMe": True
    }

    r = requests.post(url=url, json=json_date, headers=headers)

    assert r.status_code == 200
    assert r.json()["data"] is not None
    assert r.json()["message"] == "成功"
    assert r.json()["status"] == "0"


@allure.suite("测试套件2")
@allure.title("登录失败")  # 用例标题自定义
@allure.step("使用不同的错误账号登录系统")  # 测试步骤描述
@allure.feature('测试模块02')   # 对应特性场景
@allure.description('登录失败测试用例')  # 对应用例里面的描述
@allure.testcase('http://www.baidu.com', name='点击我跳转百度')
@pytest.mark.parametrize('phone, password', api_date["login_fail"])
@allure.severity('blocker')
def test_login_002(phone, password):
    """
    用例描述：
    参数登录失败
    :param phone: 登录手机号
    :param password: 登录密码
    :return:
    """
    json_date = {
        "password": password,
        "phone": phone,
        "rememberMe": True
    }
    r = requests.post(url=url, json=json_date, headers=headers)
    assert r.status_code == 200
    assert r.json()['data'] is None
    assert r.json()["message"] == "手机号或密码不存在" or "password,不能为空" or "phone,不能为空"
    assert r.json()["status"] == "100005" or "100001"


if __name__ == '__main__':
    pytest.main()
