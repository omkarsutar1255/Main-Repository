class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        list1 = string.split("-")
        """return cls(list[0], list[1], list[2])"""
        return cls(*list1)

    @staticmethod
    def printgood(string):
        print("this is " + string)


class Programmer(Employee):  # taking properties of Employee class
    no_of_holiday = 56  # new variable

    def __init__(self, name, salary, role, languages):  # adding extra elements to class
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):  # use other name for function
        return f"name is {self.name}, salary is {self.salary}, role is {self.role} and languages are {self.languages}"


omkar = Employee("omkar", 50000, "student")
avdhut = Employee("rohan", 40000, "friend")

shubham = Programmer("shubham", 555, "programmer", ["python"])
karan = Programmer("karan", 755, "programmer", ["python", "cpp"])

print(karan.printprog())
print(karan.no_of_holiday)
