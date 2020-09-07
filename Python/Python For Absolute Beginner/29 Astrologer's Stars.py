print("Enter number of rows")
n = int(input())
print("enter 1 for ascending and 0 for descending order")
v = int(input())
b = 1

if v == 1:
    while b <= n:
        print(b*"*")
        b = b+1

elif v == 0:
    while n >= 0:
        print(n*"*")
        n = n - 1

else:
    print("enter order in form of ascending or descending")