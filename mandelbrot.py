import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0
max_iter = 256  # Maximum iterations for determining escape

x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)

# Create a grid of complex numbers C
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

Z = np.zeros_like(C, dtype=np.complex128) # Initialize Z with the same shape as C to store iteration results, using complex128 for complex number operations
mandelbrot_set = np.zeros(C.shape, dtype=np.float32)

for i in range(max_iter):
    mask = np.abs(Z) <= 2 # Identify points that haven't escaped
    Z[mask] = Z[mask]**2 + C[mask] # Update Z for these points
    mandelbrot_set[mask] = i # Record the iteration count for points that haven't escaped

plt.figure(figsize=(8, 8))
plt.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='inferno', interpolation='bilinear')
plt.colorbar(label='Iterations to escape')  
plt.title("Mandelbrot Set")
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')

plt.savefig('mandelbrot_set.png') 
plt.close() 