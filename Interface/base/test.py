import requests

import json,mock



class RunMain:

    # def __init__(self):
    #     self.res = self.run_main()

    def send_get(self, url, data):
        res = requests.get(url=url, data=data,).text
        #return json.dumps(res, indent=2, sort_keys=True)
        #return json.loads(res, strict=False)
        #print(u'HTTP状态码:', res.status_code)
        # print(u'请求的URL:', r.url)
        # print(u'获取Headers:', r.headers)
        # print(u'响应内容:', r.text)
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        # print(res)
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data=None):

        if method == 'GET':
            return self.send_get(url, data)
        else:
            return self.send_post(url, data)


if __name__ == '__main__':
    #url = 'http://127.0.0.1:8000/login/?username=5435fdsaf&password=54325432'
    url = 'http://www.youdao.com'
    # data = {
    #     'password': '1234',
    #     'username': 'dfdf'
    #
    #  }
    run = RunMain()
    #print(run.res)
    print(run.run_main(url, 'GET'))
