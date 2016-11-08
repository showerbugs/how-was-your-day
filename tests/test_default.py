import unittest


class DefaultTestCase(unittest.TestCase):
    def testTrue(self):
        self.assertTrue('This testcase should be success.', True)

if __name__ == '__main__':
    unittest.main()