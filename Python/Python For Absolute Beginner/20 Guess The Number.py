n = 26
chances = 10
print("you have only 10 chances")
print("enter first value ")
value = input()
person = int(value)   # dont forgot to convert input in integer
while(chances >0 ): # loop condition write in () brackets

    if n == person and chances > 0:
        print("you won")
        print((chances-1),"chances are left")
        break # use break to exit loop

    elif chances==1:
        print("you lose")
        break

    elif person > n:
        print("enter smaller value")
        new = input()
        person = int(new)
        chances = chances - 1

    else:
        print("enter bigger value")
        new = input()
        person = int(new)
        chances = chances - 1