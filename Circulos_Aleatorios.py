from classdisc import disk

# Crear 4 discos con posiciones fijas y velocidades aleatorias
discos = []
for i in range(4):
    # Posiciones fijas
    x = 0.25 if i % 2 == 0 else 0.75
    y = 0.75 if i < 2 else 0.25

    # Velocidades aleatorias entre -0.5 y 0.5
    vx, vy = np.random.uniform(-0.5, 0.5, size=2)

    # Crear el disco
    disco = disk(positionx=x, positiony=y, speedx=vx, speedy=vy, radious=0.1)
    discos.append(disco)

    # Imprimir velocidad de cada disco
    print(f"Disco {i+1} → Velocidad aleatoria: ({vx:.3f}, {vy:.3f})")
