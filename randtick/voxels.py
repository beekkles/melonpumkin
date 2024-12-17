# voxels.py
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

def generate_animation(axes, num_randoms, color_list, save_as_gif=False):
    data = np.zeros(axes, dtype=np.bool)
    alpha = 0.9

    # Inicializa la matriz de colores con 4 componentes (RGB + alpha) por cada voxel
    colors = np.zeros(axes + [4], dtype=np.float32)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        nonlocal data, colors

        # Limpia los datos anteriores para mostrar solo el cubo nuevo en cada fotograma
        data.fill(0)
        colors.fill(0)  # Esto ahora llena la matriz con ceros (transparente)

        for _ in range(num_randoms):
            random_x_start = random.randint(0, axes[0] - 2)
            random_y_start = random.randint(0, axes[1] - 2)
            random_z_start = random.randint(0, axes[2] - 2)

            random_color = color_list[random.randint(0, len(color_list)-1)]

            # Marca el cubo 2x2x2 en el lugar aleatorio
            data[random_x_start:random_x_start+2, 
                 random_y_start:random_y_start+2, 
                 random_z_start:random_z_start+2] = 1

            colors[random_x_start:random_x_start+2, 
                   random_y_start:random_y_start+2, 
                   random_z_start:random_z_start+2] = np.append(random_color, alpha)

        ax.cla()  # Limpia el gráfico anterior
        ax.set_box_aspect([1, 1, 1])  # Asegura la proporción 1:1:1
        ax.set_xlim(0, axes[0])
        ax.set_ylim(0, axes[1])
        ax.set_zlim(0, axes[2])

        ax.voxels(data, facecolors=colors)

        return ax

    # Crea la animación
    ani = FuncAnimation(fig, update, frames=30, interval=500, repeat=False)

    if save_as_gif:
        ani.save('random_cubes.gif', writer='imagemagick', fps=2)

    plt.show()
