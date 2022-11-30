from re import fullmatch
from .exceptions import InvalidCustomerPhoneNumberException
from .exceptions import InvalidCustomerIdException
from .exceptions import InvalidCustomerNameException


class Customer:

    def __init__(self, cid, lname, fname, pnumber):

        self.__MATCH_PHONE_NUMBER = "[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$"
        self.__MATCH_NAME = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
        if not fullmatch(self.__MATCH_NAME, lname):
            raise InvalidCustomerNameException(lname)

        if not fullmatch(self.__MATCH_NAME, fname):
            raise InvalidCustomerNameException(fname)

        if not fullmatch(self.__MATCH_PHONE_NUMBER, pnumber):
            raise InvalidCustomerPhoneNumberException(pnumber)

        if cid not in range(1000, 10000):
            raise InvalidCustomerIdException(cid)

        self.__customer_id = cid
        self.__last_name = lname
        self.__first_name = fname
        self.__phone_number = pnumber

    def __str__(self):
        return f"Customer({self.__customer_id}, {self.__last_name}, {self.__first_name}, {self.__phone_number})"


    def __repr__(self):
        return f"'Customer({self.__customer_id}, {self.__last_name}, {self.__first_name}, {self.__phone_number})'"

    def change_last_name(self, name):
        if not fullmatch(self.__MATCH_NAME, name):
            raise InvalidCustomerNameException(name)

        self.last_name = name

    def change_first_name(self, name):

        if not fullmatch(self.__MATCH_NAME, name):
            raise InvalidCustomerNameException(name)

        self.first_name = name

    def change_phone_number(self, number):
        if not fullmatch(self.__MATCH_PHONE_NUMBER, number):
            raise InvalidCustomerPhoneNumberException(number)

        self.phone_number = number