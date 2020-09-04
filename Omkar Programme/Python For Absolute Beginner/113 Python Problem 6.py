# date - 24/06/2020
# purpose - Game of 2 Player for find number between 2 digit
import random


def game(a, b, z):
    c = random.randrange(a, b)
    print("Player", z)
    print("Enter the guess number")
    n = 1
    while True:
        ans = int(input())
        if ans == c:
            print("correct ans")
            break
        elif ans > c:
            print("Enter smaller number")
        else:
            print("Enter greater number")
        n = n + 1
    print("You guess the number in", n, "th round")
    return n


if __name__ == '__main__':
    s = int(input("Enter values of a\n"))
    d = int(input("Enter values of b\n"))
    g = game(s, d, 1)
    h = game(s, d, 2)
    if g < h:
        print("Player 1 win by", h - g, "points")
    elif g > h:
        print("Player 2 Win by", g - h, "points")
    else:
        print("match Equal")
