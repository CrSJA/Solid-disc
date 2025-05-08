import matplotlib.pyplot as plt
import numpy as np

# Parámetros generales
num_discos = 4
radio = 0.05  # Radio de los discos
dt = 0.01     # Paso de tiempo
time = 100   #Tiempo de la simulación

# Posiciones conocidas (Por ahora son estas tentativas)
posiciones = np.array([
    [0.25, 0.25],
    [0.75, 0.25],
    [0.25, 0.75],
    [0.75, 0.75]
])

# Direcciones aleatorias
ángulos = np.random.uniform(0, 2*np.pi, size=num_discos)

# Magnitudes aleatorias
vel_magnitudes = np.random.uniform(0.1, 0.9, size=num_discos)

# Velocidades = magnitud * dirección
velocidades = vel_magnitudes[:, None] * np.column_stack((np.cos(ángulos), np.sin(ángulos)))

# Colores para cada disco
colores = ['red', 'green', 'blue', 'orange']

# Función para graficar
def graficar(posiciones, step):
    plt.clf()
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    for i in range(num_discos):
        circle = plt.Circle(posiciones[i], radio, color=colores[i])
        ax.add_patch(circle)
        # Flecha de velocidad
        plt.arrow(posiciones[i][0], posiciones[i][1],
                  velocidades[i][0]*0.1, velocidades[i][1]*0.1,
                  head_width=0.01, color='black')
    plt.title(f"t = {step*dt:.2f}")
    plt.pause(0.05)

# Simulación sin colisiones
plt.ion()
for step in range(time):
    posiciones += velocidades * dt
    graficar(posiciones, step)

plt.ioff()
plt.show()

