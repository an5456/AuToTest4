from base.run_method import RunMethod
from data.get_data import GetData
from util.operation_excel import OperationExcel
from jsonpath_rw import jsonpath, parse
import json

from util.operation_json import OperationJson


class DepnedentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.operation = OperationExcel()
        self.data = GetData()

    # 根据case_id,获取整行的数据
    def get_case_line_data(self):
        self.operation.get_rows_data(self.case_id)

    # 执行依赖测试，获取结果
    def run_depnedent(self):
        run_method = RunMethod()
        row_num = self.operation.get_rows_num(self.case_id)  # 获取行号
        request_data = self.data.get_json_data(row_num)  # 获取请求数据
        method = self.data.get_request_method(row_num)  # 获取请求方法
        url = self.data.get_request_url(row_num)
        cookies = {"SESSION": "bdbd5d09-29c5-40f8-aa16-cae274c1c6cd"}
        cookie = self.data.get_cookies_value(row_num)
        if cookie == 'yes':
            get_cookie = OperationJson('../dataconfig/cookie.json')
            cooki = get_cookie.get_data('SESSION')
            cookies = {
                "SESSION": cooki
            }
            res = run_method.run_main(method, url, request_data, cookies)  # 发送请求
        else:
            res = run_method.run_main(method, url, request_data)
        return json.loads(res)

    # 根据依赖的key去获取，依赖测试case的响应，得到对应的字段并且返回
    def get_data_for_key(self, row):
        depent_data = self.data.get_depentent_key(row)  # 获取匹配的依赖数据
        response_data = self.run_depnedent()
        json_exe = parse(depent_data)  # 以depent_data去匹配字段
        madel = json_exe.find(response_data)
        return [math.value for math in madel]


if __name__ == '__main__':
    depent = DepnedentData("Imooc-01")
    print(depent.run_depnedent())
