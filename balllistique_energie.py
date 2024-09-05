#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:10:22 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt

### composantes des forces

def f1(xp , yp): ##compo en x
    return - (ETA/MASSE)*xp
   
def f2(xp, yp) :  ##compo en y
    return - (ETA/MASSE)*yp - g

def energiec(xp, yp):
    ecx = 0.5*MASSE*xp**2
    ecy = 0.5*MASSE*yp**2
    return ecx, ecy

def energiep(x, y):
    epx =  MASSE*g*x
    epy =  MASSE*g*y
    return epx, epy

def energietot(xp, yp, x, y) :
    ecx, ecy = energiec(xp, yp)
    epx , epy = energiep(x,y)
    etotx = ecx + epx
    etoty = ecy + epy
    return etotx, etoty
   


### constantes et conditions initiales

v0 = 70 #m/s

DT = 0.001

g = 9.83 #m/s2

MASSE = 1#kg

Lambda = 0.001

ETA  = 0.01

Theta = np.pi/4

n1 = 0

n2 = 0

n3 = 0

n4 = 0
###fonction initialisation

def initialisation():
    y = 0 #y à t = 0
   
    x = 0#x à t = 0 
   
    xp = v0*np.cos(Theta)
   
    yp = v0*np.sin(Theta)
   
    return x, y, xp, yp

x , y, xp, yp = initialisation()

ecx, ecy = energiec(xp,yp)
epx, epy = energiep(x, y)
etotx , etoty = energietot(xp, yp, x, y)



x_tab_rk2 = np.array([x])

y_tab_rk2 = np.array([y])

xp_tab_rk2 = np.array([xp])

yp_tab_rk2 = np.array([yp])

ecx_tab = np.array([ecx])

ecy_tab = np.array([ecy])

epx_tab = np.array([epx])

epy_tab = np.array([epy])

etotx_tab = np.array([etotx])

etoty_tab = np.array([etoty])


def rk2(dt, x, y, xp, yp):
    k1p =  f1(xp, yp)*DT
    k1x =  xp*DT
    k1q =  f2(xp, yp)*DT
    k1y =  yp*DT
   
    k2p = f1(xp + 0.5*k1p, yp +0.5*k1q)*DT
    k2x = xp*DT + 0.5*k1p*DT
    k2q = f2(xp + 0.5*k1p, yp +0.5*k1q)*DT
    k2y = yp*DT + 0.5*k1q*DT
   
    xp1 = xp + k2p
    x1 = x + k2x
    yp1 = yp + k2q
    y1 = y + k2y
   
    return np.array([x1, y1, xp1, yp1])




while y >= 0 :
    x, y, xp, yp = rk2(DT, x , y , xp , yp)
   
   
    x_tab_rk2  = np.append(x_tab_rk2, x)
    y_tab_rk2  = np.append(y_tab_rk2, y)
    xp_tab_rk2  = np.append(xp_tab_rk2, xp)
    yp_tab_rk2  = np.append(yp_tab_rk2, yp)  
   
    ecx, ecy = energiec(xp,yp)
    epx, epy = energiep(x, y)
    etotx , etoty = energietot(xp, yp, x, y)
   
    ecx_tab = np.append(ecx_tab, ecx)
    ecy_tab = np.append(ecy_tab, ecy)
    epx_tab = np.append(epx_tab, epx)
    epy_tab = np.append(epy_tab, epy)
    etotx_tab = np.append(etotx_tab, etotx)
    etoty_tab = np.append(etoty_tab, etoty)
   
   
plt.figure()
plt.plot(x_tab_rk2,y_tab_rk2, "black", label= "MVT")
plt.plot(ecx_tab,ecy_tab, "red", label= "energie cinétique")
plt.plot(epx_tab,epy_tab, "blue", label = "energie potentiel")
plt.plot(etotx_tab,etoty_tab, "purple", label = "energie total" ) 
plt.title("Etude energétique du systeme")
plt.legend()
plt.show()