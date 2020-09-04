class Employee:
    no_of_leaves = 8

    def printdetails(self):  # use object in self return values according to function
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"
        # methods of class


omkar = Employee()
avdhut = Employee()

omkar.name = "omkar"
omkar.salary = 455
omkar.role = "Student"

avdhut.name = "avdhut"
avdhut.salary = 45
avdhut.role = "friend"

print(omkar.printdetails())  # To put object name in function 'object.function()'


class Employee:
    no_leaves = 8

    def __init__(self, name, salary, role):  # to add object variable in class
        self.name = name
        self.salary = salary
        self.role = role
        print('omkar')             # whole __init__ method is run as object is created
        Employee.no_leaves += 1    # every time we create object it runs init method and then it increase employee value
        # cls property can take using class name
    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"


omkar = Employee("omkar", 50000, "student")  # object created so automatically init method is run
print(omkar.salary)  # to print object variables


def printdetails(nam, sal):
    return f"name is {nam}, salary is {sal}"


n = input()
s = input()
if n == "omkar":
    s = 45000

if n == "avdhut":
    s = 40000
print(printdetails(n, s))
