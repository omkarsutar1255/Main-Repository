import requests
omk = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
r = omk.text

sut = r.rstrip().split("\n")

print([[el] for el in sut])

import pickle
cars = sut
file = "picklefile2.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

file = "picklefile2.pkl"
fileob = open(file, 'rb')
print(type(fileob))
picklefile = pickle.load(fileob)
print(picklefile)
print(type(picklefile))
