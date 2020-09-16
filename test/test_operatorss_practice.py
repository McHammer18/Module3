import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        self.assertFalse(18 == 35)
        self.assertTrue(18 != 35)
        self.assertFalse(0 > 3)
        self.assertTrue(0 < 3)
        self.assertFalse(5 >= 17)
        self.assertTrue(5 <= 17)

if __name__ == '__main__':
    unittest.main()
