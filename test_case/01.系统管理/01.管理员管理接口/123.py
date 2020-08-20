# from faker import Faker
#
# faker = Faker(locale='zh_CN')
# a = faker.name()
# print(a)
# b = faker.phone_number()
# print(b)
# {
#   "name": "string",
#   "pageNum": "string",
#   "pageSize": "string",
#   "projectids": "string",
#   "token": "string",
#   "userid": "string"
# }
from common.mysql_operate import db

a = db.select_db("SELECT id FROM sys_admin WHERE `name` LIKE '测试%' ORDER BY phone")
print(a[1]['id'])



