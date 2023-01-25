import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_grass():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    grass = f.generate()
    # Add noise to the fractal shape to make it look more like grass
    noise = np.random.normal(0, 0.05, grass.shape)
    grass = grass + noise
    grass = np.clip(grass, 0, 1)
    # Apply a grass-like color map to the fractal shape
    grass = plt.cm.Greens(grass)
    # Return the fractal grass
    return grass

# Generate 10 fractal grass images
for i in range(10):
    grass = generate_fractal_grass()
    plt.imsave("fractal_grass_{}.png".format(i), grass)
