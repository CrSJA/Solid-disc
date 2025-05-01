#!/usr/env python3

import numpy as np


def VecVelocidad(velocidad,angulo):
    VelocidadX= velocidad*np.cos(angulo)
    VelocidadY= velocidad*np.sin(angulo)
    return np.array([VelocidadX,VelocidadY])

def colision(VectorV,angulo):
    #Muy bien como la magnitud del momento no cambia, el vector V solo cambia de dirección, por lo que se ocupa solamente cambiar esto tras la colisión.Esto se logra con esta matriz de transformación
    Tmatrix = np.array([np.cos(np.pi -2*angulo),-1*np.sin(np.pi -2*angulo),np.sin(np.pi -2*angulo),np.cos(np.pi -2*angulo)])
    VectorV[0]= VectorV[0]*Tmatrix[0]+VectorV[1]*Tmatrix[1]
    VectorV[1]= VectorV[0]*Tmatrix[2]+VectorV[1]*Tmatrix[3]
    return VectorV

#Pruba1:

Vector= VecVelocidad(0.5 , np.pi/4)

print(colision(Vector, np.pi/4))
