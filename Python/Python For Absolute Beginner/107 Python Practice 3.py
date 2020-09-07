n = int(input("Enter the number how many items do you want in list : "))
print("Enter values of list")
lst = []
for i in range(n):
    lst.append(input())

lst1 = lst.copy()
lst1.reverse()
print(lst1)

lst2 = lst.copy()
c = lst2[::-1]
print(c)

z = 0
for i in range(int(n/2)):
    c = lst[z]
    d = lst[n-1]
    lst[z] = d
    lst[n-1] = c
    z = z + 1
    n = n - 1
print(lst)

if lst1 == c and c == lst:
    print("All lists are same")