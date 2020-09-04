class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting now..")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill", "F")
# print(skillf.email)

# print(type(skillf))             # its show type of string or object
# print(id("id number"))          # its show id number of string or object
o = "omkar sutar"
print(dir("o"))                   # show all attributes that can do with string or object

import inspect                    # module to inspect object or string
print(inspect.getmembers(skillf))


class A:
    classvariables = "these are the class variables"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

object = A("omkar", "sutar")

print("object attributes are")
print(dir(object))
print("\nobject variable attributes")
print(dir(object.name))
print("\nclass attributes are")
print(dir(A))
print("\nclass variable attributes are")
print(dir(A.classvariables))