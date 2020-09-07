import time
initial = time.time()        # start time
k=0
while(k<45):
    print("This is omkar")
    time.sleep(1)               # stop program for defined time
    k+=1
print("while loop take", time.time() - initial, "time")         # stop time - start time = run time
initial2 = time.time()                         # start time
for i in range(45):
    print("This is omkar")
print("for loop take", time.time() - initial2, "time")          # stop time - start time = run time

local = time.asctime()
print(local)