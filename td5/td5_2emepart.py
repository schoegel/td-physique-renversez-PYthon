#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 09:57:24 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt





###Données

Jmax = 25

Umax = 3

Uunit = Umax/2 

Nmax = 10


erreur = 10

n = 0


eps = 0.01

u = np.ones((Jmax+1,Jmax+1))

###2

u = u*Umax/2

u[Jmax,:] = 0

u[0,:] = 0

u[:,0] = 0

u[:,Jmax] = Umax


for j in np.arange(1,Jmax):
    for l in np.arange(1,Jmax):
        u[j,l]=0.25*(u[j+1,l]+u[j-1,l]+u[j,l+1]+u[j,l-1])
 
###3



u_ancien = u



eps = 0.01
def Jacobi(u,u_ancien,Jmax) :
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]=0.25*(u_ancien[j+1,l]+u_ancien[j-1,l]+u_ancien[j,l+1]+u_ancien[j,l-1])
    return u 
        


###convergence

# u[Jmax,:] = 0

# u[0,:] = 0

# u[:,0] = 0

# u[:,Jmax] = Umax
  



while erreur >= eps :
    n += 1
    u_ancien = np.copy(u)
    u = np.copy(Jacobi(u, u_ancien,Jmax))
    erreur = np.max(np.abs(u - u_ancien))

    
    
print("itération Jacobi", n)    
  
    
  

u[Jmax,:] = 0

u[0,:] = 0

u[:,0] = 0

u[:,Jmax] = Umax

  
    
plt.figure()  
plt.pcolormesh(u)
plt.colorbar()
plt.title("Valeur de u Jacobi avec convergence")
plt.show()
