#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:48:08 2022

@author: S18014755
"""


import numpy as np
import matplotlib.pylab as plt





###Données

Jmax = 100

Umax = 3

Uunit = Umax/2

Nmax = 10


###Initialisation

def initialisation():
    
    u = np.ones((Jmax+1,Jmax+1))
    
    u = u*Umax/2
    
    u[Jmax,:] = 0
    
    u[0,:] = 0
    
    u[:,0] = 0
    
    u[:,Jmax] = Umax
    
    return u

u = initialisation()

u_ancien = np.copy(u)

###fonctions


def Jacobi_delta2(u,u_ancien,Jmax) :
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]=0.25*(u_ancien[j+1,l]+u_ancien[j-1,l]+u_ancien[j,l+1]+u_ancien[j,l-1])
    return u 
        

def Jacobi_delta4(u,u_ancien,Jmax) :
    for j in np.arange(1,Jmax):
        for l in np.arange(1,Jmax):
            u[j,l]= 0.05*(4*(u_ancien[j+1,l]+u_ancien[j-1,l]+u_ancien[j,l+1]+u_ancien[j,l-1])+u_ancien[j+1,l+1]+u_ancien[j-1,l-1]+u_ancien[j+1,l-1]+u_ancien[j-1,l+1])
    return u 
        

###etude du nombra d'itération en fonctoin de delta

eps = 0.001

n = 0

erreur = 10

while erreur >= eps :
    n += 1
    u_ancien = np.copy(u)
    u = np.copy(Jacobi_delta4(u, u_ancien, Jmax))
    erreur = np.max(np.abs(u - u_ancien))

print("itération pour Jacobi pour delta⁴",n)   ### 258 eps 0,001

u = initialisation()

u_ancien = np.copy(u)

n = 0

erreur = 10

while erreur >= eps :
    n += 1
    u_ancien = np.copy(u)
    u = np.copy(Jacobi_delta2(u, u_ancien, Jmax))
    erreur = np.max(np.abs(u - u_ancien))

print("itération pour Jacobi pour delta²",n) #287 > delta4eps 0,001

#l'utilisation de delta a la puissance 4 demande moin d'itération et est par conséquent plus rapide et consomme moins d'energie et est plus précis    
  










