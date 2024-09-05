#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 09:14:51 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt





###Données

Jmax = 10

Umax = 3

Uunit = Umax/2

Nmax = 10

###1 # 1ere ligne = j 2eme ligne = l

#u = np.linspace(0,2*(Jmax+1),dtype = float).reshape(2,Jmax)

# J = np.arange((Jmax+1), dtype = float) #pas de 1

# L = np.arange((Jmax+1), dtype = float)

# u = np.array([])

# u = np.append(u,J)

# u = np.append(u,L).reshape(2,len(J))

u = np.ones((Jmax+1,Jmax+1))

###2

u = u*Umax/2

u[Jmax,:] = 0

u[0,:] = 0

u[:,0] = 0

u[:,Jmax] = Umax


#uj,l = 1/4(uj+1,l + uj−1,l + uj,l+1 + uj,l−1) + 4 ρj,l

###3

# u_ancien = np.array([])

# u_ancien = np.append(u_ancien,J)

# u_ancien = np.append(u_ancien,L).reshape(2,len(J))

u_ancien = np.copy(u)



 
for n in np.arange(Nmax):
    u_ancien = np.copy(u)
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]=0.25*(u_ancien[j+1,l]+u_ancien[j-1,l]+u_ancien[j,l+1]+u_ancien[j,l-1])
            
     



   
plt.figure()     
plt.pcolormesh(u)
plt.title("Valeur de u Jacobi")
plt.show()



            
            
     
     



