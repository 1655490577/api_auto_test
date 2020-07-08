import pytest
from api.api_get_data import getter
from common.mysql_operate import db


@pytest.fixture()
def clear_sysAdmin():
    db.execute_db("DELETE FROM sys_admin WHERE id NOT IN ('259098505857990656','266683435907547136')")
    db.execute_db("DELETE FROM sys_admin_role WHERE admin_id NOT IN ('259098505857990656','266683435907547136')")


def clear_sysRole():
    db.execute_db(
        "DELETE FROM sys_role WHERE id NOT IN ('144596599002103829','263713039419703296','266683343469281280')")
    db.execute_db(
        "DELETE FROM sys_role_menu WHERE role_id NOT IN ('144596599002103829','263713039419703296','266683343469281280')")


def clear_project():
    db.execute_db("TRUNCATE TABLE tb_construction_project")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


def clear_projectBid():
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


def clear_projectBidBasement():
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")


def clear_projectBidBuild():
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")


def clear_projectBidUnit():
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


def clear_tbUnit():
    db.execute_db("TRUNCATE TABLE tb_unit")
    db.execute_db("TRUNCATE TABLE tb_unit_qualification")


def clear_tbContract():
    db.execute_db("TRUNCATE TABLE tb_contract")


def clear_questionBase():
    db.execute_db("TRUNCATE TABLE tb_question_base")
    db.execute_db("TRUNCATE TABLE tb_question_part")


def clear_tbQualityInspectDay():
    db.execute_db("TRUNCATE TABLE tb_quality_inspect_day")
    db.execute_db("TRUNCATE TABLE tb_quality_question_detail")


def clear_tbQualityQuestion():
    db.execute_db("TRUNCATE TABLE tb_quality_question_detail")


def add_test_role():
    # 2.2 新增角色(系统角色)
    getter.role_save(cookies, name="测试系统角色", perms=perm, token=token, userid=userId)
    # 新增角色(公司角色)
    getter.role_save(cookies, dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试公司角色",
                     perms=perm, token=token, userid=userId)
    # 新增角色(部门角色)
    getter.role_save(cookies, branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试部门角色",
                     perms=perm, token=token, userid=userId)
    # 新增角色(子部门角色《组》)
    getter.role_save(cookies, groupCode=groupCode, groupId=groupId, groupName=groupName,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName, name="测试子部门角色",
                     perms=perm, token=token, userid=userId)


def add_user():
    sysRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试系统角色'")[0]['id']
    companyRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试公司角色'")[0]['id']
    branchRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试部门角色'")[0]['id']
    groupRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试子部门角色'")[0]['id']
    # 系统管理员2个
    getter.user_save(cookies, dataType=1, isAdmin=1, name="测试系统管理员01", password="123456", phone="13168775501",
                     roleId=sysRoleId, state=1, token=token, userid=userId)  # 添加测试系统管理员01

    getter.user_save(cookies, dataType=1, isAdmin=1, name="测试系统管理员02", password="123456", phone="13168775502",
                     roleId=sysRoleId, state=1, token=token, userid=userId)  # 添加测试系统管理员02
    # 公司管理员2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试公司管理员01", password="123456", phone="13168775503",
                     roleId=companyRoleId, state=1, token=token, userid=userId,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试公司管理员01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试公司管理员02", password="123456", phone="13168775504",
                     roleId=companyRoleId, state=1, token=token, userid=userId,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试公司管理员02
    # 部门用户2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试部门用户01", password="123456", phone="13168775505",
                     roleId=branchRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试部门用户01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试部门用户02", password="123456", phone="13168775506",
                     roleId=branchRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName)  # 添加测试部门用户02
    # 组用户2个
    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试组用户01", password="123456", phone="13168775507",
                     roleId=groupRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName,
                     groupCode=groupCode, groupId=groupId, groupName=groupName)  # 添加测试组用户01

    getter.user_save(cookies, dataType=1, isAdmin=2, name="测试组用户02", password="123456", phone="13168775508",
                     roleId=groupRoleId, state=1, token=token, userid=userId,
                     branchCode=branchCode, branchId=branchId, branchName=branchName,
                     dicCode=dicCode, dicId=dicId, dicName=dicName,
                     groupCode=groupCode, groupId=groupId, groupName=groupName)  # 添加测试组用户02


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
token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
data = db.select_db("SELECT id FROM sys_menu")
perm = '"' + ":".join([i['id'] for i in data]) + '"'

