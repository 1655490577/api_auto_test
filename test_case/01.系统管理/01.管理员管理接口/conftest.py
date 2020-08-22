import pytest
from api.api_get_data import getter
from common.mysql_operate import db


@pytest.fixture(scope='class')
def add_user():
    token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
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
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试组用户", password="123456789", phone="13168775547",
                     proSelected=["272459479822368768"], projects="272459479822368768",
                     roleId=groupRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName,
                     groupCode=groupCode, groupId=groupId, groupName=groupName)
    for i in range(1, 5):
        getter.user_save(cookies, dataType=1, isAdmin=1, name=f"测试系统管理员0{i}",
                         password="123456789", phone=str(13100000000+i),
                         proSelected=[], roleId=sysRoleId, state=1, token=token, userid=userId)  # 添加测试系统管理员01-04

        getter.user_save(cookies, dataType=1, isAdmin=2, name=f"测试公司管理员0{i}",
                         password="123456789", phone=str(13100000004+i),
                         proSelected=["272459479822368768"], projects="272459479822368768",
                         roleId=companyRoleId, state=1, token=token, userid=userId,
                         dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试公司管理员01-04

        getter.user_save(cookies, dataType=1, isAdmin=2, name=f"测试部门用户0{i}",
                         password="123456789", phone=str(13100000008+i),
                         proSelected=["272459479822368768"], projects="272459479822368768",
                         roleId=branchRoleId, state=1, token=token, userid=userId,
                         branchCode=branchCode, branchId=branchId, branchName=branchName,
                         dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试部门用户01-04

        getter.user_save(cookies, dataType=1, isAdmin=2, name=f"测试组用户0{i}",
                         password="123456789", phone=str(13100000012+i),
                         proSelected=["272459479822368768"], projects="272459479822368768",
                         roleId=groupRoleId, state=1, token=token, userid=userId,
                         branchCode=branchCode, branchId=branchId, branchName=branchName,
                         dicCode=dicCode, dicId=dicId, dicName=dicName,
                         groupCode=groupCode, groupId=groupId, groupName=groupName)  # 添加测试组用户01-04

    yield
    token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
    id_data = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")
    for i, val in enumerate(id_data):
        getter.user_delete(cookies, id=val['id'], token=token, userId=userId)
