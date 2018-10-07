import ddt
import unittest

@ddt.ddt

class DataTest(unittest.TestCase):
    
    def setUp(self):
        print("这是setUp")

    def tearDown(self):
        print("这是tearDown")

    @ddt.data(
        [1, 2],
        [2, 3],
        [4, 5]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)

if __name__ == '__main__':
          unittest.main()