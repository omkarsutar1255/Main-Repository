# date - 24/06/2020
# purpose - to get next palindrome number from your given number

print("Enter how many number you want to palindrome")
b = int(input())

lst = []
for i in range(b):
    print("Enter the values")
    d = int(input())
    lst.append(d)

lst2 = []
for i in lst:
    while True:
        om = i
        r = 0
        while i > 0:
            r = r * 10
            r = r + i % 10
            i = int(i / 10)
        if om != r:
            i = om + 1
        else:
            lst2.append(om)
            break

for z in range(b):
    print("\nnext palindrome for", lst[z], "is", lst2[z])
