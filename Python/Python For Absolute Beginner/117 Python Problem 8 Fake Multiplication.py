# Date - 25/06/2020
# Purpose - To find wrong index in table
import random
lst = []
# Rohandas function to get wrong input

def rohandas(a, b):
    f = 1
    z = random.randrange(1, b)
    for i in range(b):
        if i == z and a > 5 and f == 1:
            lst.append((a * (i+1)) + random.randrange(0, 4))
            f = f + 1
        else:
            lst.append(a * (i+1))
# Omkar function to find wrong index of multiflication table


def omkar(lst):
    i = 1
    for item in lst:
        if item % i == 0:
            i = i + 1
            pass
        else:
            print(f"{item} is wrong ans")
            i = i + 1


rohandas(6, 10)
print(lst)
omkar(lst)


"""import random

def rohanMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1

    return None

if __name__ == "__main__":
    # print(rohanMultiplication(7))
    number = int(input("Enter a number: "))
    myTable = rohanMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
"""
