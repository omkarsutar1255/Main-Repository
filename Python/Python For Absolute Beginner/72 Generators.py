"""
Iterable - __iter__ or __getitem__()
Iterator _ __next__()
Iteration -
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(5)         # gen function for make generaor

print(g.__next__())           # use one at a time iteration
print(g.__next__())           # cannot repeat one iteration


for i  in g:
    print(i)

ier = iter("omkar")              # iter function is inbuilt function for make generator of string
print(ier.__next__())            # strings are iterable
print(ier.__next__())            # use one at a time iteration
print(ier.__next__())           # cannot repeat one iteration
# stop iteration error : iteration are over so cannot iterate again