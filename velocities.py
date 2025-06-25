#Basicamente todo el documento se cambió, nada es igual, ya que el programa solo
#toma en cuenta cuando solo dos circulos en específico van a colisionar,
#pero no toma en cuenta cuando los circulos son diferentes o son más de 2 y así
#entonces se cambió la mayoría del código.

import numpy as np
from classdisc import disk

def newVelocityVector(d1, d2):
    """Colisión elástica físicamente correcta entre dos discos"""
    """
    Calcula nuevas velocidades tras colisión elástica entre dos discos.
    
    Args:
        d1 (disk): Primer disco en colisión
        d2 (disk): Segundo disco en colisión
    """
    delta_pos = d1.position - d2.position
    distancia = np.linalg.norm(delta_pos)

    if distancia == 0:
        return  # evitar error

    normal = delta_pos / distancia
    delta_vel = d1.velocity - d2.velocity
    velocidad_relativa = np.dot(delta_vel, normal)

    if velocidad_relativa > 0:
        return  # ya se están separando

    masa_total = d1.mass + d2.mass
    impulso = (2 * velocidad_relativa) / masa_total

    d1.velocity -= (impulso * d2.mass) * normal
    d2.velocity += (impulso * d1.mass) * normal

def separar_discos(d1, d2, margen=1e-3):
    """
    Separa físicamente dos discos tras colisión para evitar superposición.

    Args:
        d1 (disk): Primer disco a separar
        d2 (disk): Segundo disco a separar
        margen (float): Distancia adicional de seguridad (default: 1e-3)
    """


    delta = d1.position - d2.position
    distancia = np.linalg.norm(delta)
    min_distancia = d1.radious + d2.radious + margen

    if distancia == 0:
        direccion = np.random.rand(2) - 0.5
        direccion /= np.linalg.norm(direccion)
    else:
        direccion = delta / distancia

    desplazamiento = (min_distancia - distancia) / 2
    d1.position += direccion * desplazamiento
    d2.position -= direccion * desplazamiento

def detectar_colisiones_y_actualizar(discos):
    """
    Detecta colisiones entre todos los discos y actualiza sus estados.

    Args:
        discos (list): Lista de objetos disk en la simulación
    """
    n = len(discos)
    for i in range(n):
        for j in range(i + 1, n):
            d1 = discos[i]
            d2 = discos[j]
            if d1.is_colliding_with(d2):
                newVelocityVector(d1, d2)
                separar_discos(d1, d2)
