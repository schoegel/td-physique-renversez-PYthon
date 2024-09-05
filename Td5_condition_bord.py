#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:09:00 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt



### Si on change les conditions aux bords en Umax + Udecal tout les point seronts  

###Données

Jmax = 100

Umax = 3

Uunit = Umax/2

Nmax = 10

eps = 0.01


erreur = 10

n = 0

K = 10  

erreur_tab = np.array([])

###8

u_analy = np.zeros((Jmax+1,Jmax+1)) #vrai u 

u_analy[Jmax,:] = 0

u_analy[0,:] = 0

u_analy[:,0] = 0

u_analy[:,Jmax] = Umax

u_analy[0,0] = Umax

u_analy[0,Jmax] = Umax

u_analy[Jmax,0] = Umax

u_analy[Jmax,Jmax] = Umax

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





###Méthode de Gauss

u = np.ones((Jmax+1,Jmax+1))

u = u*Umax/2

u[Jmax,:] = 10

u[0,:] = 10

u[:,0] = 10

u[:,Jmax] = Umax +10




###3



u_ancien = np.copy(u)



def Gauss(u,Jmax) : 
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]=0.25*(u[j+1,l]+u[j-1,l]+u[j,l+1]+u[j,l-1])        
    return u 


while erreur >= eps :
    u_ancien = np.copy(u)
    u = np.copy(Gauss(u,Jmax))
    erreur = np.max(np.abs(u - u_ancien))
   
    
plt.figure()
plt.pcolormesh(u)
plt.colorbar()
plt.title("u(Gauss) avec changement de bord")
plt.show()