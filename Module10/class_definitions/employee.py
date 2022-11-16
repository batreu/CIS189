class Employee:

    """
    Brandon Treu 900704435
    employee.py
    """

    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.salaried = salaried
        self.start_date = start_date
        self.salary = salary

    def __str__(self):
        return ' ' + '\n' + str(self.first_name) + '\n' + str(self.last_name) + '  ' + str(self.address) + '\n' + str(self.phone_number) + '\n' + str(self.start_date) + '\n' + str(self.salary)

    def __repr__(self):
        return ' ' + '\n' + str(self.first_name) + '\n' + str(self.last_name) + '  ' + str(self.address) + '\n' + str(self.phone_number) + '\n' + str(self.start_date) + '\n' + str(self.salary)

    def display(self):
        print(self)

employee1 = Employee('Treu','Brandon', '101 Fake Drive', '515-720-1852', True, '03/16/2020',55000)
employee1.display()