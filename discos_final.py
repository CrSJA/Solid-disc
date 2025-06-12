import numpy as np

#Se cambiaron diferentes parámetros ya que que en pasado solo estaba teniendo
#en cuenta que solo fueran 4 discos, pero la ultima parte dice que se tiene
#que variar con diferentes círculos

from classdisc_final import disk

def generar_discos(n, radio):
    discos = []
    for _ in range(n):
        # Posiciones aleatorias dentro del área segura (sin salirse de la caja)
        x, y = np.random.uniform(0.1, 0.9, size=2)
        # Velocidades aleatorias
        vx, vy = np.random.uniform(-1, 1, size=2)
        disco = disk(positionx=x, positiony=y, speedx=vx, speedy=vy, radious=radio, mass=1)
        discos.append(disco)
    return discos
