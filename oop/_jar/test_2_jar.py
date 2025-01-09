import unittest
from jar import Jar

class TestJar(unittest.TestCase):
    def setUp(self):
        """Set up a new jar before each test"""
        self.jar = Jar(12)

    def test_init(self):
        """Test initialization of jar with valid capacity"""
        self.assertEqual(self.jar.capacity, 12)
        self.assertEqual(self.jar.size, 0)

    def test_invalid_capacity(self):
        """Test that negative capacity raises ValueError"""
        with self.assertRaises(ValueError):
            Jar(-1)
        with self.assertRaises(ValueError):
            Jar(0)

    def test_deposit_valid(self):
        """Test valid cookie deposits"""
        self.jar.deposit(1)
        self.assertEqual(self.jar.size, 1)
        self.jar.deposit(2)
        self.assertEqual(self.jar.size, 3)

    def test_deposit_invalid(self):
        """Test deposits exceeding capacity raise ValueError"""
        with self.assertRaises(ValueError):
            self.jar.deposit(13)  # Exceeds capacity of 12

        # Fill jar to capacity then try to add more
        self.jar.deposit(12)
        with self.assertRaises(ValueError):
            self.jar.deposit(1)

    def test_withdraw_valid(self):
        """Test valid cookie withdrawals"""
        self.jar.deposit(5)
        self.jar.withdraw(2)
        self.assertEqual(self.jar.size, 3)
        self.jar.withdraw(3)
        self.assertEqual(self.jar.size, 0)

    def test_withdraw_invalid(self):
        """Test withdrawals exceeding available cookies raise ValueError"""
        self.jar.deposit(5)
        with self.assertRaises(ValueError):
            self.jar.withdraw(6)

        # Try to withdraw from empty jar
        self.jar = Jar(12)  # Reset to empty jar
        with self.assertRaises(ValueError):
            self.jar.withdraw(1)

    def test_str_representation(self):
        """Test string representation of jar"""
        self.assertEqual(str(self.jar), "")  # Empty jar
        self.jar.deposit(1)
        self.assertEqual(str(self.jar), "🍪")
        self.jar.deposit(2)
        self.assertEqual(str(self.jar), "🍪🍪🍪")

    def test_size_property(self):
        """Test size property reflects actual number of cookies"""
        self.assertEqual(self.jar.size, 0)
        self.jar.deposit(5)
        self.assertEqual(self.jar.size, 5)
        self.jar.withdraw(3)
        self.assertEqual(self.jar.size, 2)

if __name__ == "__main__":
    unittest.main()