import sys

print(sys.path)  # show path of module

from sklearn.ensemble import forest

print(forest)  # print class of module

import file2

print(file2.a)  # use files2.a so 'a' will only come from file2
file2.printjoke("omkar sutar")
