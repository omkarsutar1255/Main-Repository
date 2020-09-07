# =========== Canvas Widget ===============
from tkinter import *
root = Tk()
canvas_width = 1000
canvas_height = 600
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget =Canvas(root, width=canvas_width, height=canvas_height, bg='grey')
# creating widget for canvas giving height and width with background color grey
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 1000, 600, fill="red")
can_widget.create_line(0, 600, 1000, 0, fill="blue")

# to create rectangle give top left and bottom right points
can_widget.create_rectangle(20, 20, 400, 300, fill="green", outline='green')

# creating text by specifying center position of text in gui
can_widget.create_text(200, 200, text="python")

# take rectangle coordinates and then create oval in that rectangle
can_widget.create_oval(200, 200, 800, 400)

can_widget.create_arc(100, 200, 300, 800, extent=30)
# creating arc giving two points to it and angle as extent

photo = PhotoImage(file='C:\\Users\\dell\\Omkar Programme\\Python Files\\imgae.png')
can_widget.create_image(30, 20, image=photo, anchor=NW)    # while adding photo to widget give position in x-y direction
# and give direction in anchor for show which part of photo should display

points = [250, 110, 490, 200, 280, 280, 200, 200]     # four times x y values so create rectangle
can_widget.create_polygon(points, fill='green', outline='red', width=3)      # here width is broadness of outline
# create polygon of any shape like rectangle, triangle, hexagonal, pentagon

root.mainloop()
