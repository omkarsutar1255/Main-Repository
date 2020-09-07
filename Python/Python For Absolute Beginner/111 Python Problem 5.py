# date - 24/06/2020
# Purpose - find next palindrome number and if number is less than 10 then take it as it is


def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print("Enter how many number you want to palindrome")
b = int(input())
lst = []
for i in range(b):
    print("Enter the values")
    d = int(input())
    lst.append(d)
lst1 = []
for f in lst:
    if f < 10:
        lst1.append(f)
    else:
        z = next_palindrome(f)
        lst1.append(z)
print(lst1)
