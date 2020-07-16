import pytest
from api.api_get_data import getter
from common.mysql_operate import db


@pytest.fixture(scope="class")
def clear_sysAdmin():
    # 清除用户表及用户关联表
    db.execute_db("DELETE FROM sys_admin WHERE id != '259098505857990656'")
    db.execute_db("DELETE FROM sys_admin_role WHERE admin_id != '259098505857990656'")


@pytest.fixture(scope="class")
def clear_sysRole():
    # 清除角色表及角色菜单关联表
    db.execute_db(
        "DELETE FROM sys_role WHERE id NOT IN ('144596599002103829','263713039419703296')")
    db.execute_db(
        "DELETE FROM sys_role_menu WHERE role_id NOT IN ('144596599002103829','263713039419703296')")


@pytest.fixture()
def clear_project():
    # 清除项目信息
    db.execute_db("TRUNCATE TABLE tb_construction_project")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


@pytest.fixture()
def clear_projectBid():
    # 清除标段信息
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


@pytest.fixture()
def clear_projectBidBasement():
    # 清除地下室区块信息
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_basement")


@pytest.fixture()
def clear_projectBidBuild():
    # 清除楼栋信息
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_build")


@pytest.fixture()
def clear_projectBidUnit():
    # 清除参建单位信息
    db.execute_db("TRUNCATE TABLE tb_construction_project_bid_unit")


@pytest.fixture()
def clear_tbUnit():
    # 清除单位信息
    db.execute_db("TRUNCATE TABLE tb_unit")
    db.execute_db("TRUNCATE TABLE tb_unit_qualification")


@pytest.fixture()
def clear_tbContract():
    # 清除合同信息
    db.execute_db("TRUNCATE TABLE tb_contract")


@pytest.fixture()
def clear_questionBase():
    # 清除问题库问题信息
    db.execute_db("TRUNCATE TABLE tb_question_base")
    db.execute_db("TRUNCATE TABLE tb_question_part")


@pytest.fixture()
def clear_tbQualityInspectDay():
    # 清除质量日检信息
    db.execute_db("TRUNCATE TABLE tb_quality_inspect_day")
    db.execute_db("TRUNCATE TABLE tb_quality_question_detail")


@pytest.fixture()
def clear_tbQualityQuestion():
    # 清除质量验收信息
    db.execute_db("TRUNCATE TABLE tb_quality_base_beton")
    db.execute_db("TRUNCATE TABLE tb_quality_earth_receipt")
    db.execute_db("TRUNCATE TABLE tb_quality_eartht_backfill")
    db.execute_db("TRUNCATE TABLE tb_quality_public")
    db.execute_db("TRUNCATE TABLE tb_quality_question_detail")
    db.execute_db("TRUNCATE TABLE tb_quality_rebar_install")
    db.execute_db("TRUNCATE TABLE tb_quality_table_main")
    db.execute_db("TRUNCATE TABLE tb_quality_wall_column")
    db.execute_db("TRUNCATE TABLE tb_quality_wall_pouring")


@pytest.fixture()
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


@pytest.fixture()
def add_user():
    # 查询新增好的各角色id
    sysRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试系统角色'")[0]['id']
    companyRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试公司角色'")[0]['id']
    branchRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试部门角色'")[0]['id']
    groupRoleId = db.select_db("SELECT id FROM sys_role WHERE `name` = '测试子部门角色'")[0]['id']
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


def login_user_write_data():
    sys01_req = getter.user_login(phone="13168775501", password="123456", RememberMe=True)
    sys02_req = getter.user_login(phone="13168775502", password="123456", RememberMe=True)
    company01_req = getter.user_login(phone="13168775503", password="123456", RememberMe=True)
    company02_req = getter.user_login(phone="13168775504", password="123456", RememberMe=True)
    branch01_req = getter.user_login(phone="13168775505", password="123456", RememberMe=True)
    branch02_req = getter.user_login(phone="13168775506", password="123456", RememberMe=True)
    group01_req = getter.user_login(phone="13168775507", password="123456", RememberMe=True)
    group02_req = getter.user_login(phone="13168775508", password="123456", RememberMe=True)
    user_token_id_cookies = {
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
    user_delete = {
        "delete_success": [("13168775501", "123456", sys02_req.json()['data']['sysAdmin']['id'],
                            "13168775503", "123456"),
                           ("13168775501", "123456", company01_req.json()['data']['sysAdmin']['id'],
                            "13168775503", "123456"),
                           ("13168775501", "123456", branch01_req.json()['data']['sysAdmin']['id'],
                            "13168775503", "123456"),
                           ("13168775501", "123456", group01_req.json()['data']['sysAdmin']['id'],
                            "13168775503", "123456"),
                           ("13168775503", "123456", company02_req.json()['data']['sysAdmin']['id'],
                            "13168775504", "123456")],
        "delete_fail": [("13168775503", "123456", sys02_req.json()['data']['sysAdmin']['id'],
                        "13168775502", "123456")]
    }
    getter.write_data(user_token_id_cookies, 'userTokenUserIdCookies.yml')


# 查询字典内的组织架构信息，获取公司，部门，组用户的id，code，name
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
# 登录admin用户，获取admin用户的token，userId，cookies
token, userId, cookies = getter.get_login_token_cookies("admin", "admin", True)
# 获取数据库所有菜单id
data = db.select_db("SELECT id FROM sys_menu WHERE perms IS NOT NULL")
perm = '"' + ":".join([i['id'] for i in data]) + '"'
