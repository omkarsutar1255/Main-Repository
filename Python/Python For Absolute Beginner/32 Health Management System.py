print("lock press 1 or retrive press 2")
a = int(input())
def getdate():
    import datetime
    return datetime.datetime.now()
j = str([str(getdate())])
if a == 1:
    print("Enter name of client")
    print("1 for harry, 2 for ron, 3 for harmy")
    b = int(input())
    print("1 for exercise, 2 for diet")
    c = int(input())
    if b < 3 or c < 2:
        print("enter what you did")
        d = input()
        if b == 1 and c == 1:
            with open("11 harry exercise", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
        elif b == 1 and c == 2:
            with open("11 harry diet", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
        elif b == 2 and c == 1:
            with open("11 ron exercise", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
        elif b == 2 and c == 2:
            with open("11 ron diet", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
        elif b == 3 and c == 1:
            with open("11 harmy exercise", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
        else:
            with open("11 harmy exercise", "a") as f:
                f.write("\n" + j + " : " + d)
            print("you write successfully")
    else:
        print("Enter correct number")
elif a == 2:
    print("Enter name of client")
    print("1 for harry, 2 for ron, 3 for harmy")
    b = int(input())
    print("1 for exercise, 2 for diet")
    c = int(input())
    if b < 3 or c < 2:
        print("enter what you did")
        if b == 1 and c == 1:
            with open("11 harry exercise") as f:
                print(f.read())
        elif b == 1 and c == 2:
            with open("11 harry diet") as f:
                print(f.read())
        elif b == 2 and c == 1:
            with open("11 ron exercise") as f:
                print(f.read())
        elif b == 2 and c == 2:
            with open("11 ron diet") as f:
                print(f.read())
        elif b == 3 and c == 1:
            with open("11 harmy exercise") as f:
                print(f.read())
        else:
            with open("11 harmy exercise") as f:
                print(f.read())
    else:
        print("Enter correct number")
else:
    print("Enter correct number")