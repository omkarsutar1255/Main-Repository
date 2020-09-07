f = open("reading file 2")
print(f.tell())     # tell position of reading file
print(f.readline())

f.seek(16)           # make position to reading file
print(f.readline())

f.close()          # closing is important