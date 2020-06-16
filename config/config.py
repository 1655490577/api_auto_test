# 配置文件


def server_ip():
    """
    设置服务器ip地址
    server_ip_outside：str  外网地址
    server_ip_inside：str  内网地址
    :return:
    """
    server_ip_outside = 'http://dev-server-supervisor-api/supervisor'
    server_ip_inside = 'http://192.168.30.11:10060/supervisor'
    return server_ip_inside
