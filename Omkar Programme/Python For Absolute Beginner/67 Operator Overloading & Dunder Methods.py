class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name {self.name}, salary {self.salary}, role {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

# search mapping operator to function on google for check more functions
    def __add__(self, other):  # dunder methods     # Mapping operator to function
        return self.salary + other.salary

    def __truediv__(self, other):  # dunder methods     # Mapping operator to function
        return self.salary / other.salary

    def __repr__(self):  # Operator overloading
        return f"name {self.name}, salary {self.salary} and role {self.role}"

    def __str__(self):  # Operator overloading
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"


emp1 = Employee("omkar", 30, "programmer")
emp2 = Employee("rohan", 20, "cleaner")

print(emp1 + emp2)  # to use add operator on object variables
print(emp1 / emp2)  # to use divide operator on object variables

# str is informal output for user to easily understand
# repr is official detailed output for programmer to debug and development more detailed code
print(emp1)  # str calling if str not exist then repr calling
print(repr(emp1))  # repr calling
print(str(emp1))  # str calling if str not exist then repr calling
