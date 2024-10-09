import ctypes
import numpy as np
import matplotlib.pyplot as plt


lib = ctypes.CDLL('./libgeometry.so')


lib.parabola_gen.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.parabola_gen.restype = None

lib.get_line.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.get_line.restype = None


NUM = 100
y_array = (ctypes.c_double * NUM)()
x_array = (ctypes.c_double * NUM)()


lib.parabola_gen(y_array, x_array, ctypes.c_double(8))

y_points = np.array(list(y_array))
x_points = np.array(list(x_array))

plt.plot(x_points, y_points, label='Parabola: $y^2 = 8x$', color='r')


A = (ctypes.c_double * 2)()
B = (ctypes.c_double * 2)()


lib.get_line(A, B)


A_np = np.array([A[0], A[1]])
B_np = np.array([B[0], B[1]])


plt.plot([A_np[0], B_np[0]], [A_np[1], B_np[1]], label='x = 4a', color='b')


plt.fill_between(x_points, y_points, where=(x_points > 0) & (x_points <= 8.0001), color='cyan', alpha=0.5, label='Area')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.title('Corrected Parabola and Line Plot')


plt.show()

