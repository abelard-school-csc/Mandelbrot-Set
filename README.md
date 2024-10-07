# Mandelbrot Set Visualization

This project generates a visualization of the Mandelbrot set using Python, NumPy, and Matplotlib. The Mandelbrot set is a famous fractal defined by a simple iterative equation, and its visual representation reveals intricate patterns.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [License](#license)

## Introduction

The Mandelbrot set is defined in the complex plane and consists of points that do not escape to infinity under iteration of the function:

\[ Z_{n+1} = Z_n^2 + C \]

where \( C \) is a complex number. This project calculates the set and visualizes it using a color map to represent the number of iterations required for points to escape.

## Requirements

To run this project, you will need:

- Python 3.x
- NumPy
- Matplotlib

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## Installation

1. Clone the repository:

   ```bash
   git clone <link-to-your-repo>
   ```

2. Navigate to the project directory:

   ```bash
   cd mandelbrot-set
   ```

## Usage

Run the script to generate the Mandelbrot set image:

```bash
python mandelbrot.py
```

This will create a file named `mandelbrot_set.png` in the same directory.

### Parameters

You can adjust the following parameters in the script:

- `width` and `height`: Dimensions of the output image.
- `x_min`, `x_max`, `y_min`, `y_max`: The bounds of the complex plane to visualize.
- `max_iter`: The maximum number of iterations to determine whether a point escapes.

## Output

The script will produce an image file named `mandelbrot_set.png`. The image shows the Mandelbrot set with a color map indicating the number of iterations for each point to escape.

![Mandelbrot Set Example](output_example.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
