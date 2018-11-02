import requests
from jsonpath_rw import jsonpath, parse


class Resquest:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def get_file(self):
        res = requests.get(self.url).json()
        print(res)
        json_exe = parse(self.key)
        model = json_exe.find(res)
        return [math.value for math in model][0]
        #print(model)


if __name__ == '__main__':
    url = "http://mam.netease.com/api/v1/getconfig"
    key = "data.isconnect"
    rew = Resquest(url, key)
    print(rew.get_file())
