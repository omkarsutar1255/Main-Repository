with open("reading file 2") as f:    # use for read file many times
    a = f.readlines()
    print(a)

f = open("reading file 2")          # use for read file single time
print(f.readline())
f.close()