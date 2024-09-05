#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:59:31 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt

###données

tab_x, tab_y = np.loadtxt("points2.dat",skiprows=0,unpack=True)

N = len( tab_x)

###Somme, det et coeff


Sx = np.sum(tab_x)
Sy = np.sum(tab_y)
S2x = np.sum(tab_x**2)
S3x = np.sum(tab_x**3)
S4x = np.sum(tab_x**4)
Sxy = np.sum(tab_x*tab_y)
S2xy = np.sum((tab_x**2)*tab_y)

Det = N*(S2x*S4x-(S3x)**2)-Sx*(Sx*S4x-S3x*S2x)+S2x*(Sx*S3x-(S2x)**2)

a = (1/Det)*(N*(S2x*S2xy-Sxy*S3x)-Sx*(Sx*S2xy-Sxy*S2x)+Sy*(Sx*S3x-(S2x)**2))
b = (1/Det)*(N*(Sxy*S4x-S3x*S2xy)-Sy*(Sx*S4x-S3x*S2x)+S2x*(Sx*S2xy-S2x*Sxy))
c = (1/Det)*(Sy*(S2x*S4x-(S3x)**2)-Sx*(Sxy*S4x-S3x*S2xy)+S2x*(Sxy*S3x-S2x*S2xy))


###régréssion linéaire


z = a*(tab_x**2)+b*tab_x+c

plt.figure()
plt.scatter(tab_x, tab_y)
plt.plot(tab_x, z, color='red')

A = np.vstack([tab_x, np.ones(len(tab_x))]).T

Y = np.hstack(tab_y)

m, c = np.linalg.lstsq(A,tab_y,  rcond=None)[0]

plt.plot(tab_x, m*tab_x+c, color = "black")




###regression polynomial

a,b,c = np.polyfit(tab_x,tab_y,2)

plt.plot(tab_x, a*tab_x**2+b*tab_x+c, color = "purple", marker='*')

plt.show()