import os

import sys
sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\moco')
import time
import HTMLTestRunner
from selenium import webdriver

from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
from util.read_ini import ReadIni
import ddt
import unittest

exl = ExcelUtil()
data = exl.get_data()


@ddt.ddt
class FirstDateCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        get_element = ReadIni()
        # cls.file_name = "C:/Users/Administrator/PycharmProjects/moco/moco_selenium/image/test001.png"
        # cls.file_name = get_element.get_value("code_image_url")

    def setUp(self):
        #self.driver = webdriver.Chrome("C:\Program Files (x86)\python\chromedriver.exe")
        self.driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application"
                                       "\\chromedriver.exe")
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for methon_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                #filePath = os.path.join(os.path.dirname(os.getcwd()) + "\\moco\\report\\" + case_name + ".png")
                filePath1 = 'C:\\Users\\Administrator\\PycharmProjects\\moco\\report'
                filePath = filePath1 + '\\' + case_name + '.png'
                self.driver.save_screenshot(filePath)
        self.driver.close()

    # @ddt.data(
    #     ['12', 'advbd12', '1234456', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['@q.com', 'advbd12', '1234456', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['wer@qq.com', 'advbd12', '1234456', 'code', 'user_email_error', '请输入有效的电子邮件地址']
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data

        email_error = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertEquals(email_error, assertText, "case执行失败")


if __name__ == '__main__':
    #filePath = os.path.join(os.path.dirname(os.getcwd()) + "\\moco\\report\\" + "first_case.html")
    filePath = 'C:\\Users\\Administrator\\PycharmProjects\\moco\\report\\first_case.html'
    f = open(filePath, "wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDateCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="UI 自动化测试报告", description=u"这是我们第一个测试报告1", verbosity=2)
    runner.run(suite)
