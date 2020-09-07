ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)

ls = [i for i in range(100) if i%3==0]       # list comprehension

print(ls)

dict1 = {i:f"item{i}" for i in range(1, 12) if i%2==0}    # dictionary comprehension
print(dict1)
dict1 = {value:key for key,value in dict1.items()}        # can change key:value to value:key
print(dict1)

dresses = {dress for dress in ["dress1", "dress2", "dress3", "dress2"]}    # set comprehension cannot give repeated values
print(type(dresses))
print(dresses)

dresses = [dress for dress in ["dress1", "dress2", "dress3", "dress 2"]]    # list comprehension can give repeated values
print(type(dresses))
print(dresses)

evens = (i for i in range(100) if i%10==0)         # generator comprehension  use parenthisis
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())

for items in  evens:
    print(items)

print("how much values do you want in a list")
limit = int(input())
print("enter values of list")
list = []
for i in range(limit):
    list.append(input())



print("press 1 for list comprehension\npress 2 for set comprehension\npress 3 for generator comprehension")
ans = int(input())
if ans == 1:
    ls = [i for i in list]
    print(ls)
elif ans == 2:
    dresses = {i for i in list}
    print(type(dresses))
    print(dresses)

elif ans == 3:

    dict1 = (i for i in list)
    print(type(dict1))
    for item in dict1:
        print(item)