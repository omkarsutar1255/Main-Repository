class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):  # to add object variable in class
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def from_str(cls, string):  # convert string into items(tupple)
        list = string.split("-")  # split string wherever '-' sign
        """return cls(list[0], list[1], list[2])"""
        return cls(*list)  # args use convert list into items


omkar = Employee("omkar", 50000, "student")
avdhut = Employee("rohan", 40000, "friend")
karan = Employee.from_str("karan-750-dancer")  # object variables in the form of string
print(karan.salary)
