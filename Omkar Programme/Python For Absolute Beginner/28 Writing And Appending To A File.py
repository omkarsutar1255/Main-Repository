f= open("reading file 1", "a")        #  adding content to file
f.write("\npython is great language")
f.close()

f = open("reading file 2","w")   # "w" replace the old content with new one
a = f.write("clean house")  # it give how many character in files to a for print
print(a)                    # show total characters in file its available only with (.write)
f.close()

f=open("reading file 2","r+")  # its use to do read and write both to a file
s = f.read()
print(s)
f.write("\nalso its widely use")
f.close()
