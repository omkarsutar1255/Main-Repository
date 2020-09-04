list = ["zero", "one", "three", "four"]

i = 1                    # we can initial the position of for loop
for item in list:
    if i % 2 is not 0:
        print(f"jarvis say number {item}")
    i += 1                 # have to increment each time

list = ["zero", "one", "three", "four"]

for index, item in enumerate(list):         # enumerate list start with 0 but increment by 1 automatically
    if index % 2 == 0:
        print(f"jarvis say number {item}")