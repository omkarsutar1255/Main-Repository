print("Enter the price items")
total = int(input())
i = 1
print(f"{i} item price = {total}")
while True:
    i = i + 1
    a = int(input())
    print(f"{i} item price = {a}")
    total = a + total
    print("total is = ", total)
    z = input("Enter t to exit\n")
    if z == "q":
        break
    else:
        print("Enter next value")
