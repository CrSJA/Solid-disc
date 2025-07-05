
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from discos_final import generar_discos
from velocities import detectar_colisiones_y_actualizar
from classdisc import disk

"""
SIMULACIÓN DE DINÁMICA DE DISCOS CON COLISIONES

Este script principal ejecuta una simulación de:
- Movimiento de discos en un espacio confinado
- Colisiones elásticas entre discos
- Colisiones con las paredes del contenedor

Los parámetros configurables son:
- cantidad_discos: Número de discos en la simulación
- radio_disco: Radio de cada disco
- dt: Paso de tiempo para la simulación
- frames: Número de frames en la animación
"""

cantidad_discos = 50
radio_disco = 0.05
dt = 0.01

discos = generar_discos(n=cantidad_discos, radio=radio_disco)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

def save_xposition(filename="x_positions.csv"): #guarda posicion en x en csv
    """
    Guarda las posiciones en X de todos los discos en un archivo CSV para graficarlas después.
    Args:
    filename (str): Nombre del archivo donde se guardarán las posiciones.
    """
    x_positions = [d.position[0] for d in discos]
    with open(filename, "a") as f:
        line = ",".join(map(str, x_positions))
        f.write(line + "\n")

colors = [np.random.rand(3,) for _ in discos]
patches = [plt.Circle((d.position[0], d.position[1]), d.radious, color=colors[i]) for i, d in enumerate(discos)]
for p in patches:
    ax.add_patch(p)

def actualizar(frame):
    """
    Actualiza el estado de la simulación para cada frame.

    Pasos:
    1. Mueve todos los discos según su velocidad
    2. Verifica colisiones con las paredes
    3. Detecta y procesa colisiones entre discos
    4. Actualiza las posiciones visuales

    Args:
        frame (int): Número del frame actual
    """
    for d in discos:
        d.mover(dt)
        d.verificar_colision_con_pared()
    detectar_colisiones_y_actualizar(discos)

    for i, d in enumerate(discos):
        patches[i].center = d.position[0], d.position[1]
    save_xposition()
    return patches

ani = animation.FuncAnimation(fig, actualizar, frames=500, interval=20, blit=True)
plt.show()

data = np.loadtxt("x_positions.csv", delimiter=",")

# Flatten all x-positions across all saved frames
all_x = data.flatten()

all_x = data.flatten()

# Plot global histogram
plt.hist(all_x, bins=30, color='lightgreen', edgecolor='black')
plt.xlabel("X Position")
plt.ylabel("Total Count (all sampled frames)")
plt.title("Global Histogram of X Positions")
plt.grid(True)
plt.show()