import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from discos_final import generar_discos
from velocities_final import detectar_colisiones_y_actualizar
from classdisc import disk

"""
SIMULACIÓN DE DINÁMICA DE DISCOS CON COLISIONES

Este script principal ejecuta una simulación de:
- Movimiento de discos en un espacio confinado
- Colisiones elásticas entre discos
- Colisiones con las paredes del contenedor
- Visualización animada con histograma en tiempo real

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


fig, (ax_sim, ax_hist) = plt.subplots(1, 2, figsize=(10, 5))
ax_sim.set_xlim(0, 1)
ax_sim.set_ylim(0, 1)
ax_sim.set_aspect('equal')
ax_sim.set_title("Disc Simulation")

ax_hist.set_xlim(0, 1)  # x ranges from 0 to 1
ax_hist.set_ylim(0, cantidad_discos)  # max possible discs per bin
ax_hist.set_title("X-Position Histogram")
ax_hist.set_xlabel("X Position")
ax_hist.set_ylabel("Count")

def mostrar_histograma():
    """
    Muestra un histograma final de las posiciones en X después de la simulación.
    """
    x_positions = [d.position[0] for d in discos]
    plt.figure()
    plt.hist(x_positions, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('X Position')
    plt.ylabel('Number of Discs')
    plt.title('Histogram of Disc X Positions')
    plt.grid(True)
    plt.show()



colors = [np.random.rand(3,) for _ in discos]
patches = [plt.Circle((d.position[0], d.position[1]), d.radious, color=colors[i]) for i, d in enumerate(discos)]
for p in patches:
    ax_sim.add_patch(p)

def actualizar(frame):
    """
    Actualiza el estado de la simulación para cada frame.

    Pasos:
    1. Mueve todos los discos según su velocidad
    2. Verifica colisiones con las paredes
    3. Detecta y procesa colisiones entre discos
    4. Actualiza las posiciones visuales
    5. Actualiza el histograma cada 10 frames

    Args:
        frame (int): Número del frame actual
    """
    for d in discos:
        d.mover(dt)
        d.verificar_colision_con_pared()
    detectar_colisiones_y_actualizar(discos)

    for i, d in enumerate(discos):
        patches[i].center = d.position[0], d.position[1]
    
    if frame % 10 == 0:
        ax_hist.clear()
        x_positions = [d.position[0] for d in discos]
        ax_hist.hist(x_positions, bins=20, color='skyblue', edgecolor='black')
        ax_hist.set_xlim(0, 1)
        ax_hist.set_ylim(0, cantidad_discos)
        ax_hist.set_title("X-Position Histogram")
        ax_hist.set_xlabel("X Position")
        ax_hist.set_ylabel("Count")
    
    return patches

ani = animation.FuncAnimation(fig, actualizar, frames=500, interval=20, blit=False)
plt.show()
