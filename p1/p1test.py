import unittest
import p1

class test_p1(unittest.TestCase):

    def testInt(self):
        self.assertEqual(p1.volume_cube(10), 1000)

    def testFloat(self):
        self.assertEqual(p1.volume_cube(5.5), 166.375)

    def testZero(self):
        self.assertEqual(p1.volume_cube(0), 0) 

    def testNegative(self):
        self.assertRaises(ValueError, p1.volume_cube, -1)

    def testString(self):
        self.assertRaises(TypeError, p1.volume_cube, "a string")

    def testComplex(self):
        self.assertRaises(TypeError, p1.volume_cube, 5j)

    def testNone(self):
        self.assertRaises(TypeError, p1.volume_cube)

if __name__ == '__main__':
    unittest.main()
        