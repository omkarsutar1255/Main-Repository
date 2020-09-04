users = ['rohan das', 'shubham', 'skill f', 'omkar sutar']

computer = ['respberry pi', 'android', '100 rs wala computer', 'iphone']

for i in range(0, len(users)):
    template = "Computer used by {} is {}"
    print(template.format(users[i], computer[i]))



# for reverse the list format
users = ['rohan das', 'shubham', 'skill f', 'omkar sutar']

computer = ['respberry pi', 'android', '100 rs wala computer', 'iphone']

for i in range(0, len(users)):
    template = "Computer used by {1} is {0}"
    print(template.format(users[i], computer[i]))
