import pytest
from api.api_get_data import getter
from common.mysql_operate import db


@pytest.fixture()
def add_dictionaries_company():
    token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
    getter.sysGroup_save(cookies, name='测试公司', parentid='bc7b99932b23464fa0917b147ab62dc6',
                         token=token, userid=userId)
    branchPid = db.select_db("SELECT id FROM sys_dictionaries WHERE `name`='测试公司'")[0]['id']
    getter.sysGroup_save(cookies, name='测试部门', parentid=branchPid, token=token, userid=userId)
    groupPid = db.select_db("SELECT id FROM sys_dictionaries WHERE `name`='测试部门'")[0]['id']
    getter.sysGroup_save(cookies, name='测试子部门', parentid=groupPid, token=token, userid=userId)
    groupIId = db.select_db("SELECT id FROM sys_dictionaries WHERE `name`='子测试部门'")[0]['id']
    yield
    getter.sysGroup_delete(cookies, id=groupIId, token=token, userid=userId)
    getter.sysGroup_delete(cookies, id=groupPid, token=token, userid=userId)
    getter.sysGroup_delete(cookies, id=branchPid, token=token, userid=userId)


@pytest.fixture()
def add_test_role():
    token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
    rsp = getter.role_find(cookies, id='144596599002103829', token=token, userid=userId)  # 获取所有权限
    a = rsp.json()['data']['sysRoleMenus']
    aList = []
    for i in a:
        aList.append(i['menuId'])
    Perm = '"' + ":".join([i for i in aList]) + '"'
    # 2.2 新增角色(系统角色)
    getter.role_save(cookies, name="测试系统角色", perms=Perm, token=token, userid=userId)
    # 新增角色(公司角色)
    getter.role_save(cookies, dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试公司角色",
                     perms=Perm, token=token, userid=userId)
    # 新增角色(部门角色)
    getter.role_save(cookies, branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试部门角色",
                     perms=Perm, token=token, userid=userId)
    # 新增角色(子部门角色《组》)
    getter.role_save(cookies, groupCode=groupCode, groupId=groupId, groupName=groupName,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试子部门角色",
                     perms=Perm, token=token, userid=userId)
    yield
    getter.role_delete(cookies, id=sysRoleId, token=token, userid=userId)
    getter.role_delete(cookies, id=companyRoleId, token=token, userid=userId)
    getter.role_delete(cookies, id=branchRoleId, token=token, userid=userId)
    getter.role_delete(cookies, id=groupRoleId, token=token, userid=userId)


@pytest.fixture()
def add_user():
    token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
    # 系统管理员2个
    getter.user_save(cookies, dataType=1, isAdmin=1, name="测试系统管理员01", password="123456", phone="13168775501",
                     proSelected=[], roleId=sysRoleId, state=1, token=token, userid=userId)  # 添加测试系统管理员01

    getter.user_save(cookies, dataType=1, isAdmin=1, name="测试系统管理员02", password="123456", phone="13168775502",
                     proSelected=[], roleId=sysRoleId, state=1, token=token, userid=userId)  # 添加测试系统管理员02
    # 公司管理员2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试公司管理员01", password="123456", phone="13168775503",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=companyRoleId, state=1, token=token, userid=userId,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试公司管理员01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试公司管理员02", password="123456", phone="13168775504",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=companyRoleId, state=1, token=token, userid=userId,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试公司管理员02
    # 部门用户2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试部门用户01", password="123456", phone="13168775505",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=branchRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试部门用户01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试部门用户02", password="123456", phone="13168775506",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=branchRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试部门用户02
    # 组用户2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试组用户01", password="123456", phone="13168775507",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=groupRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName,
                     groupCode=groupCode, groupId=groupId, groupName=groupName)  # 添加测试组用户01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试组用户02", password="123456", phone="13168775508",
                     proSelected=["268683583802048512"], projects="268683583802048512",
                     roleId=groupRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName,
                     groupCode=groupCode, groupId=groupId, groupName=groupName)  # 添加测试组用户02
    yield
    getter.user_delete(cookies, token=token, userId=userId01)
    getter.user_delete(cookies, token=token, userId=userId02)
    getter.user_delete(cookies, token=token, userId=userId03)
    getter.user_delete(cookies, token=token, userId=userId04)
    getter.user_delete(cookies, token=token, userId=userId05)
    getter.user_delete(cookies, token=token, userId=userId06)
    getter.user_delete(cookies, token=token, userId=userId07)


