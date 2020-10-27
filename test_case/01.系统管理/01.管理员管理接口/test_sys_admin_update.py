from api.api_get_data import getter
from common.mysql_operate import db
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_test_role')
@pytest.mark.usefixtures("add_dictionaries_company")
class TestSysAdminUpdate(object):
    """
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
      "id": "被修改用户id"
      "isAdmin": "是否管理员(1:管理员2:用户账号)",
      "name": "用户名",
      "password": "密码",
      "phone": "手机",
      "projects": "项目集合",
      "roleId": "角色id",
      "token": "token唯一标识",
      "userid": "用户id唯一标识"
    """
    @pytest.mark.parametrize(('login_phone', 'login_password', 'update_phone', 'update_password',
                              'except_message_update', 'except_status_update',
                              'except_message_login', 'except_status_login'),
                             getter.load_yaml('SystemManagementData.yml')['test_sys_admin_save']['test_user_save_sys'])
    def test_user_update_sys_isAdmin(self, login_phone, login_password, update_phone, update_password,
                                     except_message_update, except_status_update,
                                     except_message_login, except_status_login):
        with allure.step("step1: 步骤1 ==>> 登录并获取操作人token,userid,cookies,被修改人id"):
            token, userid, cookies = getter.get_login_token_cookies(login_phone, login_password)
            update_user_id = getter.user_login(phone=update_phone, password=update_password,
                                               rememberMe=False).json()['data']['sysAdmin']['id']
        with allure.step("step2: 步骤2 ==>> 查询必要信息公司roleId,公司id，公司name，公司code，项目id"):
            roleData = db.select_db("SELECT id FROM sys_role WHERE name LIKE '测试%'")
            dictionaryData = db.select_db(
                "SELECT id,name,code FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `code` ")
            projectId = db.select_db("SELECT id FROM tb_construction_project WHERE `name`='预置项目'")[0]['id']
            companyRoleId = roleData[1]['id']
            companyId = dictionaryData[0]['id']
            companyName = dictionaryData[0]['name']
            companyCode = dictionaryData[0]['code']
        with allure.step("step3: 步骤3 ==>> 修改系统管理员为公司管理员"):
            rsp_update = getter.user_update(cookies, )


if __name__ == '__main__':
    pytest.main(['-s', 'test_sys_admin_update.py'])
