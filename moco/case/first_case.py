from selenium import webdriver
import sys
import unittest
import os
import time
import HTMLTestRunner

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\moco')
from business.register_business import RegisterBusiness
from log.get_log import UserLog

from util.read_ini import ReadIni


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        get_element = ReadIni()
        cls.file_name = "C:/Users/Administrator/PycharmProjects/moco/moco_selenium/image/test001.png"
        # cls.file_name = get_element.get_value("code_image_url")
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application"
                                       "\\chromedriver.exe")
        # self.driver = webdriver.Chrome()
        option = webdriver.ChromeOptions()
        option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.logger.info("打开浏览器成功")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for methon_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                # filePath = os.path.join(os.path.dirname(os.getcwd()) + "\\report\\" + case_name + ".png")
                filePath1 = 'C:\\Users\\Administrator\\PycharmProjects\\moco\\report'
                filePath = filePath1 + '\\' + case_name + '.png'
                self.driver.save_screenshot(filePath)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    # 邮箱错误
    def test_login_email_error(self):

        email_error = self.login.login_email_error("andong@qq.com", "user1111", "123456", self.file_name)
        self.assertFalse(email_error, "case执行成功")

    # 用户名错误
    def test_login_username_error(self):
        username_error = self.login.login_username_error("54567@qq.com", "ur", "12345", self.file_name)
        self.assertFalse(username_error, "case执行成功")

    # 密码错误
    def test_login_password_error(self):
        password_erroer = self.login.login_password_error("6789@qq.com", "test123", "11", self.file_name)
        self.assertFalse(password_erroer, "case执行成功")

    # 验证码错误
    def test_longin_code_error(self):
        code_error = self.login.login_code_error("12345@qq.com", "loawang12", "123456", self.file_name)
        self.assertFalse(code_error, "case执行成功")

    # 注册成功
    def test_login_success(self):
        success = self.login.user_base("2345@qq.com", "wanglaosi12", "23456", self.file_name)
        self.assertFalse(success, "case执行了")


if __name__ == '__main__':
    # filePath = os.path.join(os.path.dirname(os.getcwd()) + "\\report\\" + "first_case.html")
    filePath = 'C:\\Users\\Administrator\\PycharmProjects\\moco\\report\\first_case.html'
    f = open(filePath, "wb")
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_email_error"))
    suite.addTest(FirstCase("test_login_username_error"))
    suite.addTest(FirstCase("test_login_password_error"))
    suite.addTest(FirstCase("test_longin_code_error"))
    # suite.addTest(FirstCase("test_login_success"))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="UI 自动化测试报告", description=u"这是我们第一个测试报告", verbosity=2)
    runner.run(suite)
