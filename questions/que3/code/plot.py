#Program to plot  the tangent of a parabola
#Code by GVV Sharma
#Released under GNU GPL
#August 19, 2024

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/ramaraogolla/Desktop/EE1030/matgeo/codes/CoordGeo')        #path to my scripts


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
num = 100


V = np.array(([0, 0], [0, 1]))
u = np.array(([-4, 0])).reshape(-1, 1)
f = 0


n = np.array(([4, 0])).reshape(-1, 1)
c1 = 0
c2 = 10


m, h = param_norm(n, c1)
A, B = chord(V, u, f, m, h)
m, h = param_norm(n, c2)
C, D = chord(V, u, f, m, h)


A = A.reshape(2, 1)
B = B.reshape(2, 1)
C = C.reshape(2, 1)
D = D.reshape(2, 1)


y = np.linspace(-np.sqrt(8 * 8), np.sqrt(8 * 8), num)


flen = 8
x = parab_gen(y, flen)

xStandard = np.block([[x], [y]])


plt.plot(xStandard[0, :], xStandard[1, :], label='Parabola: $y^2 = 4ax$', color='r')

# Filling the area between the parabola and the x-axis from x=0 to x=8
plt.fill_between(xStandard[0, :], xStandard[1, :], where=(xStandard[0, :] >= 0) & (xStandard[0, :] <= 8),
                 color='cyan', alpha=0.5, label='Area')


A = np.array([8, -8])
B = np.array([8, 8])

# Extract x and y coordinates
x_values = [A[0], B[0]]
y_values = [A[1], B[1]]

# Plot the line
plt.plot(x_values, y_values, label='x = 4a', color='b')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# Display the plot
plt.show()
