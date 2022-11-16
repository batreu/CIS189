class Student:
    """
    Brandon Treu 900704435
    Student class
    """
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_characters.issuperset(lname) or not name_characters.issuperset(fname) \
                or not name_characters.issuperset(major):  # check appropriate chars
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        if not isinstance(gpa, float):  # check gpa is float
            raise ValueError
        if gpa < 0 or gpa > 4:  # check gpa in range
            raise ValueError('gpa out of range')
        self.gpa = gpa

    def __str__(self):
        return "Student: %s, %s, %s, %s" % (self.last_name, self.first_name, self.major, self.gpa)

    def __repr__(self):
        return "Student: lname=%s, fname=%s, major=%s, gpa=%s" % (self.last_name, self.first_name, self.major, self.gpa)

    def display(self):
        return self.first_name + ' ' + self.last_name + " is majoring in " + self.major +\
                                     " with GPA: " + str(self.gpa)


# Driver
student = Student('Ovechkin', 'Alex', 'Goal Scoring', 4.0)
print(repr(student))