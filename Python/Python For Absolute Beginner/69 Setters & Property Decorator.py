class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
        # if self.email is set in constructor then it will call for self.email

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property             # when set self.fname or self.lname set outside class and used inside class
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set. Please set using setter"
        return f"{self.fname}.{self.lname}@gmail.com"           # return with new values provided by user

    @email.setter          # setter are used to set self.fname and self.lname inside function
    def email(self, string):
        print("setting now..")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter           # deleter are used to delete self.fname and self.lname inside class
    def email(self):
        self.fname = None
        self.lname = None


omkar = Employee("omkar", "sutar")

print(omkar.email)                # calling function email from class Employee
omkar.fname = "popat"             # setting self.fname as popat outside the class
print(omkar.email)                # getting new email with self.fname as popat in it due to property decorator
omkar.email = "sutar.amol@gmail.com"     # setting self.fname and self.lname inside the by using setter decorator
print(omkar.email)                    # calling email function with new value of fname and lname set by setter decorator
del omkar.email                       # deleting self.fname and l.name as none by using deleter decorator
print(omkar.email)                    # calling email function with new self.fname and self.lname values
