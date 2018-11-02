# from jsonpath_rw import jsonpath,parse
# jsonpath_expr = parse('foo[-1][age]')
# data = {'foo': [{'baz': 'news', 'name': 'liming'}, {'baz': 'music'}, {'age': '123'}]}
# print([match.value for match in jsonpath_expr.find(data)])
# foo = [match.value for match in jsonpath_expr.find(data)][0]
# # name = [match.value for match in jsonpath_expr.find(data)][1]
# print("foo----->:"+foo)
# # print("name---->:"+name)
# # import requests
# #
# #
# #
# # import json
# # import urllib
# # url = "http://192.168.2.153/planapi/api/quotation/detailInfo"
# # data = {"ticketno":"QT20181025001058"}
# #
# # headers = {"Content-Type": "application/json;charset=UTF-8"}
# # res = requests.post(url=url, json=data, headers=headers).json()
# # ad = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
# # print(ad)
import requests
import json
# url = "http://192.168.2.153/planapi/api/excel/equiryOrder/new/export"
# f = {
#     "companyId": (None, "enquiry (1).xls"),
#     "myFile": ("enquiry (1).xls", open("enquiry (1).xls", "rb"), "application/vnd.ms-excel")
# }
# r = requests.post(url=url, files=f).json()
# s = json.dumps(r, ensure_ascii=False, sort_keys=True, indent=2)
# print(s)
#url = "http://sso.csjscm.com/login?service=http://scm.csjmro.com/csj_login"
url1 = "http://scm.csjmro.com/csj_login"
res =requests.get(url=url1)
print(res.headers)
jssid =res.headers['Set-Cookie'].split(";")[0].split("=")[1]
cookies ={
        "JSESSIONID": jssid
}
print(jssid)
ad =requests.get("http://sso.csjscm.com/login?service=http://scm.csjmro.com/csj_login")
print(ad.headers)
# print(u'获取Headers:', res.headers)
# print(u'响应内容:', res.text)