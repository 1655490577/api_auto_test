from api.api_get_data import getter
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminList(object):
    """
    用户列表数据展示测试
    接口参数列表：
    "area"            区
    "areaCode"        区编码
    "branchCode"      部门编码
    "branchId"        部门id
    "branchName"      部门名称
    "city"	          市
    "cityCode"        市编码
    "dicCode"         机构编码
    "dicId"           机构id
    "dicName"         机构名称
    "groupCode"       组code
    "groupId"         组id
    "groupName"       组名称
    "isAdmin"         是否管理员(1:管理员2:用户账号)
    "name"            名称
    "pageNum"         页码
    "pageSize"        每页条数
    "phone"           手机
    "province"        省
    "provinceCode"    省编码
    "token"           token唯一标识
    "userid"          用户id唯一标识
    """

    @pytest.mark.parametrize(('phone', 'password', 'exist_data', 'notExist_data', 'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_list'][
                                 'test_sys_admin_base_list'])
    def test_sys_admin_user_base_list(self, phone, password, exist_data, notExist_data, except_message, except_status):
        #   用户列表基本信息数据查询
        with allure.step("step1: 步骤1 ==>> 登录用户账号，获取对应信息"):
            token, userId, cookies = getter.get_login_token_cookies(phone, password, True)

        with allure.step("step2: 步骤2 ==>> 获取对应列表信息"):
            rsp_base = getter.user_list_nothing(cookies, pageNum=1, pageSize=1000, toKen=token, userid=userId)

        assert rsp_base.status_code == 200
        assert rsp_base.json()['data'] is not None
        if exist_data is not None:
            for i in exist_data:
                assert i in rsp_base.text
        if notExist_data is not None:
            for i in notExist_data:
                assert i not in rsp_base.text
        assert rsp_base.json()['message'] == except_message
        assert rsp_base.json()['status'] == except_status

    @pytest.mark.parametrize(('phone', 'password', 'select_phone', 'exist_data',
                              'notExist_data', 'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_list'][
                                 'test_sys_admin_phone_list'])
    def test_sys_admin_user_phone_list(self, phone, password, select_phone, exist_data,
                                       notExist_data, except_message, except_status):
        #   根据手机号筛选列表数据
        with allure.step("step1: 步骤1 ==>> 登录用户账号，获取对应信息"):
            login_data = getter.user_login(phone=phone, password=password, rememberMe=False)
            dicId = login_data.json()['data']['sysAdmin']['dicId']
            branchId = login_data.json()['data']['sysAdmin']['branchId']
            groupId = login_data.json()['data']['sysAdmin']['groupId']
            token = login_data.json()['data']['token']
            userId = login_data.json()['data']['sysAdmin']['id']
            cookies = login_data.cookies.get_dict()

        with allure.step("step2: 步骤2 ==>> 通过手机号获取对应列表信息"):
            rsp_phone = getter.user_list_nothing(cookies, dicId=dicId, branchId=branchId, groupId=groupId,
                                                 phone=select_phone, pageNum=1, pageSize=1000,
                                                 toKen=token, userid=userId)

        assert rsp_phone.status_code == 200
        assert rsp_phone.json()['data'] is not None
        if exist_data is not None:
            for i in exist_data:
                assert i in rsp_phone.text
        if notExist_data is not None:
            for i in notExist_data:
                assert i not in rsp_phone.text
        assert rsp_phone.json()['message'] == except_message
        assert rsp_phone.json()['status'] == except_status

    @pytest.mark.parametrize(('phone', 'password', 'select_name', 'exist_data',
                              'notExist_data', 'except_message', 'except_status'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_list'][
                                 'test_sys_admin_name_list'])
    def test_sys_admin_user_name_list(self, phone, password, select_name, exist_data,
                                      notExist_data, except_message, except_status):
        #   根据用户名筛选列表数据
        with allure.step("step1: 步骤1 ==>> 登录用户账号，获取对应信息"):
            login_data = getter.user_login(phone=phone, password=password, rememberMe=False)
            dicId = login_data.json()['data']['sysAdmin']['dicId']
            branchId = login_data.json()['data']['sysAdmin']['branchId']
            groupId = login_data.json()['data']['sysAdmin']['groupId']
            token = login_data.json()['data']['token']
            userId = login_data.json()['data']['sysAdmin']['id']
            cookies = login_data.cookies.get_dict()

        with allure.step("step2: 步骤2 ==>> 通过用户名获取对应列表信息"):
            rsp_name = getter.user_list_nothing(cookies, dicId=dicId, branchId=branchId, groupId=groupId,
                                                name=select_name, pageNum=1, pageSize=1000,
                                                toKen=token, userid=userId)
            print(rsp_name.json())

        assert rsp_name.status_code == 200
        assert rsp_name.json()['data'] is not None
        if exist_data is not None:
            for i in exist_data:
                assert i in rsp_name.text
        if notExist_data is not None:
            for i in notExist_data:
                assert i not in rsp_name.text
        assert rsp_name.json()['message'] == except_message
        assert rsp_name.json()['status'] == except_status


if __name__ == '__main__':
    pytest.main(['-s', 'test_sys_admin_list_nothing.py'])
