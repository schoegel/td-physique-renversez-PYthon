#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:09:07 2022

@author: S18014755
"""
import numpy as np
import matplotlib.pylab as plt
### composantes des forces
def f1(xp , yp): ##compo en x
    return - (ETA/MASSE)*xp
   
def f2(xp, yp) :  ##compo en y
    return - (ETA/MASSE)*yp - g

### constantes et conditions initiales
v0 = 70 #m/s
DT = 0.01
g = 9.81 #m/s2
MASSE = 1#kg
Lambda = 0.001
ETA  = 0.01
Theta = np.pi/4
n1 = 0
n2 = 0
n3 = 0
n4 = 0
###fonction initialisation

def initialisation():
    y = 0 #y à t = 0
   
    x = 0#x à t = 0 
   
    xp = v0*np.cos(Theta)
   
    yp = v0*np.sin(Theta)
   
    return x, y, xp, yp

x , y, xp, yp = initialisation()

###euler

x_tab_euler1 = np.array([x])

y_tab_euler1 = np.array([y])

xp_tab_euler1 = np.array([xp])

yp_tab_euler1 = np.array([yp])

x_tab_euler2 = np.array([x])

y_tab_euler2 = np.array([y])

xp_tab_euler2 = np.array([xp])

yp_tab_euler2 = np.array([yp])

def euler(dt, x, y, xp, yp): #xp1 yp1, xp et yp a l'instant t+1
    xp1 = xp + f1(xp, yp)*DT
    x1 = x + xp*DT
    yp1 = yp + f2(xp, yp)*DT
    y1 = y + yp*DT
    return np.array([x1, y1, xp1, yp1])

###euler cromer

x_tab_eulerc1 = np.array([x])

y_tab_eulerc1 = np.array([y])

xp_tab_eulerc1 = np.array([xp])

yp_tab_eulerc1 = np.array([yp])

x_tab_eulerc2 = np.array([x])

y_tab_eulerc2 = np.array([y])

xp_tab_eulerc2 = np.array([xp])

yp_tab_eulerc2 = np.array([yp])

def euler_cromer(dt, x, y, xp, yp): #xp1 yp1, xp et yp a l'instant t+1
    xp1 = xp + f1(xp, yp)*DT
    x1 = x + xp1*DT
    yp1 = yp + f2(xp, yp)*DT
    y1 = y + yp1*DT
    return np.array([x1, y1, xp1, yp1])

### runge kutta 2

x_tab_rk21 = np.array([x])

y_tab_rk21 = np.array([y])

xp_tab_rk21 = np.array([xp])

yp_tab_rk21 = np.array([yp])

x_tab_rk22 = np.array([x])

y_tab_rk22 = np.array([y])

xp_tab_rk22 = np.array([xp])

yp_tab_rk22 = np.array([yp])
                       

def rk2(dt, x, y, xp, yp):
    k1p =  f1(xp, yp)*DT
    k1x =  xp*DT
    k1q =  f2(xp, yp)*DT
    k1y =  yp*DT
   
    k2p = f1(xp + 0.5*k1p, yp +0.5*k1q)*DT
    k2x = xp*DT + 0.5*k1p*DT
    k2q = f2(xp + 0.5*k1p, yp +0.5*k1q)*DT
    k2y = yp*DT + 0.5*k1q*DT
   
    xp1 = xp + k2p
    x1 = x + k2x
    yp1 = yp + k2q
    y1 = y + k2y
   
    return np.array([x1, y1, xp1, yp1])

### Incrémentation eta = 0.01



while y >= 0 :
    x, y, xp, yp = euler(DT, x , y , xp , yp)
    x_tab_euler1  = np.append(x_tab_euler1, x)
    y_tab_euler1  = np.append(y_tab_euler1, y)
    xp_tab_euler1  = np.append(xp_tab_euler1, xp)
    yp_tab_euler1  = np.append(yp_tab_euler1, yp)
    n1 += 1
 
x , y, xp, yp = initialisation()
      
while y >= 0 :
    x, y, xp, yp = euler_cromer(DT, x , y , xp , yp)
    x_tab_eulerc1  = np.append(x_tab_eulerc1, x)
    y_tab_eulerc1  = np.append(y_tab_eulerc1, y)
    xp_tab_eulerc1  = np.append(xp_tab_eulerc1, xp)
    yp_tab_eulerc1  = np.append(yp_tab_eulerc1, yp)
    n2 += 1


x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = rk2(DT, x , y , xp , yp)
    x_tab_rk21  = np.append(x_tab_rk21, x)
    y_tab_rk21  = np.append(y_tab_rk21, y)
    xp_tab_rk21  = np.append(xp_tab_rk21, xp)
    yp_tab_rk21  = np.append(yp_tab_rk21, yp)
    n3 += 1   
   
 ### Incrémentation eta = 0.0  
  
ETA  = 0.0

x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = euler(DT, x , y , xp , yp)
    x_tab_euler2  = np.append(x_tab_euler2, x)
    y_tab_euler2  = np.append(y_tab_euler2, y)
    xp_tab_euler2  = np.append(xp_tab_euler2, xp)
    yp_tab_euler2  = np.append(yp_tab_euler2, yp)
    n4 += 1
 
x , y, xp, yp = initialisation()
      
while y >= 0 :
    x, y, xp, yp = euler_cromer(DT, x , y , xp , yp)
    x_tab_eulerc2  = np.append(x_tab_eulerc2, x)
    y_tab_eulerc2  = np.append(y_tab_eulerc2, y)
    xp_tab_eulerc2  = np.append(xp_tab_eulerc2, xp)
    yp_tab_eulerc2  = np.append(yp_tab_eulerc2, yp)

x , y, xp, yp = initialisation()

while y >= 0 :
    x, y, xp, yp = rk2(DT, x , y , xp , yp)
    x_tab_rk22  = np.append(x_tab_rk22, x)
    y_tab_rk22  = np.append(y_tab_rk22, y)
    xp_tab_rk22  = np.append(xp_tab_rk22, xp)
    yp_tab_rk22  = np.append(yp_tab_rk22, yp) 


###plot   
   
plt.figure()
plt.grid()
plt.plot(x_tab_euler1,y_tab_euler1, "red", label= "eta = 0,01")
plt.plot(x_tab_euler2,y_tab_euler2, "blue", label= "eta = 0,0")
plt.legend()
plt.title("equation du mouvement avec Euler ")
plt.savefig("equa_du_mvt_euler.pdf")
plt.show()
   
plt.figure()
plt.grid()
plt.plot(x_tab_eulerc1,y_tab_eulerc1, "red", label= "eta = 0,01")
plt.plot(x_tab_eulerc2,y_tab_eulerc2, "blue", label= "eta = 0,0")
plt.legend()
plt.title("equation du mouvement avec Euler cromer ")
plt.show()
   
plt.figure()
plt.grid()
plt.plot(x_tab_rk21,y_tab_rk21, "red", label= "eta = 0,01")
plt.plot(x_tab_rk22,y_tab_rk22, "blue", label= "eta = 0,0")
plt.legend()
plt.title("equation du mouvement avec rk2")
plt.show()


### ode

from scipy.integrate import ode

def f(t,y):
    xp=y[0]
    x= y[1]
    yp=y[2]
    y= y[3]   
    return([f1(xp,yp),xp,f2(yp,yp),yp])

x_sc, y_sc, xp_sc, yp_sc = initialisation()

t=0
y =[xp_sc, x_sc, yp_sc, y_sc]


x_tab_sc = np.array([x_sc])
y_tab_sc = np.array([y_sc])
xp_tab_sc = np.array([xp_sc])
yp_tab_sc = np.array([yp_sc])


r = ode(f).set_integrator('dopri5') 

r.set_initial_value(y, t)

while r.successful() and  r.y[3]>=0:  
    xp_sc,x_sc,yp_sc,y_sc=r.integrate(r.t+DT)
    x_tab_sc  = np.append(x_tab_sc, x_sc)
    y_tab_sc  = np.append(y_tab_sc, y_sc)
    xp_tab_sc  = np.append(xp_tab_sc, xp_sc)
    yp_tab_sc  = np.append(yp_tab_sc, yp_sc)
    


plt.figure()
plt.grid()
plt.plot(x_tab_euler2,y_tab_euler2, "black", label= "mvt avec eulereta ")
plt.plot(x_tab_eulerc2,y_tab_eulerc2, "purple", label= "mvt avec euleur_cromer ")
plt.plot(x_tab_rk22,y_tab_rk22, "blue", label= "mvt avec rungeeta ")
plt.plot(x_tab_sc, y_tab_sc, "red", label= "mvt avec scipy ")
plt.plot(x_tab_rk22 - x_tab_sc, y_tab_rk22 - y_tab_sc )
plt.legend()
plt.title("equations du mouvement eta = 0")
plt.show()