class A:
    def met(self):
        print("method of class A")


class B(A):  # If not in class B then from class A
    def __init__(self):
        print('sutar')

    def met(self):
        print("method of class B")


class C(A):  # If not in class C then from class A
    def __init__(self, name):
        print('omkar is ', name)

    def met(self):
        print("method of class C")


class D(B, C):  # If not in class D then from class B and then class C
    def __init__(self, ll):
        print('child class init')
        C.met(self)  # calling class C method
        B.__init__(self)  # from here we can call B class init
        C.__init__(self, ll)  # from here we can call C class init


a = A()
b = B()
d = D('king')  # calling init method of class D()

d.met()  # get first inheritance class for D that is B so called B class met function
