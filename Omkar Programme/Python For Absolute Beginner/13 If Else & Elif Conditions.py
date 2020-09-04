
var1=78
print("enter your value")
var2 = int(input())
if var1>var2:
    print("lesser")
elif var1==var2:        #elif use for else if
    print("equal")
else:
    print("greater")


list={1,2,3,4,5,6}
print(5 in list)            #in is used for check number in list
print(24 not in list)        #not in used for check number not in list
if 14 not in list:
    print("yes its not in list")


print("Enter your age")
age = int(input())

if 7>age:
   print("please Enter valid age")
elif 100<age:
        print("please enter valid age")
elif 18<age:
        print("you are allowed")
else:
    print("you are not allowed")