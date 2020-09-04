# ==========CREATING SKY IN TURTLE==========
import turtle
import random
om = turtle.Turtle()
a = turtle.Screen()
a.bgcolor('black')
om.hideturtle()
om.speed(0)
om.color('white')
for i in range(50):
    x = random.randint(-670, 670)
    y = random.randint(-330, 330)
    om.up()
    om.goto(x, y)
    om.down()
    om.begin_fill()
    for x in range(5):
        om.fd(3)
        om.rt(144)
    om.end_fill()

om2 = turtle.Turtle()            # we can create many turtle to draw
om2.write("Omkar Sutar", move=True, align="center", font=("Ink Free", 18, "bold"))
# write - it allows us to write text, move - if true turtle will move as text written
# align - it take values for position of turtle after text wrote
# font - it take style of text, size of text, shape of text(normal, bold)

# we can create many shapes at same time using many turtle

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

# we can do graphical clock, chess board, night sky, stop watch, cube, virus shapes, square shapes patterns++

