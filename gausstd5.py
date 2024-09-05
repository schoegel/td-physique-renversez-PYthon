#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:38:11 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt





###Données

Jmax = 25

Umax = 3

Uunit = Umax/2

Nmax = 10

eps = 0.01


erreur = 10

n = 0


u = np.ones((Jmax+1,Jmax+1))

###2

u = u*Umax/2

u[Jmax,:] = 0

u[0,:] = 0

u[0,0] = Umax

u[0,Jmax] = Umax

u[Jmax,0] = Umax

u[Jmax,Jmax] = Umax

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

print("itération pour gauss",n)      
  
    
plt.figure()  
plt.pcolormesh(u)
plt.colorbar()
plt.title("Valeur de u Gauss avec convergence")
plt.show()


