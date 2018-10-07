import unittest


class FirstCase(unittest.TestCase):
    def testfirst01(self):
        print("这是第一个case")
    def testfirst02(self):
        print("这是第二个case")
    def testfirst03(self):
        print("这是第三条case")
    def testfirst04(self):
        print("这是第四个case")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("testfirst02"))
    suite.addTest(FirstCase("testfirst01"))
    unittest.TextTestRunner().run(suite)
