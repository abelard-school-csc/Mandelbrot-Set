# Mandelbrot Set Visualization

## What is the Mandelbrot Set?

The Mandelbrot set is a famous fractal, named after mathematician Benoit Mandelbrot. It is defined as the set of complex numbers `c` for which the function `f(z) = z^2 + c` does not diverge when iterated starting from `z = 0`.

In other words, for each complex number `c`, we iterate the function, checking if the value of `z` escapes to infinity or remains bounded. Points that remain bounded after a large number of iterations belong to the Mandelbrot set, while points that escape are outside of it.

The beauty of the Mandelbrot set comes from its fractal nature: as you zoom in, intricate patterns appear infinitely, with self-similar structures.

## About the Code

This Python script generates a visualization of the Mandelbrot set using the `matplotlib` library. The script follows these key steps:

1. **Grid Generation**: It creates a 2D grid of complex numbers (`C`) that represent points in the complex plane. Each pixel in the image corresponds to a complex number.
2. **Iteration**: For each point `C`, the script iterates the function `Z = Z^2 + C` a maximum number of times (set to `256` iterations by default). The value of `Z` is checked to see if it escapes, defined as having a magnitude greater than `2`.
3. **Escape Times**: The number of iterations before escape (or if the point never escapes) is stored in the `mandelbrot_set` array. This array represents the final image, where points in the Mandelbrot set are colored based on how long it takes them to escape.
4. **Plotting**: The result is visualized using `matplotlib`, where a colormap (`inferno`) is applied to show the escape times in different colors.

### Why This Code Works

- **Correct Iteration**: The key to visualizing the Mandelbrot set is properly iterating the function `Z = Z^2 + C`. This code handles the iteration process efficiently using `numpy` arrays and masks to check escape conditions.

- **Escape Condition**: The escape condition is based on checking the magnitude of `Z`. If it becomes greater than 2, the point is considered to have escaped.

- **Detailed Visualization**: The script generates a detailed, high-resolution visualization of the Mandelbrot set by mapping escape times to colors. This provides a clear depiction of the fractal's intricate boundary and the points that lie inside it.

## How to Run

1. Install the required dependencies:
```bash
pip install numpy matplotlib
```

2. Run the script:
```bash
python mandelbrot.py
```

A window will pop up displaying the Mandelbrot set. You can modify the resolution, number of iterations, and zoom level by adjusting the parameters in the code.

## Customization

- **Resolution**: Modify the `width` and `height` variables to change the resolution of the image.
- **Zoom**: Adjust the `x_min`, `x_max`, `y_min`, and `y_max` variables to zoom in or out on different regions of the complex plane.
- **Iterations**: Change the `max_iter` variable to control the maximum number of iterations.

## Example Output

The output of the script looks like this:

![Mandelbrot Set Visualization](output_example.png)

Enjoy exploring the infinite beauty of the Mandelbrot set!
