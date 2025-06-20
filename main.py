import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from discos_final import generar_discos
from velocities import detectar_colisiones_y_actualizar
from classdisc import disk

cantidad_discos = 50
radio_disco = 0.05
dt = 0.01

discos = generar_discos(n=cantidad_discos, radio=radio_disco)


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')


colors = [np.random.rand(3,) for _ in discos]
patches = [plt.Circle((d.position[0], d.position[1]), d.radious, color=colors[i]) for i, d in enumerate(discos)]
for p in patches:
    ax.add_patch(p)

def actualizar(frame):
    for d in discos:
        d.mover(dt)
        d.verificar_colision_con_pared()
    detectar_colisiones_y_actualizar(discos)

    for i, d in enumerate(discos):
        patches[i].center = d.position[0], d.position[1]
    return patches

ani = animation.FuncAnimation(fig, actualizar, frames=500, interval=20, blit=True)
plt.show()
