import configparser
cf = configparser.ConfigParser()
cf.read("C:/Users/Administrator/PycharmProjects/moco/config/localElement.ini")
print(cf.get('RegisterElement', 'user_name'))
