class Employee:
    no_of = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @staticmethod  # if we use class values like no_of then use @classmethod & cls.no_of inside def
    # if we use class def values like self.name then use self.name while use
    # but if we dont want class values and class def values only want outside values then use @staticmethod

    def printgood(string):  # its in the class because only class and objects variables can use it
        print("this is " + string)
        return "returns the value"  # skip if not want return value


omkar = Employee("omkar", 50000, "student")
avdhut = Employee("rohan", 40000, "friend")

Employee.printgood("good")
omkar.printgood("me")  # not give return value if not printed
print(omkar.printgood("me"))  # this will give return value
