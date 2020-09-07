def facto_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("Enter some value\n"))
print(facto_iterative(number))

def facto_recursive(n):
    if n ==1:
        return 1
    else:
        return n * facto_recursive(n-1)


number = int(input("Enter some value\n"))
print(facto_recursive(number))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number = int(input("Enter some value\n"))
print(fibonacci(number))