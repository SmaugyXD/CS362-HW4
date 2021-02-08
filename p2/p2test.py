import unittest
import p2

class test_p2(unittest.TestCase):

    def testNum(self):
        self.assertEqual(p2.average([1,2,3,4,5,6,7,8,9,10]), 5.5)

    def testFloat(self):
        self.assertEqual(p2.average([1.2,3.4,5.6]), 3.4)

    def testEmpty(self):
        self.assertRaises(ValueError, p2.average, []) 

    def test_missing_args(self):
        self.assertRaises(TypeError, p2.average)

if __name__ == '__main__':
    unittest.main()
        