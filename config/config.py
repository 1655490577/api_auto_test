# 配置文件


def server_ip():
    """
    设置服务器ip地址
    server_ip_outside：str  外网地址
    server_ip_inside：str  内网地址
    :return:
    """
    server_ip_outside = 'http://api.supervisor.dev.hbyrzx.top/supervisor'
    server_ip_inside = 'http://192.168.30.11:10060/supervisor'
    test = 'http://192.168.30.11:10063/supervisor'
    return server_ip_inside


def mysql_setting():
    """
    数据库连接配置
    host 服务器ip地址
    user 数据库登录名
    password 登录密码
    database 要使用的数据库
    autocommit 防止事物执行阻塞，默认为false
    """
    test = {"host": "192.168.30.11",
            "user": "root",
            "password": "Yr!@#1230.",
            "database": "supervisor-test",
            "autocommit": True}
    other = {"host": "192.168.30.11",
             "user": "root",
             "password": "Yr!@#1230.",
             "database": "supervisor",
             "autocommit": True}
    return test
