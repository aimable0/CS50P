import unittest
from employee import Employee

# note: the test below don't run in order its important to have that in mind
# such that test can run independently..


class TestEmployee(unittest.TestCase):

    def setUp(self):
        # this method runs before every test method
        self.employee_1 = Employee("ange", "mutesi", 200)
        self.employee_2 = Employee("james", "iradukunda", 300)

    def tearDown(self):
        # this is a cleanup method.. that runs after every test method.
        pass

        # ex if you created a test method that creates a file
        # then the tearDown should be able to delete that file after test
        # since it was for test purposes
        # or even to have a fresh env each time you test.

    def test_email(self):

        self.assertEqual(self.employee_1.email, "ange.mutesi@gmail.com")
        self.assertEqual(self.employee_2.email, "james.iradukunda@gmail.com")

        self.employee_1.first = "nyinawinka"
        self.employee_2.first = "fisheri"

        self.assertEqual(self.employee_1.email, "nyinawinka.mutesi@gmail.com")
        self.assertEqual(self.employee_2.email, "fisheri.iradukunda@gmail.com")

    def test_fullname(self):

        self.assertEqual(self.employee_1.fullname, "ange mutesi")
        self.assertEqual(self.employee_2.fullname, "james iradukunda")

        self.employee_2.last = "Ira"
        self.employee_1.last = "Mutesa"

        self.assertEqual(self.employee_1.fullname, "ange Mutesa")
        self.assertEqual(self.employee_2.fullname, "james Ira")

    def test_applyraise(self):

        self.employee_1.apply_raise()
        self.employee_2.apply_raise()

        self.assertEqual(self.employee_1.pay, 210)
        self.assertEqual(self.employee_2.pay, 315)


if __name__ == "__main__":
    unittest.main()
