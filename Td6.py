#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:34:24 2022

@author: S18014755
"""

import numpy as np 
import matplotlib.pylab as plt

### composantes des forces 

def f1(xp , yp): ##compo en x
    return - (ETA/MASSE)*xp
    
def f2(xp, yp) :  ##compo en y
    return - (ETA/MASSE)*yp + g


### constantes et conditions initiales

v0 = 70 #m/s

DT = 0.001

g = 9.83 #m/s2

MASSE = 1#kg

Lambda = 0.001

ETA  = 0.01

Teta = np.pi/4

y = 0 #y à t = 0

x = 0 #x à t = 0  

xp = 0

yp = 0

x_tab = np.array([])

y_tab = np.array([])

xp_tab = np.array([])

yp_tab = np.array([])

    
###euler

def euler(dt, x, y, xp, yp): #xp1 yp1, xp et yp a l'instant t+1
    xp1 = xp + f1(xp, yp)*DT
    x1 = x + xp*DT
    yp1 = yp + f2(xp, yp)*DT
    y1 = y + yp*DT
    return np.array([x1, y1, xp1, yp1])


while y >= 0 : 
    y += 1
    x_tab, y_yab, xp_tab, yp_tab = euler(DT, x , y , xp , yp)







