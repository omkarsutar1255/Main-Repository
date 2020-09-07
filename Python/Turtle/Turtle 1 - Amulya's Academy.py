import turtle
omk = turtle.Turtle()
# turtle.done()                      # way to hold screen for turtle designing
# turtle.Screen().exitonclick()      # another way to hold screen at output
omk.shape('turtle')                  # getting pointer in turtle shape
# omk.shape("circle")                  # for getting circle shape for pointer
# omk.shapesize(10)                    # it increase size of pointer
omk.color('red')                     # changing color as red or green
omk.forward(100)                     # forward movement of turtel pen
omk.color('green', 'red')            # green as line color and red as turle color
omk.backward(200)                    # backward movement
turtle.colormode(255)                # set color as 255 before setting rbg color to turtle
turtle.color((120, 40, 50), (80, 90, 100))            # RBG color number for turtle color and line color
# omk.pen(shown, pendown, pencolor, fillcolor, pensize, speed, resizemode, stretchfactor,
#         shearfactor, outline, tilt)        # these much parameter we can give to pen

wn = turtle.Screen()                 # turtle screen set as wn then
wn.bgcolor("green")                  # setting background color for turtle screen
# to set rbg color to background color of screen first set turtle colormode as 255
wn.title("omkar")                    # setting title to turtle screen
wn.bgpic('gif photo.gif')            # setting gif photo to background

omk.setheading(90)                     # turtle change its direction to 90 degree(i.e. north)
omk.setheading(180)                    # turtle not changes its direction from new angle it angles from north direction
omk.fd(-50)                           # -ve number to forward so turtle move backward
omk.bk(50)                            # bk for turtle move backward
omk.lt(45)                            # changing direction to left of turtle from present angle
omk.fd(100)
omk.rt(45)                            # changing direction to right for any degree from present angle
omk.fd(90)

omk.speed(1)                    # speed of turtle between 1 to 10
# fastest: 0, fast: 10, normal: 6,slow: 3, slowest: 1
omk.begin_fill()             # from here it start calculate area to fill color
omk.fillcolor('red')         # color for fill in calculated area
for i in range(4):           # to skip repeated some command
    omk.fd(100)
    omk.rt(90)
omk.end_fill()               # till here it calculate area to fill color
omk.hideturtle()             # to hide turtle while drawing or also at end

omk.circle(-50, extent=180, steps=3)     # negative radius for clockwise direction circle otherwise will anticlockwise
# extent are how much degree circle should draw and step are lines to draw circle (i.e. polygon, hexagon)
omk.reset()                              # to clear screen from what we have drawn

omk.undo()                               # to undo operations
omk.up()                                 # not to draw but move turtle position
omk.goto(10, -100)                       # to giving new position to turtle giving x and y values
omk.down()                               # to drawn again after getting required position
omk.circle(100)

def omkar(a, b, c):
    omk.up()
    omk.goto(a, b)
    omk.down()
    omk.begin_fill()
    omk.fillcolor(c)
    omk.pensize(10)
    omk.circle(50)
    omk.end_fill()
omkar(0, -50, 'green')
omkar(-200, -200, 'red')
omkar(-200, 100, 'blue')
omkar(200, 100, 'orange')
omkar(200, -200, 'yellow')
omk.up()
omk.home()                          # to get back to main position use home

list1 = ['yellow', 'red', 'blue', 'green']
omk.up()
omk.goto(200, 0)
for i in range(4):
    omk.down()
    omk.color(list1[i])            # using for loop retrieving colors from list
    omk.pensize(10)                # that colors are set to pen so we can use diff colors of pen
    omk.circle(100)
    omk.up()
    omk.bk(100)

list2 = ['purple', 'red', 'orange', 'blue', 'green']
omk.speed(0)
for i in range(100):
    omk.color(list2[i % 5])           # to get 0 to 5 number for 200 times
    omk.pensize(i/5)                  # pensize are depend on loop value
    omk.forward(i + 10)               # forward motion are set to loop value
    omk.left(30)                      # angles are imp

# we can draw nation flag, heart shape, etc. on turtle
turtle.mainloop()                    # good way to hold screen at output
