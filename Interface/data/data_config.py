class global_var(object):
    # id
    id = '0'

    # 名称
    name = '1'

    # url
    url = '2'

    # 是否执行
    run = '3'

    # 请求方式
    request_way = '4'

    # header（cookies）
    header = '5'

    # 获取header的值
    header_value = '6'

    # 依赖ID
    depend_id = '7'

    # 依赖数据
    depend_data = '8'

    # 依赖数据的字段
    depend_file = '9'

    # 请求数据
    request_data = '10'

    # 预期结果
    expect = '11'

    # 实际结果
    result = '12'


# 获取caseid
def get_id():
    return global_var.id


# 获取名称
def get_name():
    return global_var.name


# 获取url
def get_url():
    return global_var.url


# 获取是否执行
def get_run():
    return global_var.run


# 获取请求方式
def get_request_way():
    return global_var.request_way


# 获取cookies
def get_cookies():
    return global_var.header


# 获取header值
def get_header_value():
    return global_var.header_value


# 获取依赖id
def get_depend_id():
    return global_var.depend_id


# 获取依赖数据
def get_depend_data():
    return global_var.depend_data


# 获取依赖数据的字段
def get_depend_file():
    return global_var.depend_file


# 获取请求数据
def get_request_data():
    return global_var.request_data


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result
