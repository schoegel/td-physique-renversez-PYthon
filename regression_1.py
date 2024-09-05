#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:14:43 2022

@author: S18014755
"""


import numpy as np 

###2.2.1

###données

tab_x = np.array([1.0, 2.0, 4.0, 10.0])
tab_y = np.array([3.1, 5.2, 10.65, 25.77])

N = len(tab_x)

###Somme

Sx = np.sum(tab_x)

Sy = np.sum(tab_y)

Sxx = Sx**2

Syy = Sy**2

Sxy = Sy*Sx

###coeficient a, b , p pour dx/da et dx/db = 0 (pas de variation de c)

a = (N*Sxy-Sx*Sy)/(N*Sxx-Sx**2)

b = (Sx*Sxy - Sxx*Sy)/(Sx**2-Sxx*N)

p = (Sx*Sxy)/np.sqrt((N*Syy-Sy)*(N*Sxx-Sx))


#### fonctions (a = pente , b = ordo a l'origine, c = coefficient directeur)

def pente(N, Sx, Sy, Sxx, Syy, Sxy) : 
    return a

def ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy):
    return b 

def coeff_corr(N, Sx, Sy, Sxx, Syy, Sxy) :
    return p
    
print(pente(N, Sx, Sy, Sxx, Syy, Sxy),ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy),coeff_corr(N, Sx, Sy, Sxx, Syy, Sxy))





    