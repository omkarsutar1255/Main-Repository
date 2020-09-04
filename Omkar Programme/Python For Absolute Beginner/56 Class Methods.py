class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):  # to add object variable in class
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod  # class method are use to make changes in class properties from object
    def change_leaves(cls, newleaves):  # can change class variable and set new value
        cls.no_of_leaves = newleaves


omkar = Employee("omkar", 50000, "student")
avdhut = Employee("rohan", 40000, "friend")

avdhut.change_leaves(34)  # can change from object
Employee.change_leaves(100)  # can change from class
# Employee.no_of_leaves = 89
print(omkar.no_of_leaves)
