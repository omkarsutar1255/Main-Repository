#dictonary is nothing but key value pairs

d1 ={} #its dictionary
print(type(d1))
d2 = {"omkar":{"medium1":"size","medium2" :"height"},"amol":"double big","abhi":"normal"}

d2["amit"] = "million" #adding key values
d2["bhuvan"] = 2100    #adding key values
del d2["amol"]         #deleting key values

print("\n", d2, "\n")     # how to add key and values to dictionary

d2 = {"omkar":{"medium1":"size","medium2" :"height"},"amol":"double big","abhi":"normal"}
d3 = d2.copy()            #only copy of d2 paste in d3
del d3["amol"]            #delete amol only in d3 without d2
print(d2)
d2.update({"sss":"zzz"})  #updating key values
print(d2.keys())          #only keys will print
print(d2.items())         #print d2 in item form
print(d2)
print(d2)



# del list["hp2"]
# print(list)