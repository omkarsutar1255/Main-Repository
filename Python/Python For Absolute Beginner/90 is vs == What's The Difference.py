
# == - value equality - Two object have the same value
# is - reference equality - Two references refer to the same object

# Python Console
# a = [7,4,5]
# b = a        # b is second reference of a

# b == a
# True

# b is a
# True

# b[0] = 0
# a
# [0, 4, 5]

# c = a[:]               # c is new object having similar values of a
# b == c
# True
# a == c
# True
# c is a
# False

a = [6, 4, "34"]
b = [6, 4, "34"]
print(b is a)