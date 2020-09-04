f1 = open("reading file 1")

try:
    f2 = open("reading 2")        # file not exist

except EOFError as e:
    print("EOF ala ahe")

except IOError as e:
    print("IO ala ahe")

else:
    print("this will run only if except is not running")

finally:             # Either try run or except run the program in finally always run
    print("run this anyway")
    f1.close()
    # f2.close()

print("Important stuff")