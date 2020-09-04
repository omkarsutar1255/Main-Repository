def function1():
    print("subscribe now")

fun2 = function1
del function1
fun2()              # method of print functions

def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a=funcret(1)
print(a)

def executor(func):
    func("this")
executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("executed")
    return nowexec
@dec1                       # to send one function to another function
def omkar():
    print("programming")

# omkar = dec1(omkar)       # to send one function to another function
omkar()                     # method of print functions