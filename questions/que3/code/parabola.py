import ctypes
import numpy as np
import matplotlib.pyplot as plt


lib = ctypes.CDLL('./libparabola.so')


class Parabola(ctypes.Structure):
    _fields_ = [("V", ctypes.POINTER(ctypes.POINTER(ctypes.c_double))),
                ("U", ctypes.POINTER(ctypes.c_double)),
                ("f", ctypes.c_double),
                ("rows", ctypes.c_int),
                ("cols", ctypes.c_int),
                ("size", ctypes.c_int)]


lib.createParabola.restype = Parabola
lib.createParabola.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]

lib.calculate_y.restype = ctypes.c_double
lib.calculate_y.argtypes = [ctypes.POINTER(Parabola), ctypes.c_double]

lib.freeParabola.argtypes = [ctypes.POINTER(Parabola)]


vRows = 2
vCols = 2
uSize = 1
f = 0.0
parabola = lib.createParabola(vRows, vCols, uSize, f)


V = parabola.V


V[1][0] = ctypes.c_double(0.0)  
V[1][1] = ctypes.c_double(1.0)

U = parabola.U
U[0] = ctypes.c_double(0.0)


x_values = np.linspace(0, 10, 400)
y_values = [lib.calculate_y(ctypes.byref(parabola), x) for x in x_values]

lib.freeParabola(ctypes.byref(parabola))


plt.figure(figsize=(10, 6))


x_parabola = np.linspace(0, 10, 400)
y_positive = np.sqrt(8 * x_parabola)
y_negative = -np.sqrt(8 * x_parabola)

plt.fill_between(x_parabola[x_parabola <= 8], y_positive[x_parabola <= 8], color='cyan', alpha=0.5, label='Shaded Area')
plt.fill_between(x_parabola[x_parabola <= 8], y_negative[x_parabola <= 8], color='cyan', alpha=0.5)

plt.plot(x_parabola, y_positive, label=r'$y^2 = 4ax$', color='red')
plt.plot(x_parabola, y_negative, color='red')

plt.axvline(x=8, color='blue', label='x = 4a')


plt.title("Plot of the Parabola and Shaded Region")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-15, 15)
plt.xlim(-1, 10)
plt.grid(True)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.show()

