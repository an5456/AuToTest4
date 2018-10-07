from datetime import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from moco_selenium.ShowapiRequest import ShowapiRequest
import time
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register?goto=/")
title = EC.title_contains("注册")
locater=(By.CLASS_NAME, "controls")
util = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locater))
print(util)
driver.save_screenshot("D:/imooc3.png")
driver.find_element_by_css_selector("#")
code_element = driver.find_element_by_id("getcode_num")
print(code_element)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im =Image.open("D:/imooc3.png")
img = im.crop((left, top, right, height))
img.save("D:/imooc3.png")




r = ShowapiRequest("http://route.showapi.com/184-4", "75137", "0d0a8091cf03459bbd9d0badc3021af8")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/imooc3.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id("captcha_code").send_keys(text)
time.sleep(5)
driver.close()
# time.sleep(5)
# print(title)
# driver.find_element_by_id("register_email").send_keys("527011764@qq.com")
# user_name_node=driver.find_elements_by_class_name("controls")[1]
# user_name=user_name_node.find_element_by_class_name("form-control")
# user_name.send_keys("andong")
# driver.find_element_by_name("password").send_keys("123456")
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
driver.__getattribute__("value")