class Employee:  # class name Employee
    no_of_leaves = 8  # variable of class which apply to all objects
    pass


# we can create many objects from one class
omkar = Employee()  # object of class
avdhut = Employee()  # object of class

# way to add init values in class for any object
omkar.name = "omkar"  # variables of class
omkar.salary = 455
omkar.role = "Student"

avdhut.name = "avdhut"  # variables of class
avdhut.salary = 45
avdhut.role = "friend"

print(omkar.salary, omkar.no_of_leaves, Employee.no_of_leaves)  # print values of variables

print(Employee.__dict__)  # dict of class
Employee.no_of_leaves = 10  # variables of class only can change from class
print(Employee.__dict__)  # dict after change class variable

print(avdhut.__dict__)  # dict of object
avdhut.no_of_leaves = 20  # it can change from object or class
print(avdhut.__dict__)  # dict after change object variable

print(Employee.no_of_leaves)  # print variable of class
print(omkar.no_of_leaves)  # print variable of object
print(avdhut.no_of_leaves)  # print variable of object
