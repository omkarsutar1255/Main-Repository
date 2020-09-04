import turtle
import time
j = turtle.Turtle()
a = turtle.Screen()
j.hideturtle()
hr = time.localtime().tm_hour       # for getting hour from time
min = time.localtime().tm_min
sec = time.localtime().tm_sec
a.bgcolor("black")
j.color("Green")
while True:
    time.sleep(1)
    j.clear()                             # to clear screen after every iteration
    j.write(str(hr).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2), align="center", font=("Arial", 72, "bold"))
    sec += 1                              # zfill() convert number from single digit to multiple digit
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        hr += 1
        min = 0
    if hr == 13:
        hr += 1
turtle.mainloop()
