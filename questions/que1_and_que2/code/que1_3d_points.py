
#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/ramaraogolla/Desktop/EE1030/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex
#end if

#Given points
A = np.array(([1, -2,1])).reshape(-1,1)
B = np.array(([-2,4, 5])).reshape(-1,1)
C = np.array(([1,-6, -7])).reshape(-1,1)  
D = np.array(([0,-4, -1])).reshape(-1,1)


# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
x_BC = line_gen(B,C)
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)
x_AD= line_gen(A,D)


#Plotting all lines
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],label='$BC$')
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')
ax.plot(x_AD[0,:],x_AD[1,:], x_AD[2,:],label='$AB$')
ax.plot(x_CD[0,:],x_CD[1,:], x_CD[2,:],label='$AB$')



# Scatter plot
colors = np.arange(1,5)  # Example colors
tri_coords = np.block([A, B, C, D])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :],c=colors)
vert_labels = ['A', 'B', 'C','D']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('chapters/12/11/3/6/figs/fig.pdf')
#subprocess.run(shlex.split("termux-open chapters/12/11/3/6/figs/fig.pdf"))
#else
plt.show()
