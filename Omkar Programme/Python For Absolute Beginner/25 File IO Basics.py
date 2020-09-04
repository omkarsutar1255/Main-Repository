# Files Io Basics
"""
"r" = read dada from files       # default mode
"w" = write in files
"x" = create files if not exist
"a" = add something at end
"t" = text mode                   # default mode
"b" = binary mode
"+" = read and write
"""
# Question of day
def func1(a,b):
    """This is use to minus number"""
    c = (a-b)
    return c

f = func1(56, 24)
print(f)
print(func1.__doc__)