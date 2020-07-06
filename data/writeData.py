from common.mysql_operate import db
from api.api_get_data import getter
import yaml
import os


class writeTestData(object):

    def __init__(self):
        try:
            # 查询字典中公司部门及组的相关信息
            self.select_data = db.select_db(
                "SELECT `code`,id,`name` FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `level`")
            self.dicCode = self.select_data[0]['code']
            self.dicId = self.select_data[0]['id']
            self.dicName = self.select_data[0]['name']
            self.branchCode = self.select_data[1]['code']
            self.branchId = self.select_data[1]['id']
            self.branchName = self.select_data[1]['name']
            self.groupCode = self.select_data[2]['code']
            self.groupId = self.select_data[2]['id']
            self.groupName = self.select_data[2]['name']
        except Exception as e:
            print(self.select_data)
            raise e
        # 1.清除所有角色信息以及用户信息
        db.execute_db("DELETE FROM sys_role WHERE id !='144596599002103829' "
                      "AND id !='263713039419703296' AND id !='264171233677934592'")
        db.execute_db("DELETE FROM sys_admin WHERE id !='259098505857990656' AND id !='264171330776072192'")
        # 2.1 admin账号登录，获取token，cookies
        self.token, self.userId, self.cookies = getter.get_login_token_cookies("admin", "admin", True)
        # 通用全权限
        self.perm = "144596599002103809:144596599002103813:144596599002103814:144596599002103815:144596599002103816:" \
                    "149625711110389767:144596599002103817:144596599002103818:144596599002103819:144596599002103820:" \
                    "149625711110389765:144596599002103821:144596599002103822:144596599002103823:144596599002103824:" \
                    "147483859720601600:144596599002103825:144596599002103826:144596599002103827:144596599002103828:" \
                    "147829264618618900:258283468763430951:258283468763430953:258283468763430954:258283468763430955:" \
                    "149625711110389011:258283468763430952:258283468763430956:258283468763430957:258283468763430958:" \
                    "149625711110389000:147829264618620000:147829264618620001:147829264618620002:147829264618620003:" \
                    "147829264618630000:147829264618630001:147829264618630002:147829264618630003:147829264618630004:" \
                    "147829264618640001:147829264618640002:147829264618640003:147829264618640004:147829264618650001:" \
                    "147829264618650002:147829264618650003:147829264618650004:147829264618660001:147829264618660002:" \
                    "147829264618660003:147829264618660004:147829264618670001:147829264618670002:147829264618670003:" \
                    "147829264618670004:149625711110389001:149625711110389002:149625711110389003:149625711110389004:" \
                    "149625711110389005:258661332363317250:258661332363317251:258661332363317252:258661332363317253:" \
                    "258661332363317254:149625711110389006:149625711110389007:149625711110389008:149625711110389009:" \
                    "149625711110389010:258283468763430949:258283468763430950:258660332359122944:258660332363317248:" \
                    "258660332363317249:147829264618640000:147829264618641000:147829264618641100:147829264618641200:" \
                    "147829264618641300:147829264618641400:147829264618641500:263449920340492297:263449920340492298:" \
                    "263449920340492299:263449920340492300:263449920340492301:263449920340492302:263449920340492303:" \
                    "263449920340492304:263449920340492305:147829264618642000:263449920340492288:263449920340492289:" \
                    "263449920340492292:263449920340492293:263449920340492294:263449920340492295:263449920340492296:" \
                    "263449920340492290:263449920340492291"
        # 要生成的数据文件的路径
        self.file_path = os.path.dirname(os.path.dirname(__file__)) + "/data/"

    def add_role(self):
        # 2.2 新增角色(系统角色)
        getter.role_save(self.cookies, name="测试系统角色", perms=self.perm, token=self.token, userid=self.userId)
        # 新增角色(公司角色)
        getter.role_save(self.cookies, dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName, name="测试公司角色",
                         perms=self.perm, token=self.token, userid=self.userId)
        # 新增角色(部门角色)
        getter.role_save(self.cookies, branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName, name="测试部门角色",
                         perms=self.perm, token=self.token, userid=self.userId)
        # 新增角色(子部门角色《组》)
        getter.role_save(self.cookies, groupCode=self.groupCode, groupId=self.groupId, groupName=self.groupName,
                         branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName, name="测试子部门角色",
                         perms=self.perm, token=self.token, userid=self.userId)

    @staticmethod
    def select_role_id():
        sysRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试系统角色'")[0]['id']
        companyRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试公司角色'")[0]['id']
        branchRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试部门角色'")[0]['id']
        groupRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试子部门角色'")[0]['id']
        return sysRoleId, companyRoleId, branchRoleId, groupRoleId

    def add_user(self, sysRoleId, companyRoleId, branchRoleId, groupRoleId):
        # 系统管理员2个
        getter.user_save(self.cookies, dataType=1, isAdmin=1, name="测试系统管理员01", password="123456", phone="13168775501",
                         roleId=sysRoleId, state=1, token=self.token, userid=self.userId)  # 添加测试系统管理员01

        getter.user_save(self.cookies, dataType=1, isAdmin=1, name="测试系统管理员02", password="123456", phone="13168775502",
                         roleId=sysRoleId, state=1, token=self.token, userid=self.userId)  # 添加测试系统管理员02
        # 公司管理员2个
        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试公司管理员01", password="123456", phone="13168775503",
                         roleId=companyRoleId, state=1, token=self.token, userid=self.userId,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName)  # 添加测试公司管理员01

        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试公司管理员02", password="123456", phone="13168775504",
                         roleId=companyRoleId, state=1, token=self.token, userid=self.userId,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName)  # 添加测试公司管理员02
        # 部门用户2个
        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试部门用户01", password="123456", phone="13168775505",
                         roleId=branchRoleId, state=1, token=self.token, userid=self.userId,
                         branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName)  # 添加测试部门用户01

        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试部门用户02", password="123456", phone="13168775506",
                         roleId=branchRoleId, state=1, token=self.token, userid=self.userId,
                         branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName)  # 添加测试部门用户02
        # 组用户2个
        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试组用户01", password="123456", phone="13168775507",
                         roleId=groupRoleId, state=1, token=self.token, userid=self.userId,
                         branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName,
                         groupCode=self.groupCode, groupId=self.groupId, groupName=self.groupName)  # 添加测试组用户01

        getter.user_save(self.cookies, dataType=1, isAdmin=2, name="测试组用户02", password="123456", phone="13168775508",
                         roleId=groupRoleId, state=1, token=self.token, userid=self.userId,
                         branchCode=self.branchCode, branchId=self.branchId, branchName=self.branchName,
                         dicCode=self.dicCode, dicId=self.dicId, dicName=self.dicName,
                         groupCode=self.groupCode, groupId=self.groupId, groupName=self.groupName)  # 添加测试组用户02

    @staticmethod
    def get_login_testData():
        data = db.select_db("SELECT phone FROM sys_admin WHERE phone like '131687755%'ORDER BY phone")
        sysPhone = data[0]['phone']
        companyPhone = data[2]['phone']
        branchPhone = data[4]['phone']
        groupPhone = data[6]['phone']
        login_data = {"login_success": [[sysPhone, "123456", True], [sysPhone, "123456", False],
                                        [companyPhone, "123456", True], [companyPhone, "123456", False],
                                        [branchPhone, "123456", True], [branchPhone, "123456", False],
                                        [groupPhone, "123456", True], [groupPhone, "123456", False]],
                      "login_error_fail": [[sysPhone, "123", True], [companyPhone, "123", True],
                                           [branchPhone, "12", True], [groupPhone, "2142241", True]],
                      "login_null_fail": [[sysPhone, "", True], ["", "123456", True],
                                          [sysPhone, "", True], [companyPhone, "", True],
                                          [branchPhone, "", True], [groupPhone, "", True]],
                      "login_nopassword_fail": [[sysPhone, True]],
                      "login_noRememberMe_fail": [[sysPhone, "123456"]]
                      }
        return login_data

    @staticmethod
    def get_change_password_testData():
        data = db.select_db(
            "SELECT id ,`name`,`password`,phone FROM sys_admin WHERE phone like '131687755%'ORDER BY phone")
        sysId01, sysName01, sysPwd01, sysPhone01 = data[0]['id'], data[0]['name'], "123456", data[0]['phone']
        sysId02, sysName02, sysPwd02, sysPhone02 = data[1]['id'], data[1]['name'], "123456", data[1]['phone']
        companyId01, companyName01, companyPwd01, companyPhone01 = data[2]['id'], data[2]['name'], "123456", data[2][
            'phone']
        companyId02, companyName02, companyPwd02, companyPhone02 = data[3]['id'], data[3]['name'], "123456", data[3][
            'phone']
        branchId01, branchName01, branchPwd01, branchPhone01 = data[4]['id'], data[4]['name'], "123456", data[4][
            'phone']
        branchId02, branchName02, branchPwd02, branchPhone02 = data[5]['id'], data[5]['name'], "123456", data[5][
            'phone']
        groupId01, groupName01, groupPwd01, groupPhone01 = data[6]['id'], data[6]['name'], "123456", data[6]['phone']
        groupId02, groupName02, groupPwd02, groupPhone02 = data[7]['id'], data[7]['name'], "123456", data[7]['phone']
        change_password_Data = {
            "test_change_password_success":
                [[sysId02, sysName02, sysPwd02, sysPhone02, sysPwd02, sysPhone02],
                 [companyId01, companyName01, companyPwd01, companyPhone01, companyPwd01, companyPhone01],
                 [branchId01, branchName01, branchPwd01, branchPhone01, branchPwd01, branchPhone01],
                 [groupId01, groupName01, groupPwd01, groupPhone01, groupPwd01, groupPhone01],
                 [sysId02, sysName02, sysPwd02, sysPhone02, sysPwd01, sysPhone01],
                 [companyId01, companyName01, companyPwd01, companyPhone01, sysPwd01, sysPhone01],
                 [branchId01, branchName01, branchPwd01, branchPhone01, sysPwd01, sysPhone01],
                 [groupId01, groupName01, groupPwd01, groupPhone01, sysPwd01, sysPhone01],
                 [branchId01, branchName01, branchPwd01, branchPhone01, companyPwd01, companyPhone01],
                 [groupId01, groupName01, groupPwd01, groupPhone01, companyPwd01, companyPhone01],
                 [groupId01, groupName01, groupPwd01, groupPhone01, branchPwd01, branchPhone01]],
            "test_change_password_fail":
                [[sysId01, sysName01, sysPwd01, sysPhone01, companyPwd01, companyPhone01],
                 [companyId02, companyName02, companyPwd02, companyPhone02, companyPwd01, companyPhone01],
                 [sysId01, sysName01, sysPwd01, sysPhone01, branchPwd01, branchPhone01],
                 [companyId01, companyName01, companyPwd01, companyPhone01, branchPwd01, branchPhone01],
                 [branchId02, branchName02, branchPwd02, branchPhone02, branchPwd01, branchPhone01],
                 [sysId01, sysName01, sysPwd01, sysPhone01, groupPwd01, groupPhone01],
                 [companyId01, companyName01, companyPwd01, companyPhone01, groupPwd01, groupPhone01],
                 [branchId01, branchName01, branchPwd01, branchPhone01, groupPwd01, groupPhone01],
                 [groupId02, groupName02, groupPwd02, groupPhone02, groupPwd01, groupPhone01]],
            "test_change_password_noLogin":
                [[sysId01, sysName01, sysPwd01, sysPwd01, sysPhone01, sysId01],
                 [groupId01, groupName01, groupPwd01, sysPwd01, sysPhone01, sysId01],
                 [sysId01, sysName01, sysPwd01, groupPwd01, groupPhone01, groupId01]]
        }
        return change_password_Data

    @staticmethod
    def get_user_testData():
        sys01_req = getter.user_login(phone="13168775501", password="123456", RememberMe=True)
        sys02_req = getter.user_login(phone="13168775502", password="123456", RememberMe=True)
        company01_req = getter.user_login(phone="13168775503", password="123456", RememberMe=True)
        company02_req = getter.user_login(phone="13168775504", password="123456", RememberMe=True)
        branch01_req = getter.user_login(phone="13168775505", password="123456", RememberMe=True)
        branch02_req = getter.user_login(phone="13168775506", password="123456", RememberMe=True)
        group01_req = getter.user_login(phone="13168775507", password="123456", RememberMe=True)
        group02_req = getter.user_login(phone="13168775508", password="123456", RememberMe=True)
        user_data = {
            "sys01": {"token": sys01_req.json()['data']['token'],
                      "userId": sys01_req.json()['data']['sysAdmin']['id'],
                      "cookies": sys01_req.cookies.get_dict()},
            "sys02": {"token": sys02_req.json()['data']['token'],
                      "userId": sys02_req.json()['data']['sysAdmin']['id'],
                      "cookies": sys02_req.cookies.get_dict()},
            "company01": {"token": company01_req.json()['data']['token'],
                          "userId": company01_req.json()['data']['sysAdmin']['id'],
                          "cookies": company01_req.cookies.get_dict()},
            "company02": {"token": company02_req.json()['data']['token'],
                          "userId": company02_req.json()['data']['sysAdmin']['id'],
                          "cookies": company02_req.cookies.get_dict()},
            "branch01": {"token": branch01_req.json()['data']['token'],
                         "userId": branch01_req.json()['data']['sysAdmin']['id'],
                         "cookies": branch01_req.cookies.get_dict()},
            "branch02": {"token": branch02_req.json()['data']['token'],
                         "userId": branch02_req.json()['data']['sysAdmin']['id'],
                         "cookies": branch02_req.cookies.get_dict()},
            "group01": {"token": group01_req.json()['data']['token'],
                        "userId": group01_req.json()['data']['sysAdmin']['id'],
                        "cookies": group01_req.cookies.get_dict()},
            "group02": {"token": group02_req.json()['data']['token'],
                        "userId": group02_req.json()['data']['sysAdmin']['id'],
                        "cookies": group02_req.cookies.get_dict()}
        }
        return user_data

    def write_data(self, data, filename):
        with open(self.file_path + filename, 'w+', encoding='utf-8') as f:
            yaml.safe_dump(data, f, allow_unicode=True)


if __name__ == '__main__':
    w = writeTestData()
    w.add_role()
    roleId1, roleId2, roleId3, roleId4 = w.select_role_id()
    w.add_user(roleId1, roleId2, roleId3, roleId4)
    data1 = w.get_login_testData()
    data2 = w.get_change_password_testData()
    data3 = w.get_user_testData()
    w.write_data(data1, 'login_data.yml')
    w.write_data(data2, 'change_password_data.yml')
    w.write_data(data3, 'user_data.yml')
