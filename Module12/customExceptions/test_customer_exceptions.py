"""
Brandon Treu 900704435

test customer exceptions
"""

import unittest
from customers.customers import Customer
from customers.exceptions import InvalidCustomerIdException
from customers.exceptions import InvalidCustomerNameException
from customers.exceptions import InvalidCustomerPhoneNumberException


class CustomerTests(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1000, "Smith", "Jane", "555-555-5555")

    def tearDown(self):
        del self.customer

    def test_valid_params(self):
        invalidId = False
        invalidName = False
        invalidPhoneNumber = False
        try:
            self.customer = Customer(9999, "Smith", "John", "555-555-5555")

        except InvalidCustomerIdException:
            invalidId = True
        except InvalidCustomerNameException:
            invalidName = True
        except InvalidCustomerPhoneNumberException:
            invalidPhoneNumber = True

        self.assertFalse(invalidId)
        self.assertFalse(invalidName)
        self.assertFalse(invalidPhoneNumber)

    def test_invalid_customer_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            self.customer = Customer(10000, "Smith", "John", "555-555-5555")

    def test_invalid_first_name(self):
        with self.assertRaises(InvalidCustomerNameException):
            self.customer = Customer(1000, "Smith", "John1", "555-555-5555")

    def test_change_first_name_invalid(self):
        with self.assertRaises(InvalidCustomerNameException):
            self.customer.change_first_name("John1")

    def test_invalid_last_name(self):
        with self.assertRaises(InvalidCustomerNameException):
            self.customer = Customer(1000, "Smith2", "John", "555-555-5555")

    def test_change_last_name_invalid(self):
        with self.assertRaises(InvalidCustomerNameException):
            self.customer.change_last_name("Smith2")

    def test_invalid_phone_number(self):
        with self.assertRaises(InvalidCustomerPhoneNumberException):
            self.customer = Customer(1000, "Smith", "John", "555-555-555555")

    def test_change_phone_number_invalid(self):
        with self.assertRaises(InvalidCustomerPhoneNumberException):
            self.customer.change_phone_number("555-555-5555555")

    def test_str(self):
        actual = str(self.customer)
        expected = "Customer(1000, Smith, Jane, 555-555-5555)"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()