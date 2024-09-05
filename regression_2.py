#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:29:29 2022

@author: S18014755
"""

import numpy as np 
import matplotlib.pyplot as plt

###2.2.1

###données

tab_x, tab_y = np.loadtxt("points.dat",skiprows=0,unpack=True)

N = len(tab_x)

###Somme

Sx = np.sum(tab_x)

Sy = np.sum(tab_y)

Sxx = np.sum(tab_x**2)

Syy = np.sum(tab_y**2)

Sxy = np.sum(tab_y*tab_y)

###coeficient a, b , p pour dx/da et dx/db = 0 (pas de variation de c)

# X = (1/N)*sum((np.linalg.norm(tab_y-(a*tab_x+b)))**2)
#### fonctions (a = pente , b = ordo a l'origine, c = coefficient directeur)

def pente(N, Sx, Sy, Sxx, Syy, Sxy) : 
    a = (N*Sxy-Sx*Sy)/(N*Sxx-Sx**2)
    return (a)

def ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy):
    b = (Sx*Sxy - Sxx*Sy)/(Sx**2-Sxx*N)
    return b 

def coeff_corr(N, Sx, Sy, Sxx, Syy, Sxy) :
    p = (Sx*Sxy)/np.sqrt((N*Syy-Sy)*(N*Sxx-Sx))
    return p

# def erreur_quad(N, Sx, Sy, Sxx, Syy, Sxy):
#     X = np.array([])
#     for i in range(len(tab_x)) :
#         X.append((1/N)*sum((np.linalg.norm(tab_y[i]-(a*tab_x[i]+b)))**2))
#         print(X)
#     return X  np.linalg.norm(tab_y - ((pente(N, Sx, Sy, Sxx, Syy, Sxy)*tab_x +ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy))**2)
        
a=pente(N, Sx, Sy, Sxx, Syy, Sxy)
b=ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy)
rho=coeff_corr(N, Sx, Sy, Sxx, Syy, Sxy)
print(a,b,rho)

print((np.linalg.norm(tab_y-(pente(N, Sx, Sy, Sxx, Syy, Sxy)*tab_x +ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy))))**2)

plt.plot(tab_x,tab_y,'+-') # marche pa tres bien 
y=a*tab_x+b
plt.plot(tab_x, y,color= 'blue')
plt.show()

#transformé 1 : on utilise (fait comme si y est) une exponnentplt.show()ielle décroissante, donc on prend ln y

yt1 = np.log(tab_y)

plt.figure()
plt.plot(tab_x, yt1,color= 'red', label = 'données en log')

Sx = np.sum(tab_x)

Sy = np.sum(yt1)

Sxx = np.sum(tab_x**2)

Syy = np.sum(yt1**2)

Sxy = np.sum(tab_x*yt1)

a = pente(N, Sx, Sy, Sxx, Syy, Sxy) 
b = ordo_origine(N, Sx, Sy, Sxx, Syy, Sxy)
rho = coeff_corr(N, Sx, Sy, Sxx, Syy, Sxy)

y= a*tab_x + b

plt.plot(tab_x, y,label = 'fits en étant passé par le log')
plt.legend()
plt.show()

#transformé 2 : on repasse sur notre forme de départ ( exp(ln(y))), cependnat les coefficient issur des sommes et depandant de y on etais changé
#doncla regression lineéaire aussi 

yt2 = np.exp(y)

plt.figure()
plt.plot(tab_x, tab_y,color= 'blue')
plt.plot(tab_x, yt2,color= 'red', label = 'fits remis en forme')
plt.show()

