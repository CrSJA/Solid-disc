import numpy as np

class disk:

#Se agrega el dtype
    def __init__(self, positionx=0.5, positiony=0.5, speedx=0, speedy=0, radious=0.3, mass=1):
        self.position = np.array([positionx, positiony], dtype=float)
        self.velocity = np.array([speedx, speedy], dtype=float)
        self.radious = radious
        self.mass = mass

#Se agrega el if mag
    @property
    def polar_velocity(self):
        mag = np.linalg.norm(self.velocity)
        if mag == 0:
            return (0, 0)
        angle_radians = np.arccos(self.velocity[0] / mag)
        return (mag, angle_radians)

    @polar_velocity.setter
    def polar_velocity(self, polar_vector):
        self.velocity[0] = polar_vector[0] * np.cos(polar_vector[1])
        self.velocity[1] = polar_vector[0] * np.sin(polar_vector[1])

#Aquí se quitó una parte del código que se llama def polar_position(self)
#Aquí se quitó una parte del código que se llama def polar_position.setter

    def is_colliding_with(self, other):
        distance_squared = np.sum((self.position - other.position) ** 2)
        radii_sum_squared = (self.radious + other.radious) ** 2
        return distance_squared <= radii_sum_squared

#Aquí se modifica la parte de time_until_colision_with_another

    def verificar_colision_con_pared(self, xlim=(0, 1), ylim=(0, 1)):
        if self.position[0] - self.radious <= xlim[0] or self.position[0] + self.radious >= xlim[1]:
            self.velocity[0] *= -1
            self.position[0] = np.clip(self.position[0], xlim[0] + self.radious, xlim[1] - self.radious)
        if self.position[1] - self.radious <= ylim[0] or self.position[1] + self.radious >= ylim[1]:
            self.velocity[1] *= -1
            self.position[1] = np.clip(self.position[1], ylim[0] + self.radious, ylim[1] - self.radious)

#Agrega la función de mover
    def mover(self, dt):
        self.position += self.velocity * dt
    
