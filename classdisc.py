import numpy as np

class disk ():
    def __init__(self,positionx=0.5,positiony=0.5,speedx=0,speedy=0,radious=0.3):
        self.position=np.array([positionx,positiony])
        self.velocity=np.array([speedx,speedy])
        self.radious=radious

    @property
    def polar_velocity(self):
        mag=np.linalg.norm(self.velocity)
        angle_radians=np.arccos(self.velocity[0]/mag)
        return (mag,angle_radians) # esto es imutable, si quiere cambiar la propiedad dele una tupla nueva

    @polar_velocity.setter
    def polar_velocity(self,polar_vector):
        self.velocity[0]=polar_vector[0]*np.cos(polar_vector[1])
        self.velocity[1]=polar_vector[0]*np.sin(polar_vector[1])


    @property
    def polar_position(self):
        mag=np.linalg.norm(self.position)
        angle_radians=np.arccos(self.position[0]/mag)
        return (mag,angle_radians) # esto es imutable, si quiere cambiar la propiedad dele una tupla nueva

    @polar_position.setter
    def polar_position(self,polar_vector):
        self.position[0]=polar_vector[0]*np.cos(polar_vector[1])
        self.position[1]=polar_vector[0]*np.sin(polar_vector[1]) # de ser posible no usen hagan todo vectorial y eviten usar las propiedades polares si es posible

    def is_coliding_whit_another(self,another): # comprueva si hay colisiones con otro circulo
        distance_squared = np.sum((self.position-another.position)**2)
        radious_sum_squared = (self.radious + another.radious)**2
        return distance_squared<=radious_sum_squared
    
    def time_until_colision_with_another(self,another): 
        dr=self.position-another.position
        dv=self.velocity-another.velocity
        R=self.radious+another.radious

        a=np.dot(dv,dv)
        b=np.dot(dr,dv)
        c=np.dot(dr,dr)

        discriminant=b**2-4*a*c

        if discriminant < 0 or discriminant == 0:
            return np.infty
        
        sqrt_dsicriminant=np.sqrt(discriminant)

        t1 = (-b -sqrt_dsicriminant) / (2*a)
        t2 = (-b + sqrt_dsicriminant) / (2*a)

        if t1 > 1e-10:
            return t1
        elif t2 > 1e-10:
            return t2
        else: 
            return np.infty
        


