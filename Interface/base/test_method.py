import unittest

from base.Mock import moco_test
from base.test import RunMain

import json
from mock import mock


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data1 = {

            'username': 'andong',
           'sex': '男'
        }
        data = {

            'username': 'andong',
            'password': '54325432'
        }
        res = moco_test(self.run.run_main, data1, url, 'POST', data)
        print(res)

        # self.run.run_main = mock.Mock(return_value=data)
        #res = self.run.run_main(url, 'POST', data)
        #res1 = json.loads(res)


    # def test_02(self):
    #     url = 'http://127.0.0.1:8000/login/'
    #     data = {
    #
    #         'username': 'andong',
    #         'password': '54325432'
    #     }
    #     res = self.run.run_main(url, 'POST', data)
    #     res1 = json.loads(res)
    #     print(res1)
    #     if res1['username'] == 'andong':
    #         print("测试成功")
    #     else:
    #         print("测试失败")
    # #     # an = 'andong '
    #     # self.assertEqual(res1['username'], an)


if __name__ == '__main__':
    unittest.main()
