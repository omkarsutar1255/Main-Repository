f=open("reading file 1", "rt") # rt is default mode or to print in binary write "rb"
content = f.read(6200)         # reading files upto 6200 limit
print(content)
f.close()                 # always close files after use

f=open("reading file 1", "rt")

for line in f:          # for each line of file
    print(line,end="")  # printing each line by line
f.close()

f=open("reading file 1", "rt")
print(f.readline())     # each line will read
print(f.readline())     # one time fully read file cannot read again
f.close()

f=open("reading file 1", "rt")
print(f.readlines())    # readlines use to read all lines in binary form
f.close()