import numpy as np
import time

### Exercie 2


m = 5
n = 9
p = 4

q = (n<p) #false

print(q)

q = ( p == m+n )  #false

print(q)

q = ( p > n)  #false

print(q)

q = ( m >n or m>p)  #True

print(q)

q = (p != n) #True 

print(q)

print(" Bravo")


### Exercice 3
##1

x = 0
y= 0

for i in range(10) : 
    y = x
    x += 2
    print("x = ", x,"\n")
    print(x,"+", y, "=", x+y)
    
##2

x = 0 
S = 0 

for i in range(11):
    y = x
    x += 1.5
    print("x = ", x,"\n")
    print(x,"+", y, "=", x+y)
    

### Exercice 4
nb = int(input("saisir un nombre : "))

print("le cosinus de ce nombre vaut environs", "%.4f%", np.cos(nb))

### Exercice 5

def poly1(a,b): #a et b != 0
    if a*b < 0 :
         print("r1 = ", np.sqrt(-b/a), "r2 = ", -np.sqrt(-b/a))
    else :
        print("deux racines complexe")
        
print(poly1(5,-10))

### exercice 6 

def poly2(a,b,c): #a et b != 0
    det = b**2 - 4*a*c
    d = 0
    if det > 0 :
        d = 1
        print("deux racines réelles")

    elif det == 0 :
        d = 0
        print("une racine réelles")
                       
    else :
        d = -1
        print("deux racines complexe")

print(poly2(5,-10,20))
    
### exercice 7  
##1

m = 1
n = 3

print(m+n)

##2

m = int(input("m?"))

n = int(input("n?"))

print("la somme des nombres n et m est : ", m+n)        

m = input("m?")

n = input("n?")

print("la somme des string n et m est : ", m+n)

### exercice 8 

a0 = 2

for i in range(11):
    an = 1.1*a0
    a0 = an
    print("a_%g = %.5f"%(n,an))
    
### exercice 9

N = 10 
S1 = 0


for i in range(1 , N+1): #la suite n'est pas définie en 1
    print("le terme", i ," est ", 1/i**2)
    S1 += 1/i**2
    print("la suite est egal à :", S1)

N = 10 
S2 = 0 

for i in range(1 , N+1): 
    print("le terme", i ," est ", 4*(-1)**i/2*i+1)
    S2 += 4*(-1)**i/2*i+1 
    print("la suite est egal à :","\n" , S2) 

### exercice 10

#lorsque x = 1, Sn = somme de n= 0 jusqu'a n =N des an+1*(n+1)/x = an+1*(n+1)


n = 0
N = 10 
S3 = 1
x = float(input("entre un float"))

while n != N :        
    print("le terme n =", n ," est ", S3*x/(n+1))   
    S3 += S3*x/(n+1) 
    print("la suite est egal à :", "\n" , S3) 
    n += 1

### exercice 11 comparé exo9 et exo 9 avec numpy

### exercice 9 sans numpy

S2

t0 = time.time()

N = 10000 
S1_1 = 0


for i in range(1 , N+1): #la suite n'est pas définie en 1
    # print("le terme", i ," est ", 1/i**2)
    S1_1 += 1/i**2
    # print("la suite est egal à :", S1_1)
print("la suite est egal à :","\n" , S1_1)

seconds1 = time.time() - t0

print("temps suite 1 mth1 : ", "\n", seconds1)

t0 = time.time()

S2_1 = 0 

for i in range(0 , N+1): 
    # print("le terme", i ," est ", 4*(-1)**i/(2*i+1))
    S2_1 += 4*(-1)**i/(2*i+1) 
    # print("la suite est egal à :","\n" , S2_1) 

print("la suite est egal à :","\n" , S2_1)

seconds2 = time.time() - t0

print("temps suite 2 mth1 : ", "\n", seconds2)


#print("sans numpy : ", "\n", ticks)

### exercice 9 avec numpy

t0 = time.time()

n1 = np.arange(1,N+1)

S1_2 = sum(1/n1**2)

print("la suite 1 est égale à :", "\n",S1_2) #niquel

seconds3 = time.time() - t0

print("methode np :", "\n", seconds3, "\n","autre méthode :","\n", seconds1)

t0 = time.time()

n2 = np.arange(N+1)

S2_2 = sum(4*(-1)**n2/(2*n2+1))

print("la suite 1 est égale à :", "\n",S2_2)

seconds4 = time.time()-t0
 
print("methode np :", "\n", seconds2, "autre méthode :","\n", seconds4)

print("la méthode numpy est en moyenne :", "\n", (seconds1+seconds2)/(seconds3+seconds4)," de fois plus rapide")