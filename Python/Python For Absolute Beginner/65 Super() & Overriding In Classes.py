# =======Difference between existence of 'super'===========
class A:
    classvar1 = "I am class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        # self.classvar1 = "I am object variable in class A"
        self.special = "special in class varible of A"


class B(A):
    classvar1 = "I am class variable in class B"

    def __init__(self):  # override on class A
        super().__init__()  # super().__init__() to cancel override class A
        self.var1 = "I am inside class B's constructor"
        # self.classvar1 = "I am object variable in class B"


a = A()
b = B()

print(b.var1, b.special)

print(b.classvar1)  # first check in object variable of class B


# then  check in object variable of class A if not override in class B
# then  check in class  variable in class B
# then  check in class  variable of class A

# =======Difference between above and below of 'super'===========
class A:
    classvar1 = "classvar - class variable in class A"
    special = "special - class variable in class A"

    def __init__(self):
        self.omkar = "sutar"
        self.classvar1 = "I am object variable in class A"
        self.special = "special in object variable of A"

    def hello(self):
        print('parent class object')


class B(A):
    classvar1 = "classvar - class variable in class B"
    special = "special - class variable in class B"

    def __init__(self):
        self.classvar1 = "I am object variable in class B"  # above super take first from class A object variables
        # then class B object variables
        # then from class B class variable
        # then from class A class variable
        super().__init__()           # calling class A __init__ function
        self.omkar = "omkar"  # there has to be something in def function

        self.special = "special in object variable of B"  # below super take first from class B object variables
        # then class A object variables
        # then from class B class variable
        # then from class A class variable

    def hello(self):
        super().hello()  # this is how we can call class methods also through super
        print('child class object')


a = A()
b = B()
print(b.classvar1)
print(b.special)
print(b.hello())
