# Date - 26/06/2020
# Purpose - jumble the names of given student
print("Enter number of names")
ans1 = int(input())
lst = []
# lst one collect the names of student
print("Enter names of children")
for i in range(ans1):
    lst.append(input())
lst1 = []
# lst1 collect first name of student
lst2 = []
# lst2 collect second name of student
lst3 = []
# lst 3 collect third name of student

for item in lst:
    lst1.append(item.split(" ")[0])
    lst2.append(item.split(" ")[1])
    try:
        lst3.append(item.split(" ")[2])
    except Exception as e:
        lst3.append("")
omk = lst1[0]
# rearrange lst1 in wrong order
for i in range(ans1):
    if i == ans1-1:
        lst1[i] = omk
    else:
        lst1[i] = lst1[i+1]
# join items of each list one by one
for item in zip(lst1, lst2, lst3):
    print(" ".join(item))
