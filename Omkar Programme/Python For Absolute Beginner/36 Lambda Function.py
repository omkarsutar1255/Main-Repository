c=lambda a, b:a+b
print(c(5,6))

def first(a):
    return a[1]

a = [[25,34], [15,16], [28,29]]
a.sort(key=first)                  # key use to define user defined output
print(a)

a = [[25,34], [15,16], [28,29]]
a.sort()                           # key is none here so its sort based upon predefined method
print(a)


a = [[25,34], [15,16], [28,29]]
a.sort(key=lambda x:x[1])           # key use to define user defined output
print(a)

def iseven(n):
    return n%2==0

nums = [1,6,2,8,3,7,2,8,4,9]
b = list(filter(iseven,nums))       # list is used so its gives values in list form

print(b)

from functools import reduce
nums = [1,6,2,8,3,7,2,8,4,9]
a = list(filter(lambda n:n%2==0,nums)) # filter use function and list name and then filter according to function
b = list(map(lambda n:n*2,a))          # map use to change value and for that it takes function and list
c = reduce(lambda d,e:d+e,b)           # reduce is use to reduce list in one integer
print(c)