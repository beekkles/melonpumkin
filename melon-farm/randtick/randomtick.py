import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import imageio
import os

def generate_random_cube(axes, color):
    data = np.zeros(axes, dtype=np.bool)
    colors = np.empty(axes + [4], dtype=np.float32)
    colors[:] = [0, 0, 0, 0]
    
    for _ in range(3):
        x = random.randint(0, axes[0] - 1)
        y = random.randint(0, axes[1] - 1)
        z = random.randint(0, axes[2] - 1)

        data[x, y, z] = 1
        colors[x, y, z] = np.append(color, 1.0)  # Opacidad completa

    return data, colors

def plot_voxels(data, colors, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.voxels(data, facecolors=colors)

    ax.set_xlim(0, data.shape[0])
    ax.set_ylim(0, data.shape[1])
    ax.set_zlim(0, data.shape[2])

    ax.set_box_aspect([1, 1, 1])
    ax.set_xticks(np.arange(0, data.shape[0] + 1, 1))
    ax.set_yticks(np.arange(0, data.shape[1] + 1, 1))
    ax.set_zticks(np.arange(0, data.shape[2] + 1, 1))

    plt.savefig(filename)
    plt.close()

def main():
    axes = [16, 16, 16]
    color = [0.7, 0.2, 0.2]
    filenames = []

    for i in range(10):
        data, colors = generate_random_cube(axes, color)
        filename = f'frame_{i}.png'
        plot_voxels(data, colors, filename)
        filenames.append(filename)

    with imageio.get_writer('animation.gif', mode='I', duration=0.5) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    for filename in filenames:
        os.remove(filename)

if __name__ == "__main__":
    main()