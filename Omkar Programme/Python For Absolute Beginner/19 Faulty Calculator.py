#45*3=555, 56+9=77, 56/6=4

print("enter add, multiply, divide")
work = input()
print("Enter two values")
a = int(input())
b = int(input())

if a==45 and b==3 and work=="multiply": #use and between many argument
    print("45 * 3 = 555")
elif a==56 and b==9 and work=="add":       #put input in ("  ") sign
    print("56 + 9 = 77")
elif a==56 and b==6 and work=="divide":
    print("56 / 6 = 4")
elif work=="multiply":
    c = a*b
    print(c)
elif work=="add":
    c= a+b
    print(c)
elif work=="divide":
    c = a/b
    print(c)
else:
    print("retry")