#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:09:40 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt

### composantes des forces

def f1(xp , yp): ##compo en x
    return - (ETA/MASSE)*xp
   
def f2(xp, yp) :  ##compo en y
    return - (ETA/MASSE)*yp - g


### constantes et conditions initiales

v0 = 70 #m/s

DT = 0.001

g = 9.83 #m/s2

MASSE = 1#kg

Lambda = 0.001

ETA  = 0.01

Theta = np.pi/4

###fonction initialisation

def initialisation():
    y = 0 #y à t = 0
   
    x = 0#x à t = 0 
   
    xp = v0*np.cos(Theta)
   
    yp = v0*np.sin(Theta)    
   
    return x, y, xp, yp

x , y, xp, yp = initialisation()

###euler

x_tab_euler1 = np.array([x])

y_tab_euler1 = np.array([y])

xp_tab_euler1 = np.array([xp])

yp_tab_euler1 = np.array([yp])

def euler(dt, x, y, xp, yp): #xp1 yp1, xp et yp a l'instant t+1
    xp1 = xp + f1(xp, yp)*DT
    x1 = x + xp*DT
    yp1 = yp + f2(xp, yp)*DT
    y1 = y + yp*DT
    return np.array([x1, y1, xp1, yp1])

###euler cromer

x_tab_eulerc1 = np.array([x])

y_tab_eulerc1 = np.array([y])
xp_tab_eulerc1 = np.array([xp])
yp_tab_eulerc1 = np.array([yp])

def euler_cromer(dt, x, y, xp, yp): #xp1 yp1, xp et yp a l'instant t+1
    xp1 = xp + f1(xp, yp)*DT
    x1 = x + xp1*DT
    yp1 = yp + f2(xp, yp)*DT
    y1 = y + yp1*DT
    return np.array([x1, y1, xp1, yp1])

### runge kutta 2

x_tab_rk2 = np.array([x])
y_tab_rk2 = np.array([y])
xp_tab_rk2 = np.array([xp])
yp_tab_rk2 = np.array([yp])


## Incrémentation eta = 0.01

initialisation()

while y >= 0 :
    x, y, xp, yp = euler(DT, x , y , xp , yp)
    x_tab_euler1  = np.append(x_tab_euler1, x)
    y_tab_euler1  = np.append(y_tab_euler1, y)
    xp_tab_euler1  = np.append(xp_tab_euler1, xp)
    yp_tab_euler1  = np.append(yp_tab_euler1, yp)
 
x , y, xp, yp = initialisation()
      
while y >= 0 :
    x, y, xp, yp = euler_cromer(DT, x , y , xp , yp)
    x_tab_eulerc1  = np.append(x_tab_eulerc1, x)
    y_tab_eulerc1  = np.append(y_tab_eulerc1, y)
    xp_tab_eulerc1  = np.append(xp_tab_eulerc1, xp)
    yp_tab_eulerc1  = np.append(yp_tab_eulerc1, yp)

x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = rk2(DT, x , y , xp , yp)
    x_tab_rk21  = np.append(x_tab_rk21, x)
    y_tab_rk21  = np.append(y_tab_rk21, y)
    xp_tab_rk21  = np.append(xp_tab_rk21, xp)
    yp_tab_rk21  = np.append(yp_tab_rk21, yp)   
   
 ## Incrémentation eta = 0.0  
  
ETA  = 0.0

x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = euler(DT, x , y , xp , yp)
    x_tab_euler2  = np.append(x_tab_euler2, x)
    y_tab_euler2  = np.append(y_tab_euler2, y)
    xp_tab_euler2  = np.append(xp_tab_euler2, xp)
    yp_tab_euler2  = np.append(yp_tab_euler2, yp)
 
x , y, xp, yp = initialisation()
      
while y >= 0 :
    x, y, xp, yp = euler_cromer(DT, x , y , xp , yp)
    x_tab_eulerc2  = np.append(x_tab_eulerc2, x)
    y_tab_eulerc2  = np.append(y_tab_eulerc2, y)
    xp_tab_eulerc2  = np.append(xp_tab_eulerc2, xp)
    yp_tab_eulerc2  = np.append(yp_tab_eulerc2, yp)

x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = rk2(DT, x , y , xp , yp)
    x_tab_rk22  = np.append(x_tab_rk22, x)
    y_tab_rk22  = np.append(y_tab_rk22, y)
    xp_tab_rk22  = np.append(xp_tab_rk22, xp)
    yp_tab_rk22  = np.append(yp_tab_rk22, yp)   



#2pi rad equals 360 degrees
#1degrés = pi/180

x , y, xp, yp = initialisation()

tab_rk2_impact = np.array([])
n = 0
Theta = 0

for i in np.arange(0,10):
    while y >= 0 :
        x, y, xp, yp = rk2(DT, x , y , xp , yp)
        x_tab_rk2  = np.append(x_tab_rk2, x)
        y_tab_rk2  = np.append(y_tab_rk2, y)
        xp_tab_rk2  = np.append(xp_tab_rk2, xp)
        yp_tab_rk2  = np.append(yp_tab_rk2, yp)  
    tab_rk2_impact = np.append(tab_rk2_impact,x_tab_rk2[-1])
    Theta += np.pi/180
    x , y, xp, yp = initialisation()
   

print(Theta*2*np.pi) #=?180degres 
   
 ###plot

plt.figure()
plt.plot(tab_rk2_impact,np.arange(0,10), "red")
plt.title("equation du mouvement avec rk2 pour Theta de 0 à 2pi")
plt.xlabel("Theta")
plt.ylabel("Point d'impact")
plt.show()  
