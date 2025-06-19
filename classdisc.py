import numpy as np

class disk:
    """
    Representa un disco en la simulación con propiedades físicas.

    Attributes:
        position (ndarray): Vector posición [x, y] del centro del disco
        velocity (ndarray): Vector velocidad [vx, vy] del disco
        radious (float): Radio del disco
        mass (float): Masa del disco (afecta colisiones)
    """

#Se agrega el dtype
    def __init__(self, positionx=0.5, positiony=0.5, speedx=0, speedy=0, radious=0.3, mass=1):
        """
        Inicializa un disco con posición, velocidad, radio y masa.

        Args:
            positionx (float): Coordenada x inicial (default: 0.5)
            positiony (float): Coordenada y inicial (default: 0.5)
            speedx (float): Velocidad inicial en x (default: 0)
            speedy (float): Velocidad inicial en y (default: 0)
            radious (float): Radio del disco (default: 0.3)
            mass (float): Masa del disco (default: 1)
        """
        self.position = np.array([positionx, positiony], dtype=float)
        self.velocity = np.array([speedx, speedy], dtype=float)
        self.radious = radious
        self.mass = mass

#Se agrega el if mag
    @property
    def polar_velocity(self):
        """
        Calcula la velocidad en coordenadas polares (magnitud, ángulo).

        Returns:
            tuple: (magnitud, ángulo_en_radianes)
        """
        mag = np.linalg.norm(self.velocity)
        if mag == 0:
            return (0, 0)
        angle_radians = np.arccos(self.velocity[0] / mag)
        return (mag, angle_radians)

    @polar_velocity.setter
    def polar_velocity(self, polar_vector):
        """
        Establece la velocidad usando coordenadas polares.

        Args:
            polar_vector (tuple): (magnitud, ángulo_en_radianes)
        """
        self.velocity[0] = polar_vector[0] * np.cos(polar_vector[1])
        self.velocity[1] = polar_vector[0] * np.sin(polar_vector[1])

#Aquí se quitó una parte del código que se llama def polar_position(self)
#Aquí se quitó una parte del código que se llama def polar_position.setter

    def is_colliding_with(self, other):
        """
        Verifica colisión con otro disco.

        Args:
            other (disk): Otro objeto disco

        Returns:
            bool: True si hay colisión, False en caso contrario
        """
        distance_squared = np.sum((self.position - other.position) ** 2)
        radii_sum_squared = (self.radious + other.radious) ** 2
        return distance_squared <= radii_sum_squared

#Aquí se modifica la parte de time_until_colision_with_another

    def verificar_colision_con_pared(self, xlim=(0, 1), ylim=(0, 1)):
        """
        Detecta y maneja colisiones con las paredes del contenedor.

        Args:
            xlim (tuple): Límites en el eje x (default: (0, 1))
            ylim (tuple): Límites en el eje y (default: (0, 1))
        """
        if self.position[0] - self.radious <= xlim[0] or self.position[0] + self.radious >= xlim[1]:
            self.velocity[0] *= -1
            self.position[0] = np.clip(self.position[0], xlim[0] + self.radious, xlim[1] - self.radious)
        if self.position[1] - self.radious <= ylim[0] or self.position[1] + self.radious >= ylim[1]:
            self.velocity[1] *= -1
            self.position[1] = np.clip(self.position[1], ylim[0] + self.radious, ylim[1] - self.radious)

#Agrega la función de mover
    def mover(self, dt):
        """
        Actualiza la posición del disco según su velocidad y el tiempo transcurrido.

        Args:
            dt (float): Paso de tiempo para la simulación
        """
        self.position += self.velocity * dt
