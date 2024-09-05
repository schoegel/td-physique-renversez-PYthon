#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:58:49 2022

@author: S18014755
"""


import numpy as np
import matplotlib.pylab as plt





###Données

Jmax = 200

Umax = 3

Uunit = Umax/2

Nmax = 10

eps = 0.01

erreur = 10

n = 0

K = 10  

###8

u_analy = np.zeros((Jmax+1,Jmax+1))

u_analy[Jmax,:] = 0

u_analy[0,:] = 0

u_analy[:,0] = 0

u_analy[:,Jmax] = Umax
KMAX=10
for i in np.arange(1, Jmax) : 
    for j in np.arange(1, Jmax) :        
        S = 0
        for k in np.arange(1,KMAX) :
            n = 2*k - 1
            S += np.sin(n*np.pi*i/Jmax)*(np.sinh(n*np.pi*j/Jmax)/(n*np.sinh(n*np.pi)))
            u_analy[i,j] = S
            k +=1    
        u_analy[i,j] = (4/np.pi)*Umax*S


plt.figure()
plt.pcolormesh(u_analy)
plt.colorbar()
plt.title("U analytique ")
plt.show()

###Méthode de Gauss

u = np.ones((Jmax+1,Jmax+1))

u = u*Umax/2

u[Jmax,:] = 0

u[0,:] = 0

u[:,0] = 0

u[:,Jmax] = Umax




###3



u_ancien = np.copy(u)



def Gauss(u,Jmax) : 
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]=0.25*(u[j+1,l]+u[j-1,l]+u[j,l+1]+u[j,l-1])        
    return u 



###convergence



while erreur >= eps :
    n += 1
    u_ancien = np.copy(u)
    u = np.copy(Gauss(u,Jmax))
    erreur = np.max(np.abs(u - u_ancien))

plt.figure()
plt.pcolormesh(u - u_analy)
plt.colorbar()
plt.title("relaxVSanaly")


