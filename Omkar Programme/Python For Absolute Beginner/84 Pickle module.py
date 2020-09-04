import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]      # it can be list, tupple
file = "picklefile.pkl"                                      # file name
fileobj = open(file, 'wb')                              # open file in binary mode
pickle.dump(cars, fileobj)                              # pickle function
fileobj.close()                                         # close file


file = "picklefile.pkl"
fileob = open(file, 'rb')
print(type(fileob))                  # class bufferredReader type
picklefile = pickle.load(fileob)     # use load for not read file
print(picklefile)
print(type(picklefile))


file = "picklefile.pkl"            # file name
fileob = open(file, 'rb')          # open file in binary mode
print(type(fileob))                # class bufferredReader type
f = fileob.read()                  # read file
print(type(f))                     # class bytes type
picklefile = pickle.loads(f)       # use loads 's' stands for string
print(picklefile)                  # pickled file
print(type(picklefile))            # class list
