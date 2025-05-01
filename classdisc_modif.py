import numpy as np

class disk ():
    def __init__(self):
        self.position=np.zeros(2)
        self.speed=0 # Aqui modifique esta parte solamente para que la velocidad sea un escalar, creo que nos conviene más.
        self.radious=1
        self.angle=0 # Agregue un nuevo parametro, que es el angulo de inclinaacion del vector velocidad respecto a la base del cuadrado.




    def is_coliding_whit_another(self,another): # comprueva si hay colisiones con otro circulo
        if (self.radious + another.radious)**2 < np.dot(self.position,another.position):

            return True
        return False
    
    def time_until_colision_with_another(self,another): 
        pass

