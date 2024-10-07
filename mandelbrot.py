import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

matplotlib.use('Agg')

width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0
max_iter = 256

x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

Z = np.zeros_like(C, dtype=np.complex128)
mandelbrot_set = np.zeros(C.shape, dtype=np.float32)

for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]
    mandelbrot_set[mask] = i

plt.figure(figsize=(8, 8))
plt.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='inferno', interpolation='bilinear')
plt.colorbar(label='Iterations to escape')
plt.title("Mandelbrot Set")
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')

if args.show:
    plt.show()
else:
    plt.savefig('mandelbrot_set.png')
    plt.close()
