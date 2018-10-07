import sys
sys.path.append('')
import time
from selenium import webdriver
import random
from PIL import Image
from moco_selenium.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
class RegisterFuntion(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)
    #获取driver打开URL
    def get_driver(self, url, i):
        if i == 0:
            driver = webdriver.Chrome()
        else:
            # driver = webdriver.Ie()
            # time.sleep(5)
            pass
        driver.get(url)
        driver.maximize_window()
        return driver
    # 输入用户信息

    def get_usr_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        return find_element.get_element(key)

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('0123456789abcdefghijklmnABCDEFGHIJKLUM', 8))
        return user_info

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 解析图片，获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "75137", "0d0a8091cf03459bbd9d0badc3021af8")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    def run_main(self):
        user_name_info = self.get_range_user()
        get_email = user_name_info + "@qq.com"
        get_name = user_name_info
        file_name = r"C:\Users\Administrator\PycharmProjects\moco\moco_selenium\image\test02.png"
        code_text = self.code_online(file_name)
        self.get_usr_info('user_email', get_email)
        self.get_usr_info('user_name', get_name)
        self.get_usr_info('password', '123456')
        self.get_usr_info('code_text',code_text )
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None :
            print("注册成功")
        else:
            self.driver.save_screenshot("C:/Users/Administrator/PycharmProjects/moco/moco_selenium/image/code_error.png")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':

    for i in range(2):
        register_funtion = RegisterFuntion("http://www.5itest.cn/register?goto=/", i)
        register_funtion.run_main()



