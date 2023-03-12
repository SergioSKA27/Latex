from sympy import *
from sympy.plotting import plot3d,plot3d_parametric_line,plot3d_parametric_surface
from sympy.plotting.pygletplot import plot_axes
import matplotlib.pyplot as mpl
import math as mt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



x, y,z  = symbols('x,y,z')

expr = x**2*y + x
expr2 = 1/(sin(x+y))
# Create axis
axes = [5, 5, 5]

# Create Data
data = np.ones(axes, dtype=np.bool)

a = plot3d(expr,(x,0,1),(y,0,1),show=False)
a1 = plot3d(expr,(x,0,1),(y,0,0),show=False)
a.append(a1[0])
a.show()
b = plot3d(expr2,(x,0,mt.pi),(y,-mt.pi/2,mt.pi/2))

