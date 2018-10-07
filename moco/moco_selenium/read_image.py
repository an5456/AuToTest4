import pytesseract
from PIL import Image
import requests

from moco_selenium.ShowapiRequest import ShowapiRequest

# image = Image.open("C:/Users/Administrator/Desktop/icmmo.png")
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4", "75137", "0d0a8091cf03459bbd9d0badc3021af8")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/imooc2.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
