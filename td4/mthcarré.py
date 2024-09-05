#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:58:39 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pyplot as plt

xmin = 0
xmax = 3*np.pi/2
nbx = 20
nbi = nbx - 1 # nombre d'intervalles

x = np.linspace(xmin, xmax, nbx)
y = np.cos(x)



# méthode d'intégration des carré : 
    
def carre1(x, y):
    integrale1 = 0
    for i in range(nbi):
        integrale1 = integrale1 + y[i]*(x[i+1]-x[i])               
    return integrale1





# dessin du rectangle



x_rect = np.array([])
y_rect = np.array([])  

for i in range(nbi):
    x_rect = np.append(x_rect,[x[i], x[i], x[i+1], x[i+1], x[i]])  # abscisses des sommets
    y_rect = np.append(y_rect, [0, y[i], y[i], 0, 0])  # ordonnees des sommets       


print("integrale1 =", carre1(x, y), "x y  rectangle = ", x_rect , y_rect)  # abscisses des sommets

plt.plot(x,y,"bo-")
# plt.plot(x_rect, y_rect, "black")


def carré():montecarlo(x1,y2)
    x_rect2 = np.array([])
    y_rect2 = np.array([])  

    for i in range(nbi):
        x_rect2 = np.append(x_rect2,[x[i], x[i], x[i+1], x[i+1], x[i]])  # abscisses des sommets
        y_rect2 = np.append(y_rect2, [0, y[i], y[i], 0, 0])  # ordonnees des sommets     
    return x_rect2, y_rect2

x_rect2, y_rect2 = carré()

plt.plot(x_rect2, y_rect2, "cyan")
plt.show()



