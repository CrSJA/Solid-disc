import numpy as np

class disk ():
    def __init__(self):
        self.position=np.zeros(2)
        self.speed=np.zeros(2)
        self.radious=1




    def is_coliding_whit_another(self,another): # comprueva si hay colisiones con otro circulo
        if (self.radious + another.radious)**2 < np.dot(self.position,another.position):

            return True
        return False
    
    def time_until_colision_with_another(self,another): 
        pass

