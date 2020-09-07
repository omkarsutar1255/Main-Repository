import bisect

number = 234
lst = [23,45,78,90,123,345,567]

print(bisect.bisect(lst, number))

bisect.insort(lst, number)
print(lst)