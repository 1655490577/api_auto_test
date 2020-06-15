import yaml

with open('../Date/test.yaml', encoding='utf-8') as f:
    print(yaml.safe_load(f))

# yaml_str = '''
# name: Cactus
# age: 18
# skills:
#   -
#     - Python
#     - 3
#   -
#     - Java
#     - 5
# has_blog: true
# gf: ~
# '''
# print(yaml.safe_load(yaml_str))