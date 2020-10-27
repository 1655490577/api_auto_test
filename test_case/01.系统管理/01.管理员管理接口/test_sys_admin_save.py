from api.api_get_data import getter
from common.mysql_operate import db
import pytest
import allure


@pytest.mark.usefixtures('add_base_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminSave(object):
    """
    参数列表:
      "branchCode": "部门编码",
      "branchId": "部门id",
      "branchName": "部门名称",
      "dataCodes": "数据权限集合 0101,0102",
      "dataType": "数据权限类型(1:自己2:分配)",
      "dicCode": "机构编码(公司)",
      "dicId": "机构id",
      "dicName": "机构名称",
      "groupCode": "组code",
      "groupId": "组id",
      "groupName": "组名称",
      "isAdmin": "是否管理员(1:管理员2:用户账号)",
      "name": "用户名",
      "password": "密码",
      "phone": "手机",
      "projects": "项目集合",
      "roleId": "角色id",
      "token": "token唯一标识",
      "userid": "用户id唯一标识"
    """
    _count = 0

    @pytest.mark.parametrize(('login_phone', 'login_password', 'except_message_save', 'except_status_save',
                              'except_message_login', 'except_status_login'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_save']['test_user_save_sys'])
    def test_user_save_sys(self, login_phone, login_password, except_message_save, except_status_save,
                           except_message_login, except_status_login):
        # 不同账号添加系统用户
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 查询必要信息roleId"):
            roleData = db.select_db("SELECT id FROM sys_role WHERE name LIKE '测试%'")
            sysRoleId = roleData[0]['id']

        with allure.step("step2: 步骤2 ==>> 使用当前登录账号添加系统用户"):
            rsp_save_sys = getter.user_save(cookies, dataType=1, isAdmin=1,
                                            userName=str(13800000000 + TestSysAdminSave._count),
                                            name=f'测试添加系统用户账号{TestSysAdminSave._count}',
                                            phone=str(13800000000 + TestSysAdminSave._count),
                                            password='1', proSelected=[], projects='',
                                            roleId=sysRoleId, state=1, token=token, userid=userId)

        with allure.step("step3: 步骤3 ==>> 使用新增的账号登录系统"):
            rsp_new_user_login = getter.user_login(phone=str(13800000000 + TestSysAdminSave._count),
                                                   password='1', rememberMe=False)
            TestSysAdminSave._count += 1

        assert rsp_save_sys.status_code == 200
        assert rsp_save_sys.json()['data'] is None
        assert rsp_save_sys.json()['message'] == except_message_save
        assert rsp_save_sys.json()['status'] == except_status_save
        assert rsp_new_user_login.status_code == 200
        assert rsp_new_user_login.json()['data'] is not None
        assert rsp_new_user_login.json()['data']['sysAdmin']['dicId'] == ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['branchId'] == ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['groupId'] == ''
        assert rsp_new_user_login.json()['message'] == except_message_login
        assert rsp_new_user_login.json()['status'] == except_status_login

    @pytest.mark.parametrize(('login_phone', 'login_password', 'except_message_save', 'except_status_save',
                              'except_message_login', 'except_status_login'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_save'][
                                 'test_user_save_company'])
    def test_user_save_company(self, login_phone, login_password, except_message_save, except_status_save,
                               except_message_login, except_status_login):
        # 不同账号新增公司用户
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 查询必要信息公司roleId,公司id，公司name，公司code，项目id"):
            roleData = db.select_db("SELECT id FROM sys_role WHERE name LIKE '测试%'")
            dictionaryData = db.select_db(
                "SELECT id,name,code FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `code` ")
            projectId = db.select_db("SELECT id FROM tb_construction_project WHERE `name`='预置项目'")[0]['id']
            companyRoleId = roleData[1]['id']
            companyId = dictionaryData[0]['id']
            companyName = dictionaryData[0]['name']
            companyCode = dictionaryData[0]['code']

        with allure.step("step2: 步骤2 ==>> 使用当前登录账号添加系统用户"):
            rsp_save_sys = getter.user_save(cookies, dataType=1, isAdmin=2,
                                            userName=str(13800000000 + TestSysAdminSave._count),
                                            name=f'测试添加系统用户账号{TestSysAdminSave._count}',
                                            phone=str(13800000000 + TestSysAdminSave._count),
                                            password='1', proSelected=[projectId], projects=projectId,
                                            roleId=companyRoleId, state=1, token=token, userid=userId,
                                            dicCode=companyCode, dicId=companyId, dicName=companyName)

        with allure.step("step3: 步骤3 ==>> 使用新增的账号登录系统"):
            rsp_new_user_login = getter.user_login(phone=str(13800000000 + TestSysAdminSave._count),
                                                   password='1', rememberMe=False)
            TestSysAdminSave._count += 1

        assert rsp_save_sys.status_code == 200
        assert rsp_save_sys.json()['data'] is None
        assert rsp_save_sys.json()['message'] == except_message_save
        assert rsp_save_sys.json()['status'] == except_status_save
        assert rsp_new_user_login.status_code == 200
        assert rsp_new_user_login.json()['data'] is not None
        assert rsp_new_user_login.json()['data']['sysAdmin']['dicId'] != ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['branchId'] == ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['groupId'] == ''
        assert rsp_new_user_login.json()['message'] == except_message_login
        assert rsp_new_user_login.json()['status'] == except_status_login

    @pytest.mark.parametrize(('login_phone', 'login_password', 'except_message_save', 'except_status_save',
                              'except_message_login', 'except_status_login'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_save'][
                                 'test_user_save_branch'])
    def test_user_save_branch(self, login_phone, login_password, except_message_save, except_status_save,
                              except_message_login, except_status_login):
        # 不同账号新增部门用户
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 查询必要信息公司roleId,公司id，公司name，"
                         "公司code，项目id，部门id，部门name，部门code"):
            roleData = db.select_db("SELECT id FROM sys_role WHERE name LIKE '测试%'")
            dictionaryData = db.select_db(
                "SELECT id,name,code FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `code` ")
            projectId = db.select_db("SELECT id FROM tb_construction_project WHERE `name`='预置项目'")[0]['id']
            branchRoleId = roleData[1]['id']
            companyId = dictionaryData[0]['id']
            companyName = dictionaryData[0]['name']
            companyCode = dictionaryData[0]['code']
            branchId = dictionaryData[1]['id']
            branchName = dictionaryData[1]['name']
            branchCode = dictionaryData[1]['code']

        with allure.step("step2: 步骤2 ==>> 使用当前登录账号添加系统用户"):
            rsp_save_sys = getter.user_save(cookies, dataType=1, isAdmin=2,
                                            userName=str(13800000000 + TestSysAdminSave._count),
                                            name=f'测试添加系统用户账号{TestSysAdminSave._count}',
                                            phone=str(13800000000 + TestSysAdminSave._count),
                                            password='1', proSelected=[projectId], projects=projectId,
                                            roleId=branchRoleId, state=1, token=token, userid=userId,
                                            dicCode=companyCode, dicId=companyId, dicName=companyName,
                                            branchId=branchId, branchName=branchName, branchCode=branchCode)

        with allure.step("step3: 步骤3 ==>> 使用新增的账号登录系统"):
            rsp_new_user_login = getter.user_login(phone=str(13800000000 + TestSysAdminSave._count),
                                                   password='1', rememberMe=False)
            TestSysAdminSave._count += 1

        assert rsp_save_sys.status_code == 200
        assert rsp_save_sys.json()['data'] is None
        assert rsp_save_sys.json()['message'] == except_message_save
        assert rsp_save_sys.json()['status'] == except_status_save
        assert rsp_new_user_login.status_code == 200
        assert rsp_new_user_login.json()['data'] is not None
        assert rsp_new_user_login.json()['data']['sysAdmin']['dicId'] != ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['branchId'] != ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['groupId'] == ''
        assert rsp_new_user_login.json()['message'] == except_message_login
        assert rsp_new_user_login.json()['status'] == except_status_login

    @pytest.mark.parametrize(('login_phone', 'login_password', 'except_message_save', 'except_status_save',
                              'except_message_login', 'except_status_login'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_save'][
                                 'test_user_save_branch'])
    def test_user_save_group(self, login_phone, login_password, except_message_save, except_status_save,
                             except_message_login, except_status_login):
        # 不同账号新增组用户
        with allure.step("step1: 步骤1 ==>> 登录并获取token,userid,cookies"):
            token, userId, cookies = getter.get_login_token_cookies(login_phone, login_password)

        with allure.step("step2: 步骤2 ==>> 查询必要信息公司roleId,公司id，公司name，"
                         "公司code，项目id，部门id，部门name，部门code，组id，组name，组code"):
            roleData = db.select_db("SELECT id FROM sys_role WHERE name LIKE '测试%'")
            dictionaryData = db.select_db(
                "SELECT id,name,code FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `code` ")
            projectId = db.select_db("SELECT id FROM tb_construction_project WHERE `name`='预置项目'")[0]['id']
            groupRoleId = roleData[1]['id']
            companyId = dictionaryData[0]['id']
            companyName = dictionaryData[0]['name']
            companyCode = dictionaryData[0]['code']
            branchId = dictionaryData[1]['id']
            branchName = dictionaryData[1]['name']
            branchCode = dictionaryData[1]['code']
            groupId = dictionaryData[2]['id']
            groupName = dictionaryData[2]['name']
            groupCode = dictionaryData[2]['code']

        with allure.step("step2: 步骤2 ==>> 使用当前登录账号添加系统用户"):
            rsp_save_sys = getter.user_save(cookies, dataType=1, isAdmin=2,
                                            userName=str(13800000000 + TestSysAdminSave._count),
                                            name=f'测试添加系统用户账号{TestSysAdminSave._count}',
                                            phone=str(13800000000 + TestSysAdminSave._count),
                                            password='1', proSelected=[projectId], projects=projectId,
                                            roleId=groupRoleId, state=1, token=token, userid=userId,
                                            dicCode=companyCode, dicId=companyId, dicName=companyName,
                                            branchId=branchId, branchName=branchName, branchCode=branchCode,
                                            groupId=groupId, groupName=groupName, groupCode=groupCode)

        with allure.step("step3: 步骤3 ==>> 使用新增的账号登录系统"):
            rsp_new_user_login = getter.user_login(phone=str(13800000000 + TestSysAdminSave._count),
                                                   password='1', rememberMe=False)
            TestSysAdminSave._count += 1

        assert rsp_save_sys.status_code == 200
        assert rsp_save_sys.json()['data'] is None
        assert rsp_save_sys.json()['message'] == except_message_save
        assert rsp_save_sys.json()['status'] == except_status_save
        assert rsp_new_user_login.status_code == 200
        assert rsp_new_user_login.json()['data'] is not None
        assert rsp_new_user_login.json()['data']['sysAdmin']['dicId'] != ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['branchId'] != ''
        assert rsp_new_user_login.json()['data']['sysAdmin']['groupId'] != ''
        assert rsp_new_user_login.json()['message'] == except_message_login
        assert rsp_new_user_login.json()['status'] == except_status_login


if __name__ == '__main__':
    pytest.main(['-s', 'test_sys_admin_save.py'])
