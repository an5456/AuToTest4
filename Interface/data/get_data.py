import data.data_config


from util.operation_excel import OperationExcel
from util.operation_json import OperationJson


class GetData:
    def __init__(self):
        self.operation = OperationExcel()

    # 获取Excel行数，即case的个数
    def get_case_lines(self):
        return self.operation.get_lines()

    # 获取case名称
    def get_case_name(self, row):
        col = int(data.data_config.get_name())
        case_name = self.operation.get_cell_value(row, col)
        if case_name is not None:
            return case_name
        else:
            return None

    # 获取是执行
    def get_is_run(self, row):
        flag = None
        col = int(data.data_config.get_run())
        run_if = self.operation.get_cell_value(row, col)
        if run_if == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带cookies
    def get_cookies_value(self, row):
        col = int(data.data_config.get_cookies())
        header = self.operation.get_cell_value(row, col)
        if header is not None:
            return header
        else:
            return None

    # 获取header的值
    def get_header_value(self, row):
        col =int(data.data_config.get_header_value())
        header_value = self.operation.get_cell_value(row, col)
        return header_value

    # get或post
    def get_request_method(self, row):
        col = int(data.data_config.get_request_way())
        request_mehtod = self.operation.get_cell_value(row, col)
        return request_mehtod

    # 获取url
    def get_request_url(self, row):
        col = int(data.data_config.get_url())
        url = self.operation.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_reauest_data(self, row):
        col = int(data.data_config.get_request_data())
        request_data = self.operation.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    # 通过关键字获取data数据
    def get_json_data(self, row):
        operation1 = OperationJson()
        json_data = operation1.get_data(self.get_reauest_data(row))
        return json_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data.data_config.get_expect())
        expect = self.operation.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # execl写入数据
    def write_result(self, row, value):
        col = int(data.data_config.get_result())
        self.operation.write_data(row, col, value)

    # 获取依赖数据
    def get_depentent_key(self, row):
        col = int(data.data_config.get_depend_data())
        depend_key = self.operation.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:

            return depend_key

    # 判断是否有case依赖
    def case_id(self, row):
        col = int(data.data_config.get_depend_id())
        depent_case_id = self.operation.get_cell_value(row, col)
        if depent_case_id == '':
            return None
        else:
            return depent_case_id

    # 获取数据依赖字段
    def get_depnet_file(self, row):
        col = int(data.data_config.get_depend_file())
        depent_file = self.operation.get_cell_value(row, col)
        if depent_file == '':
            return None
        else:
            return depent_file
