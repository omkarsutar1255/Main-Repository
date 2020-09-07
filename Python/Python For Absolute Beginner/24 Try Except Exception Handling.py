print("Enter numbers")
a = input()
b = input()  # take as e or somethings else

try:                     # this try and except
    print(int(a) + int(b))      # trying this statement without errors
except Exception as e:          # except use to give similar error pattern
    print(e)
print("this line is important")   # remaining program will run smoothly