# def login_user_write_data():
#     sys01_req = getter.user_login(phone="13168775501", password="123456", RememberMe=True)
#     sys02_req = getter.user_login(phone="13168775502", password="123456", RememberMe=True)
#     company01_req = getter.user_login(phone="13168775503", password="123456", RememberMe=True)
#     company02_req = getter.user_login(phone="13168775504", password="123456", RememberMe=True)
#     branch01_req = getter.user_login(phone="13168775505", password="123456", RememberMe=True)
#     branch02_req = getter.user_login(phone="13168775506", password="123456", RememberMe=True)
#     group01_req = getter.user_login(phone="13168775507", password="123456", RememberMe=True)
#     group02_req = getter.user_login(phone="13168775508", password="123456", RememberMe=True)
#     user_token_id_cookies = {
#         "sys01": {"token": sys01_req.json()['data']['token'],
#                   "userId": sys01_req.json()['data']['sysAdmin']['id'],
#                   "cookies": sys01_req.cookies.get_dict()},
#         "sys02": {"token": sys02_req.json()['data']['token'],
#                   "userId": sys02_req.json()['data']['sysAdmin']['id'],
#                   "cookies": sys02_req.cookies.get_dict()},
#         "company01": {"token": company01_req.json()['data']['token'],
#                       "userId": company01_req.json()['data']['sysAdmin']['id'],
#                       "cookies": company01_req.cookies.get_dict()},
#         "company02": {"token": company02_req.json()['data']['token'],
#                       "userId": company02_req.json()['data']['sysAdmin']['id'],
#                       "cookies": company02_req.cookies.get_dict()},
#         "branch01": {"token": branch01_req.json()['data']['token'],
#                      "userId": branch01_req.json()['data']['sysAdmin']['id'],
#                      "cookies": branch01_req.cookies.get_dict()},
#         "branch02": {"token": branch02_req.json()['data']['token'],
#                      "userId": branch02_req.json()['data']['sysAdmin']['id'],
#                      "cookies": branch02_req.cookies.get_dict()},
#         "group01": {"token": group01_req.json()['data']['token'],
#                     "userId": group01_req.json()['data']['sysAdmin']['id'],
#                     "cookies": group01_req.cookies.get_dict()},
#         "group02": {"token": group02_req.json()['data']['token'],
#                     "userId": group02_req.json()['data']['sysAdmin']['id'],
#                     "cookies": group02_req.cookies.get_dict()}
#     }
#     user_delete = {
#         "delete_success": [("13168775501", "123456", sys02_req.json()['data']['sysAdmin']['id'],
#                             "13168775502", "123456"),
#                            ("13168775501", "123456", sys01_req.json()['data']['sysAdmin']['id'],
#                             "13168775501", "123456"),
#                            ("13168775501", "123456", company01_req.json()['data']['sysAdmin']['id'],
#                             "13168775503", "123456"),
#                            ("13168775501", "123456", branch01_req.json()['data']['sysAdmin']['id'],
#                             "13168775505", "123456"),
#                            ("13168775501", "123456", group01_req.json()['data']['sysAdmin']['id'],
#                             "13168775507", "123456"),
#                            ("13168775503", "123456", branch01_req.json()['data']['sysAdmin']['id'],
#                             "13168775505", "123456"),
#                            ("13168775503", "123456", group01_req.json()['data']['sysAdmin']['id'],
#                             "13168775507", "123456"),
#                            ("13168775505", "123456", group01_req.json()['data']['sysAdmin']['id'],
#                             "13168775507", "123456")],
#         "delete_fail": [("13168775503", "123456", sys02_req.json()['data']['sysAdmin']['id'],
#                         "13168775502", "123456"),
#                         ("13168775503", "123456", company02_req.json()['data']['sysAdmin']['id'],
#                         "13168775504", "123456"),
#                         ("13168775503", "123456", company01_req.json()['data']['sysAdmin']['id'],
#                         "13168775503", "123456"),
#                         ("13168775505", "123456", sys01_req.json()['data']['sysAdmin']['id'],
#                         "13168775501", "123456"),
#                         ("13168775505", "123456", company01_req.json()['data']['sysAdmin']['id'],
#                         "13168775503", "123456"),
#                         ("13168775505", "123456", branch02_req.json()['data']['sysAdmin']['id'],
#                         "13168775506", "123456"),
#                         ("13168775505", "123456", branch01_req.json()['data']['sysAdmin']['id'],
#                         "13168775505", "123456"),
#                         ("13168775507", "123456", sys01_req.json()['data']['sysAdmin']['id'],
#                         "13168775501", "123456"),
#                         ("13168775507", "123456", company01_req.json()['data']['sysAdmin']['id'],
#                         "13168775503", "123456"),
#                         ("13168775507", "123456", branch01_req.json()['data']['sysAdmin']['id'],
#                         "13168775505", "123456"),
#                         ("13168775507", "123456", group01_req.json()['data']['sysAdmin']['id'],
#                         "13168775507", "123456"),
#                         ("13168775507", "123456", group02_req.json()['data']['sysAdmin']['id'],
#                         "13168775508", "123456")]
#     }
#     getter.write_data(user_token_id_cookies, 'userTokenUserIdCookies.yml')
#     getter.write_data(user_delete, 'userDeleteData.yml')


select_data = db.select_db(
    "SELECT `code`,id,`name` FROM sys_dictionaries WHERE `name` LIKE '测试%' ORDER BY `level`")
dicCode = select_data[0]['code']
dicId = select_data[0]['id']
dicName = select_data[0]['name']
branchCode = select_data[1]['code']
branchId = select_data[1]['id']
branchName = select_data[1]['name']
groupCode = select_data[2]['code']
groupId = select_data[2]['id']
groupName = select_data[2]['name']
sysRoleId = db.select_db("SELECT id FROM sys_role WHERE `name`='测试系统角色'")[0]['id']
companyRoleId = db.select_db("SELECT id FROM sys_role WHERE `name`='测试公司角色'")[0]['id']
branchRoleId = db.select_db("SELECT id FROM sys_role WHERE `name`='测试部门角色'")[0]['id']
groupRoleId = db.select_db("SELECT id FROM sys_role WHERE `name`='测试子部门角色'")[0]['id']
userId01 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[0]['id']
userId02 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[1]['id']
userId03 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[2]['id']
userId04 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[3]['id']
userId05 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[4]['id']
userId06 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[5]['id']
userId07 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[6]['id']
userId08 = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")[7]['id']

