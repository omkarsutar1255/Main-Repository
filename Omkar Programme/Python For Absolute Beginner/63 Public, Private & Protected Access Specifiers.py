# Public -    That can access within class, in child class and outside classes also
# Protected - That can access within class and in child class only
# Private -   That can access within that particular class


class Employee:
    var = 8  # public variable
    _protec = 16  # protected variable
    __private = 99  # private variable

    def __init__(self, name, salary, role):
        self.name = name
        self._salary = salary
        self.__role = role

    def printdetails(self):
        return f"name is {self.name}, salary is {self._salary} and role is {self.__role}"


emp = Employee("omkar", 45000, "student")
print(emp.var)  # public variable can directly access from class and to sub class as well
# print(emp.protec)              # protected variables cannot access from class but directly access to sub classes
print(emp._protec)  # protected variables can access with using '_protec' element
# print(emp.private)             # private variables cannot access from class its only use within that class
print(emp._Employee__private)  # private variables can access with using '_Employee' element (name mangling)
print(emp.printdetails())  # after access to other function of class we can get private and protected values
