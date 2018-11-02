import requests
import json

from util.operation_json import OperationJson


url = "http://m.imooc.com/passport/user/login"
data = {"username": "17729597958",
        "password": "andong527011764",
        "verify": "",
        "referer": "http://m.imooc.com"
        }
res = requests.post(url, data)
af = res.headers
print(af)
# x = requests.structures.CaseInsensitiveDict(af)
# js = dict(x)
# print(js)
# response_url = res['data']['url'][0]
# print(response_url)
# request_url = response_url+"&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
#res1 = requests.get(request_url).cookies
#res2 = requests.utils.dict_from_cookiejar(res1)
#res3 = requests.utils.check_header_validity()
# op_json = OperationJson()
# op_json.write_data(res1)
#print(res1.headers)
# ad = get_headers(res)
# print(ad)
# ab = get_cookies(res1)
# print(ab)