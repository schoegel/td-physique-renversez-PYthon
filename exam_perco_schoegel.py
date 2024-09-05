#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:22:44 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
couleurs = ListedColormap((["white","turquoise","black"]))

###1
def nouvelllegrille(N,p):
    grille = np.zeros((N,N))
    for i in np.arange(N):
        for j in np.arange(N):
            x =  np.random.rand(1)
            if x < p :
                grille[i,j] = 0
            else :
                grille[i,j] = 1
    return grille
 
###2
g = nouvelllegrille(16,0.6)          
            

plt.matshow(g, cmap=couleurs)           
plt.savefig("grille.png")