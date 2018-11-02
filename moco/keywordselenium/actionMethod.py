# encoding: utf-8
import time

from selenium import webdriver

from base.find_element import FindElement

class ActionMethod:

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application"
                                       "\\chromedriver.exe")
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_key(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击
    def click_element(self, key):
        element = self.get_element(key)
        element.click()

    # 等待
    def sleep_time(self, times):
        time.sleep(times)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):

        result = self.driver.title
        return result
