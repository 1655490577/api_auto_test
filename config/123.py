import configparser

file = 'config.ini'

con = configparser.ConfigParser()

con.read(file, encoding='utf-8')

section = con.sections()

item = dict(con.items('URL'))

a = con.get('URL', 'test')
b = con.getint('URL', 'port')
c = con.options('mysql')
d = con.items('mysql')

print(c, d)
