list = ["john cena", "randy", "orton", "sheamus", "khali", "jinder mahal"]

for item in list:
    print(item, "and", end=" ")

a = " and ".join(list)          # join the items with defined word
print(a, "other wwe superstars")