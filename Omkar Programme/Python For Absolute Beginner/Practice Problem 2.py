def facto(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * facto(n-1)


g = facto(int(input("Enter the number\n")))
print(g)
i = 10
b = 0
while True:
    if g % i == 0:
        i = i * 10
        b = b + 1
    else:
        print(b)
        break
