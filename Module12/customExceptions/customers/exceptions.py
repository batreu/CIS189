class InvalidCustomerIdException(Exception):
    def __init__(self, id=None, message="is not a valid id"):
        self.message = message
        self.id = id

    def __str__(self):
        return f"{self.id}->{self.message}"


class InvalidCustomerNameException(Exception):
    def __init__(self, name=None, message="is not a valid name"):
        self.message = message
        self.name = name

    def __str__(self):
        return f"{self.name}->{self.message}"


class InvalidCustomerPhoneNumberException(Exception):
    def __init__(self, phoneNumber=None, message="is not a valid phone number"):
        self.message = message
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.phoneNumber}->{self.message}"