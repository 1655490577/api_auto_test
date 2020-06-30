from api.api_public_method import user
from common.get_token_cookies import get_login_token_cookies


def add_test_user():
    """
    area	        string      区
    areaCode	    string      区编码
    branchCode	    string      部门编码
    branchId	    string      部门id
    branchName	    string      部门名称
    city	        string      市
    cityCode	    string      市编码
    dataCodes	    string      数据权限集合 0101,0102
    dataType	    string      数据权限类型(1:自己2:分配)
    dicCode	        string      机构编码
    dicId	        string      机构id
    dicName	        string      机构名称
    groupCode	    string      组code
    groupId	        string      组id
    groupName	    string      组名称
    isAdmin*	    string      是否管理员(1:管理员2:用户账号)
    name*	        string      账号
    password*	    string      密码
    phone*	        string      手机
    province	    string      省
    provinceCode	string      省编码
    roleId*	        string      角色id
    token*	        string      token唯一标识
    userId*	        string      用户id唯一标识
    """

    token, cookies = get_login_token_cookies("admin", "admin", True)

    user.save(cookies, dataType=1, isAdmin=1, name="测试系统管理员01", password="123456", phone="13168775501",
              roleId="259752668312895488", state=1, token=token, userid="259098505857990656")  # 添加测试系统管理员01

    user.save(cookies, dataType=1, isAdmin=1, name="测试系统管理员02", password="123456", phone="13168775502",
              roleId="259752668312895488", state=1, token=token, userid="259098505857990656")  # 添加测试系统管理员02

    user.save(cookies, dataType=1, isAdmin=2, name="测试公司管理员01", password="123456", phone="13168775503",
              roleId="259821125242978304", state=1, token=token, userid="259098505857990656",
              dicCode="0102", dicId="259718019809280000", dicName="测试公司")  # 添加测试公司管理员01

    user.save(cookies, dataType=1, isAdmin=2, name="测试公司管理员02", password="123456", phone="13168775504",
              roleId="259821125242978304", state=1, token=token, userid="259098505857990656",
              dicCode="0102", dicId="259718019809280000", dicName="测试公司")  # 添加测试公司管理员02

    user.save(cookies, dataType=1, isAdmin=2, name="测试部门用户01", password="123456", phone="13168775505",
              roleId="259720390136299520 ", state=1, token=token, userid="259098505857990656",
              branchCode="010201", branchId="259718102269296640", branchName="工程部01", dicCode="0102",
              dicId="259718019809280000", dicName="测试公司")  # 添加测试部门用户01

    user.save(cookies, dataType=1, isAdmin=2, name="测试部门用户02", password="123456", phone="13168775506",
              roleId="259720390136299520 ", state=1, token=token, userid="259098505857990656",
              branchCode="010201", branchId="259718102269296640", branchName="工程部01", dicCode="0102",
              dicId="259718019809280000", dicName="测试公司")  # 添加测试部门用户02

    user.save(cookies, dataType=1, isAdmin=2, name="测试组用户01", password="123456", phone="13168775507",
              roleId="259720526056914944 ", state=1, token=token, userid="259098505857990656",
              branchCode="010201", branchId="259718102269296640", branchName="工程部01", dicCode="0102",
              dicId="259718019809280000", dicName="测试公司", groupCode="01020101", groupId="259718194518818816",
              groupName="事业组01")  # 添加测试组用户01

    user.save(cookies, dataType=1, isAdmin=2, name="测试组用户02", password="123456", phone="13168775508",
              roleId="259720526056914944 ", state=1, token=token, userid="259098505857990656",
              branchCode="010201", branchId="259718102269296640", branchName="工程部01", dicCode="0102",
              dicId="259718019809280000", dicName="测试公司", groupCode="01020101", groupId="259718194518818816",
              groupName="事业组01")  # 添加测试组用户02


if __name__ == '__main__':
    add_test_user()
