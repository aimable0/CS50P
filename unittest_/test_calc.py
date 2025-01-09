import unittest
import calc

# initially we create a test class that inherits from TestCase


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        # test some edge cases.
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        # test some edge cases.
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_mulitply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        # test some edge cases.
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        # test some edge cases.
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # test errors approach 1
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # test errors approach 2 using contenxt manager "with"
        with self.assertRaises(ValueError):
            calc.divide(20, 0)


if __name__ == "__main__":
    unittest.main()
