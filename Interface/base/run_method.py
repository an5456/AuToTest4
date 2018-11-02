import requests
import json


class RunMethod:
    def post_main(self, url, data, cookies=None):
        res = None
        if cookies is not None:
            res = requests.post(url=url, json=data, cookies=cookies, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)

        return res.json()

    def get_main(self, url, data=None, cookies=None):
        res = None
        if cookies is not None:
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)

        return res.json()

    def run_main(self, method, url, data=None, cookies=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, cookies)
        else:
            res = self.get_main(url, data)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

