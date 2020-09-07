list = [["name","omkar"],["village","siddhanerli"],
        ["tal","kagal"],["dis","kolhapur"],["college","sit"]]
#make list in [] type
for a,b in list:   # list can directly print
    print(a,b)
dict1= dict(list)  # for turn list in dictionary


zzzz = {"iu":"sduh",
        "dfc":"sda",
        "sahu":"ihdu"}
print(zzzz["dfc"])  # to print values of dictionary key
for a,b in zzzz.items():   # .items use for turn dictionary into list and without that onlt keys will display
    print(a,b)


list = [1,"fsdfg",85,56,45,46,85,2,3,4,5,456.43,44.5,6]
for a in list:
    if isinstance(a,int) and a >= 6:  # isinstance use for check value is int,float,string and double or not
        print(a)


list = [1,"fsdfg",85,56,45,46,85,2,3,4,5,456.43,44]
for b in list:
    if str(b).isnumeric() and b > 6:  # convert into string and then check numeric
        print(b)