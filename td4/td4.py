#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:27:34 2022

@author: S18014755
"""

import numpy as np
import matplotlib.pylab as plt
from scipy import integrate as intg

###données
n = 1000


a = 0 

b = 2
h = (b-a)/n
x = np.linspace(a,b,n+1)


### méthode des trapèzes

def trapeze(x,y):    
      h=x[1]-x[0]      
      return h/2*(y[0]+y[-1]+2*(sum(y)-y[0]-y[-1]))

### méthode des trapèzes

def simpson(x,y):    
    h=x[1]-x[0]
    n=len(x)
    S = 0
    for i in np.arange(1,n-1,2) :        
        S += (y[i-1]+4*y[i]+y[i+1])   
    return S*h/3

###fonctions poly2

y1 = x**2/3

It1 = trapeze(x,y1)

Is1 = simpson(x,y1)

It2 = intg.trapz(x,y1)

Is2 = intg.simps(x,y1)

print(8/9,It1,Is1, It2, Is2)

#reponse analytique = 8/9
    

###sinus cardinal

def sin_card(x) :
    y=np.empty_like(x)
    for i in np.arange(len(x)):    
        if x[i] == 0:
            y[i] = 1
        else:
            y[i] = np.sin(x[i])/x[i]
    return y

y2 = sin_card(x)

y2[0] = 0

a = 0

b = 2*np.pi

It = trapeze(x, y2)

Is = simpson(x, y2)

It = np.array([])

n_convergence=np.arange(20,1000,20)

###Trapeze

for i in n_convergence:
    x = np.linspace(a,b,i+1)
    y2 = sin_card(x)
    y2[0] = 0
    It = np.append(It,trapeze(x,y2))

###Simpson


Is = np.array([])
for i in n_convergence:
    x = np.linspace(a,b,i+1) 
    y2 = sin_card(x)
    y2[0] = 1
    Is = np.append(Is,simpson(x,y2))
    
### etude de la convergence 

x = np.linspace(a,b,len(It))


plt.figure()
plt.plot(x, It, color = "blue", label = "trapeze")
plt.plot(x, Is, color = "cyan", label="Simpson")    
plt.legend()
plt.show()

    
### rayonnement solaire 1 #1000w/m2

x,y = np.loadtxt("ASTMG173_Interpolated.dat",skiprows=0,unpack=True)


spec_Is =simpson(x,y)
print("integ spectre=",spec_Is)


### Rayonnement solaire 2 1000w/m2

x,y = np.loadtxt("ASTMG173.dat",skiprows=0,unpack=True)



def montecarlo(x,y): 
      A = 0
      for i in np.arange(len(x)) :
          A += (y[i-1]+y[i])*(x[i]-x[i-1])/2
          print(y[i-1]+y[i],x[i]-x[i-1])
      return A
 
   
spec_It = montecarlo(x,y)
print("integ spectre2 = ",spec_It)


#MC

x = np.sort(np.random.random(n))


print(montecarlo(x,y))

Im = np.array([])

for i in n_convergence:     
    x1 = np.sort(np.random.random(i+1))*2*np.pi
    y2 = x**2
    Im=np.append(Im,montecarlo(x1,y2))
  
It = np.array([])    
for i in n_convergence:
    x2 = np.linspace(a,b,i+1) 
    y2 = np.sinc(x2/np.pi)
    It=np.append(It,trapeze(x2,y2))

Is = np.array([])

for i in n_convergence:
    x3 = np.linspace(a,b,i+1) 
    y2 = np.sinc(x3/np.pi)
    Is=np.append(Is,simpson(x3,y2))
    

plt.figure()
# plt.plot(n_convergence, It, color = "blue", label = "trapeze")
# plt.plot(n_convergence, Is, color = "red", label="Simpson")    
plt.plot(n_convergence, Im, color = "purple", label="Montecarlo") 
plt.legend()
plt.show()



