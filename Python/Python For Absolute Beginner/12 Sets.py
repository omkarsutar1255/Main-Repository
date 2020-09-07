s = set()
print(type(s))

llll = {1, 2, 3, 4}
omk = set(llll)
print(omk)
print(type(omk))

s.add(1)  # addition of values in set
s.add(2)  # addition of values in set
s.remove(2)  # remove set
s1 = s.union({1, 2, 3})  # addition of list
s2 = s.intersection({1, 2, 6})  # find common values
s3 = {4, 5}
print(s.isdisjoint(s3))  # return true if two sets have null intersection
print(s, s1, s2)
