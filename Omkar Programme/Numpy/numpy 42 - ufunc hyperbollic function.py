# numpy provides ufunc sinh(), cosh(), tanh()
# that takes values in radians and produce corresponding sinh, cosh, tanh values.
import numpy as np

y = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
z = np.cosh(y)                    # cos hyperbolic function
print(z)

h = np.array([1.0, 0.2, 0.3, 0.4])
g = np.arcsinh(h)                            # finding angles from sinh, cosh, tanh values
print(g)
