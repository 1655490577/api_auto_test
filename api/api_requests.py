import requests
from api.api_base import baseApi


class Requester(baseApi):

    def __init__(self):
        super().__init__()

    def user_login(self, **kwargs):  # 登录
        return requests.post(url=self.ip + '/admin/sysadmin/login', json=kwargs, headers=self.headers)

    def user_update(self, cookies, **kwargs):  # 修改用户
        return requests.post(url=self.ip + '/admin/sysadmin/update', json=kwargs, headers=self.headers, cookies=cookies)

    def user_save(self, cookies, **kwargs):  # 保存用户
        return requests.post(url=self.ip + '/admin/sysadmin/save', json=kwargs, headers=self.headers, cookies=cookies)

    def user_reset(self, cookies, **kwargs):  # 重置密码
        return requests.post(url=self.ip + '/admin/sysadmin/reset', json=kwargs, headers=self.headers, cookies=cookies)

    def user_logout(self, cookies, **kwargs):  # 注销退出
        return requests.post(url=self.ip + '/admin/sysadmin/logout', json=kwargs, headers=self.headers, cookies=cookies)

    def user_list(self, cookies, **kwargs):  # 用户列表
        return requests.post(url=self.ip + '/admin/sysadmin/list', json=kwargs, headers=self.headers, cookies=cookies)

    def user_list_nothing(self, cookies, **kwargs):  # 用户列表
        return requests.post(url=self.ip + '/admin/sysadmin/list/nothing', json=kwargs, headers=self.headers,
                             cookies=cookies)

    def user_delete(self, cookies, **kwargs):  # 删除用户
        return requests.post(url=self.ip + '/admin/sysadmin/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def role_delete(self, cookies, **kwargs):  # 删除角色
        return requests.post(url=self.ip + '/admin/role/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def role_find(self, cookies, **kwargs):  # 查询角色
        return requests.post(url=self.ip + '/admin/role/find', json=kwargs, headers=self.headers, cookies=cookies)

    def role_list(self, cookies, **kwargs):  # 角色列表
        return requests.post(url=self.ip + '/admin/role/list', json=kwargs, headers=self.headers, cookies=cookies)

    def role_save(self, cookies, **kwargs):  # 保存角色
        return requests.post(url=self.ip + '/admin/role/save', json=kwargs, headers=self.headers, cookies=cookies)

    def role_update(self, cookies, **kwargs):  # 修改角色
        return requests.post(url=self.ip + '/admin/role/update', json=kwargs, headers=self.headers, cookies=cookies)

    def menu_delete(self, cookies, **kwargs):  # 删除菜单
        return requests.post(url=self.ip + '/admin/sysmenu/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def menu_list(self, cookies, **kwargs):  # 菜单列表
        return requests.post(url=self.ip + '/admin/sysmenu/list', json=kwargs, headers=self.headers, cookies=cookies)

    def menu_save(self, cookies, **kwargs):  # 保存菜单
        return requests.post(url=self.ip + '/admin/sysmenu/save', json=kwargs, headers=self.headers, cookies=cookies)

    def menu_tree(self, cookies, **kwargs):  # 树形菜单
        return requests.post(url=self.ip + '/admin/sysmenu/tree', json=kwargs, headers=self.headers, cookies=cookies)

    def menu_update(self, cookies, **kwargs):  # 修改菜单
        return requests.post(url=self.ip + '/admin/sysmenu/update', json=kwargs, headers=self.headers, cookies=cookies)

    def checkSystem_delete(self, cookies, **kwargs):  # 检查体系删除
        return requests.post(url=self.ip + '/admin/syscheck/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def checkSystem_list(self, cookies, **kwargs):  # 检查体系列表
        return requests.post(url=self.ip + '/admin/syscheck/list', json=kwargs, headers=self.headers, cookies=cookies)

    def checkSystem_save(self, cookies, **kwargs):  # 检查体系保存
        return requests.post(url=self.ip + '/admin/syscheck/save', json=kwargs, headers=self.headers, cookies=cookies)

    def checkSystem_update(self, cookies, **kwargs):  # 检查体系修改
        return requests.post(url=self.ip + '/admin/syscheck/update', json=kwargs, headers=self.headers, cookies=cookies)

    def sysGroup_delete(self, cookies, **kwargs):  # 组织架构删除
        return requests.post(url=self.ip + '/admin/sysgroup/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def sysGroup_list(self, cookies, **kwargs):  # 组织架构列表
        return requests.post(url=self.ip + '/admin/sysgroup/list', json=kwargs, headers=self.headers, cookies=cookies)

    def sysGroup_save(self, cookies, **kwargs):  # 组织架构保存
        return requests.post(url=self.ip + '/admin/sysgroup/save', json=kwargs, headers=self.headers, cookies=cookies)

    def sysGroup_update(self, cookies, **kwargs):  # 组织架构修改
        return requests.post(url=self.ip + '/admin/sysgroup/update', json=kwargs, headers=self.headers, cookies=cookies)

    def dictionary_delete(self, cookies, **kwargs):  # 字典删除
        return requests.post(url=self.ip + '/admin/sysdictionaries/delete', json=kwargs,
                             headers=self.headers, cookies=cookies)

    def dictionary_list(self, cookies, **kwargs):  # 字典列表
        return requests.post(url=self.ip + '/admin/sysdictionaries/list', json=kwargs,
                             headers=self.headers, cookies=cookies)

    def dictionary_save(self, cookies, **kwargs):  # 字典保存
        return requests.post(url=self.ip + '/admin/sysdictionaries/save', json=kwargs,
                             headers=self.headers, cookies=cookies)

    def dictionary_tree(self, cookies, **kwargs):  # 字典树
        return requests.post(url=self.ip + '/admin/sysdictionaries/tree', json=kwargs,
                             headers=self.headers, cookies=cookies)

    def dictionary_update(self, cookies, **kwargs):  # 字典修改
        return requests.post(url=self.ip + '/admin/sysdictionaries/update', json=kwargs,
                             headers=self.headers, cookies=cookies)

    def unit_detail(self, cookies, **kwargs):  # 单位
        return requests.post(url=self.ip + '/unit/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def unit_list(self, cookies, **kwargs):  # 单位
        return requests.post(url=self.ip + '/unit/list', json=kwargs, headers=self.headers, cookies=cookies)

    def unit_save(self, cookies, **kwargs):  # 单位
        return requests.post(url=self.ip + '/unit/save', json=kwargs, headers=self.headers, cookies=cookies)

    def unit_update(self, cookies, **kwargs):  # 单位
        return requests.post(url=self.ip + '/unit/update', json=kwargs, headers=self.headers, cookies=cookies)

    def project_list(self, cookies, **kwargs):  # 项目列表
        return requests.post(url=self.ip + '/construction/project/list', json=kwargs, headers=self.headers,
                             cookies=cookies)


user = Requester()
