grocery = ("harpic", "vim bar", "deodrant", "bhindi","lollypop", 56)
print(grocery[2])

number = [4,6,24,6,45,5,234,6]
number.sort() #for sorting number
number.reverse() #for reverse number
print(max(number)) #for max number
print(min(number)) #for min number
number.append(43) #paste that number at end
print(number)

number = [4,6,24,6,45,5,234,6]
number.insert(3,111) #insert number at any position
number.remove(234) #remove any number
number.pop() #remove last number
print(number)

number = [4,6,24,6,45,5,234,6]
number[1]=98 #replace value by putting its position
print(number)

#mutable - can change
#immutable - cannot change

tp = (1,2,3)
# tupple are in the paranthisis() bracket
print(tp)

tp=(1,) #comma
print(tp)

a=1
b=3
a,b = b,a #swapping number
print(a,b)