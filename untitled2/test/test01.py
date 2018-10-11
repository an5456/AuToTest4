import unittest

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case运行之前运行1111")

    @classmethod
    def tearDownClass(cls):
        print("所有case运行之后运行1111")

    def setUp(self):
        print("前置处理器")

    def tearDown(self):
        print("后置处理器")

    def test01(self):
        print("第一条case")
    #@unittest.skip("跳过")
    def test02(self):
        print("第二条case")

    def test03(self):
        print("第三条case")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test02"))
    suite.addTest(FirstCase("test01"))
    suite.addTest(FirstCase("test03"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
