import math

me = "harry"
a = "this is %s"%me      #this is in string format
print(a)

me = "harry"
a1 = 234
a = "this is %s %s"%(me, a1)   #for adding multiple string
print(a)

me = "harry"
a1 = 234
a = "this is {1} {0}"       # 0 and 1 is default
b = a.format(me, a1)        # collect string in a format
print(b)

me = "harry"
a1 = 234
a = f"this is {me} {a1} {4*65} {math.cos(65)}"    # F string use in carli bracket
print(a)