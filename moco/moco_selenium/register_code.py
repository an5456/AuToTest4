import time
from selenium import webdriver
import random
from PIL import Image
from moco_selenium.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
file_name = "C:/Users/Administrator/PycharmProjects/moco/moco_selenium/image/test02.png"


# 初始化浏览器
def driver_init():
    driver.get("http://www.5itest.cn/register?goto=/")
    driver.maximize_window()
    time.sleep(5)


# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('0123456789abcdefghijklmnABCDEFGHIJKLUM', 8))
    return user_info


# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)


# 解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "75137", "0d0a8091cf03459bbd9d0badc3021af8")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text


# 运行主程序
def run_main():
    user_name_info = get_range_user()
    get_email = user_name_info + "@qq.com"
    get_name = user_name_info
    driver_init()
    get_element("register_email").send_keys(get_email)
    get_element("register_nickname").send_keys(get_name)
    get_element("register_password").send_keys("123456")
    get_code_image(file_name)
    text = code_online(file_name)
    time.sleep(5)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()


run_main()
