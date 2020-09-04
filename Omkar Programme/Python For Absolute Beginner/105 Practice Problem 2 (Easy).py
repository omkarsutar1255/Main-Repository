n = int(input("Enter n number\n"))
a = int(input("Enter min numbers\n"))
z = int(input("Entermax numbers\n"))

if a < z:
    for i in range(a, z+1):
        if n % i == 0:
            print(i, "is Divisor of", n)

        else:
            print(i, "is not divisor of", n)
else:
    print("this is not a range")
    if n % a ==0:
        print(a, "is divisor of", n)
    else:
        print(a, "is not divisor of", n)