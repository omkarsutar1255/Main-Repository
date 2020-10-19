import datetime
start_time = datetime.datetime.now()
number = [4, 5, 8, 9]
total = 0
for num in number:
    total = total + num
print("total is: ", total)
ex = datetime.datetime.now()-start_time
print("time taken = ", ex.total_seconds()*1000)
