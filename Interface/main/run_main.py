import sys

from data.dependent_data import DepnedentData
from log.get_log import UserLog
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
from util.sendEmail import Mailer

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\Interface')
from util.commonUtil import CommonUtile
from base.run_method import RunMethod
from data.get_data import GetData


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.containt = CommonUtile()
        self.email = Mailer()
        self.log = UserLog()
        self.logger = self.log.get_log()

    # 执行的程序
    def go_on_run(self):
        res = None
        pass_conut = []
        fail_conut = []
        rows_conut = self.data.get_case_lines()
        for i in range(1, rows_conut):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_json_data(i)
                case_name = self.data.get_case_name(i)
                cookie = self.data.get_cookies_value(i)
                expect = self.data.get_expect_data(i)
                depent_case = self.data.case_id(i)  # 获取依赖字段的key
                if depent_case is not None:
                    # 获取依赖的key
                    depent_key = self.data.get_depnet_file(i)
                    self.depend_data = DepnedentData(depent_case)
                    # 获取依赖的响应数据
                    depnet_response_data = self.depend_data.get_data_for_key(i)
                    le = len(depent_key.split(">"))  # 切分字符串取大小
                    for y in range(0, le):
                        re = depent_key.split(">")
                        request_data[re[y]] = depnet_response_data[y]  # 循环替换
                if cookie == 'write':
                    # 发送请求
                    res = self.run_method.run_main(method, url, request_data)
                    op_cookies = OperationHeader(res)
                    op_cookies.write_cookie()  # 写入cookies到cookie.json文件中
                elif cookie == 'yes':
                    get_cookie = OperationJson('../dataconfig/cookie.json')
                    cooki = get_cookie.get_data('SESSION')
                    cookies = {
                        "SESSION": cooki
                    }
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)
                if self.containt.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_conut.append(i)
                    self.logger.info("测试通过")
                    self.logger.info("通过响应数据" + res)
                    print("测试通过")
                else:
                    self.logger.info("测试失败")
                    self.logger.info("失败case名称：" + case_name)
                    self.logger.info("失败的行数：" + str(i))
                    self.data.write_result(i, res)
                    fail_conut.append(i)
                    print("测试失败")
                    self.logger.info("url:" + url)
                    self.logger.info("失败请求数据:" + str(request_data))
                    self.logger.info("失败响应数据:" + res)

        # 发送测试报告邮件
        self.email.send_main(pass_conut, fail_conut)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
