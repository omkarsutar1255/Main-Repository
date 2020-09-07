"""string will in name then we can print as it is"""
name = "omkar sutar"
print(name)

"""string we display how much character you want"""
name = "omkar sutar"
print(name[0:11])

"""we can print leangth of string"""
name = "omkar sutar"
print(name[0:11])
print(len(name))

"""we can skip string varianble"""
name = "omkar sutar"
print(name[0:11:2])

"""by default - start = 0
end = length
skip = 1"""
name = "omkar sutar"
print(name[::])

"""using negative sign will count form last"""
name = "omkar sutar and bad boy"
print(name[-7:-1:2])
"""use -1 at skip for reverse string"""

name = "omkar sutar is bad boy"

print(name.isalnum()) #its check spaces in sentence
print(name.isalpha())
print(name.endswith("boy")) #its check end of string
print(name.count("b")) # its count argument of letter
print(name.capitalize()) #its capitliz
print(name.upper()) #its covert all letter into upper case
print(name.lower()) #its convert all letter into lower case
print(name.find("is")) #its find "is" letter in staterment
print(name.replace("is","are"))#its replace word with new one