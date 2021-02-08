import unittest
import p3

class test_p3(unittest.TestCase):

    def test_name(self):
        self.assertEqual(p3.full_name("Huy", "Nguyen"), "Huy Nguyen")

    def test_string(self):
        self.assertRaises(TypeError, p3.full_name, 1, 2.1)

    def test_empty(self):
        self.assertRaises(TypeError, p3.full_name)
        self.assertRaises(TypeError, p3.full_name, "What")

    def test_list(self):
        self.assertRaises(TypeError, p3.full_name, ["Huy", "Nguyen"])

if __name__ == '__main__':
    unittest.main()
        