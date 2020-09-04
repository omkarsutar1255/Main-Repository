# Snake Water Gun
import random
chances = 1
d = 0
e = 0
while(chances<=10):
    b = ("s", "w", "g")
    a = random.choice(b)
    print("Enter Your Choice\ns for Snake\nw for Water\ng for Gun")
    c = input()
    if a == "s":
        if c == "s":
            print("Equal")
        elif c == "w":
            print("You Lose")
            e = e + 1
        elif c == "g":
            print("You Win")
            d = d + 1
        else:
            print("Enter Correct Letter")
            chances = chances - 1
    elif a == "w":
        if c == "s":
            print("You Lose")
            e = e + 1
        elif c == "w":
            print("Equal")
        elif c == "g":
            print("You Win")
            d = d + 1
        else:
            print("Enter Correct Letter")
            chances = chances - 1
    elif a == "g":
        if c == "s":
            print("You Win")
            d = d + 1
        elif c == "w":
            print("You Lose")
            e = e + 1
        elif c == "g":
            print("Equal")
        else:
            print("Enter Correct Letter")
            chances = chances - 1
    else:
        print("Enter Correct Letter")
        chances = chances - 1
    chances = chances + 1

if chances == 11:
    print(f"You Win {d} Times")
    print(f"Computer Win {e} Times")
    if d > e:
        print("You Are Winner")
    elif d == e:
        print("Equal Score")
    else:
        print("You Lose")