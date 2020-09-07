l = 10           # Global varible
def function(n):
    #l = 5       # local varible
    global l     # global keyword that gives permission to change global vaule
    l = l + 10
    print(l)
    print(n, "i have printed")

function("this is me")
print(l)

x = 30
def omkar():
     x = 10

     def rohan():
        global x
        x = 20

     print("omkar is ",x)
     rohan()
     print("sutar is ",x)
omkar()
print(x)
