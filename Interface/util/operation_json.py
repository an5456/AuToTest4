import json


class OperationJson(object):
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../dataconfig/login.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, encoding='utf-8') as fp:
            data = json.load(fp, strict=False)
            return data

    # 根据关键字获取数字
    def get_data(self, key):
        return self.data[key]

    # 写入json
    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    operation = OperationJson('../dataconfig/cookie.json')
    print(operation.get_data("apsid"))
