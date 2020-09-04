# numpy provide trigonometric ufunc sin(), cos(), tan()
# that takes values in radians and produce corresponding sin, cos, tan values
import numpy as np
x = np.sin(np.pi/2)            # np.sin function does operation sin() on values in array
print(x)

y = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
z = np.sin(y)                  # putting whole array in sin() function
print(z)

a = np.array([360, 540, 720, 900])
b = np.deg2rad(a)                      # converting degree values to radian
print(b)

c = np.array([1, 2, 3, 4])
d = np.rad2deg(c)                      # converting radian values to degree
print(d)

e = np.array([1.0, 0.1, 1, -1])                     # converting sin, cos, tan values into radian values
f = np.arcsin(e)
print(f)

base = 3
perp = 4
h = np.hypot(base, perp)                     # finding hypotenuse length of pythagoras triangle
print(h)
