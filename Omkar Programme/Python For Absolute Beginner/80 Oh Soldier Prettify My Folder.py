import os

omk = os.listdir(os.getcwd())

for item in omk:
    os.rename(item, item.capitalize())

sut = os.listdir(os.getcwd())
i = -1
for item in sut:
    i = i + 1
    if item.endswith(".jpg"):
        os.rename(item, str(i) + " " + item)