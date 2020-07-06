import configparser
from common.read_data import data
import os

file = 'config.ini'

con = configparser.ConfigParser()

con.read(file, encoding='utf-8')

section = con.sections()

item = dict(con.items('URL'))

# a = con.get('URL', 'test')
# b = con.getint('URL', 'port')
c = con.options('mysql')
d = con.items('mysql')
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
a = data.load_ini(file_path)
print(a["URL"])
