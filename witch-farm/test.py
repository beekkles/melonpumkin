import numpy as np
import matplotlib.pyplot as plt

boat_size = 44
pressure_plate_size = 30
velocity = 14
tick_time = 1
# Coordenadas iniciales
boat_position = 0
pressure_plate_position = 100
channel_length = 200

total_ticks = 50

positions = []
activations = []

# Simulación
for tick in range(total_ticks):
    # Mover el bote
    boat_position += velocity
    
    # Registrar posición
    positions.append(boat_position)
    
    # Comprobar activación de la placa
    if (
        pressure_plate_position <= boat_position <= pressure_plate_position + pressure_plate_size
    ):
        activations.append(1)  # Placa activada
    else:
        activations.append(0)  # Placa desactivada
    
    # Reiniciar posición si se sale del canal
    if boat_position >= channel_length:
        boat_position = 0

# Graficar resultados
ticks = np.arange(total_ticks)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(ticks, positions, label="Posición del bote")
plt.axhline(y=pressure_plate_position, color="red", linestyle="--", label="Placa de presión")
plt.axhline(
    y=pressure_plate_position + pressure_plate_size, color="red", linestyle="--", alpha=0.5
)
plt.title("Movimiento del Bote")
plt.xlabel("Ticks")
plt.ylabel("Posición")
plt.legend()

# Gráfica de activación
plt.subplot(2, 1, 2)
plt.step(ticks, activations, where="post", label="Activación de la placa", color="green")
plt.title("Activación de la Placa de Presión")
plt.xlabel("Ticks")
plt.ylabel("Estado (0=Off, 1=On)")
plt.ylim(-0.1, 1.1)
plt.legend()

plt.tight_layout()
plt.show()
