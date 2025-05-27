#!/usr/bin/env python3
import numpy as np
from classdisc import disk
#Calculo de la nueva velocidad como Vectores:
def newVelocityVector(Disc1,Disc2):
    #Se obtienen las rapideces de los vectores velocidad de cada disco y sus masas.
    V1=np.linalg.norm(Disc1.velocity)
    V2=np.linalg.norm(Disc2.velocity)
    mass1=Disc1.mass
    mass2=Disc2.mass
    
    #Se obtienen las nuevas velocidades de cada vector.
    V1f= (V1*(mass1-mass2)+2*mass2*V2)/(mass1+mass2)
    V2f= (V2*(mass2-mass1)+2*mass1*V1)/(mass1+mass2)
    
    #Finalmente, se rota el vector con la transformación: [[0,-1],[-1,0]].Luego se asignan los valores de las nuevas velocidades al disco respectivo.
    Disc1.velocity=np.array([(-1*Disc1.velocity[1]/V1)*V1f,(-1*Disc1.velocity[0]/V1)*V1f])
    Disc2.velocity=np.array([(-1*Disc2.velocity[1]/V2)*V2f,(-1*Disc2.velocity[0]/V2)*V2f])
    return 0
    
#Calculo de la nueva velocidad como polares:
def newVelocityPolar(Disc1,Disc2):
    #Se obtienen los vectores polares de los discos (definidos en la clase) junto con sus masas.
    V1=Disc1.polar_velocity
    V2=Disc2.polar_velocity
    mass1=Disc1.mass
    mass2=Disc2.mass
    #Se calculan las nuevas rapideces de los discos.
    V1f= (V1[0]*(mass1-mass2)+2*mass2*V2[0])/(mass1+mass2)
    V2f= (V2[0]*(mass2-mass1)+2*mass1*V1[0])/(mass1+mass2)
    #Se forma el nuevo vector polar.
    newPolar1=(V1f,(np.pi/2)-V1[1])
    newPolar2=(V2f,(np.pi/2)-V2[1])
    #Se asignan los nuevos vectores a sus respetivos discos.
    Disc1.polar_velocity=newPolar1
    Disc2.polar_velocity=newPolar2
    Disc1.velocity=-1*Disc1.velocity
    Disc2.velocity=-1*Disc2.velocity
    return 0
    
#Prueba: Se porbaran ambos metodos con dos discos DiscA y DiscB.
DiscA = disk(positionx=0.5,positiony=0.5,speedx=-5,speedy=4,radious=0.3,mass=5)
DiscB = disk(positionx=0.9,positiony=0.6,speedx=8,speedy=1,radious=0.3,mass=2)
print(f"DiscA: {DiscA.velocity}")
print(f"DiscB: {DiscB.velocity}")
newVelocityPolar(DiscA,DiscB)
print(f"New DiscA polar: {DiscA.velocity}")
print(f"New DiscB polar: {DiscB.velocity}")

#Los llamo DiscC y DiscD pero son los mismos DiscA y DiscB originales.
DiscC = disk(positionx=0.5,positiony=0.5,speedx=-5,speedy=4,radious=0.3,mass=5)
DiscD = disk(positionx=0.9,positiony=0.6,speedx=8,speedy=1,radious=0.3,mass=2)
print(f"DiscA: {DiscC.velocity}")
print(f"DiscB: {DiscD.velocity}")
newVelocityVector(DiscC,DiscD)
print(f"New DiscA Vector: {DiscC.velocity}")
print(f"New DiscB Vector: {DiscD.velocity}")
#Vector es mucho más precisa que Polar.
