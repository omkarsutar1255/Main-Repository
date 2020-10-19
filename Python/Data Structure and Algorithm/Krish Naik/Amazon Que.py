# l1 = [1095, 1094, 1095]
# del l1[:]
# l1.extend([1005, 1094, 1095])
# print(l1)


l1 = [8676, 4444, 3333, 2222, 1111]
for i, n in enumerate(l1):
    print(i, n)
    if int(n / 1000) == 1:
        l1[i] = n + 8000
    elif int(n / 1000) == 2:
        l1[i] = n + 6000
    elif int(n / 1000) == 3:
        l1[i] = n + 4000
    elif int(n / 1000) == 4:
        l1[i] = n + 2000
    elif int(n / 1000) == 6:
        l1[i] = n - 2000
    elif int(n / 1000) == 7:
        l1[i] = n + 4000
    elif int(n / 1000) == 8:
        l1[i] = n - 6000
    elif int(n / 1000) == 9:
        l1[i] = n - 8000
    else:
        pass
print(l1)
