import numpy as np


###exercice1 

##1

a = np.zeros(10)

a[4] = 1 

print(a, type(a))

##2

b = np.zeros(10, dtype = complex)

b = b -1

b[-2] = 1 +1j

print(b, type (b))

##3

#Créer et afficher un tableau de type numpy.ndarray monodimensionnel (affecté à la
# variable c ) contenant les entiers de 10 à 20 (10 et 20 compris)
c = np.arange(10,21)

print(c)

##4
# Afficher le nombre d’éléments de c strictement supérieurs à 14 :
# (a) à l’aide d’une boucle while .
# (b) à l’aide d’une fonctionnalité de numpy .

#a)

for i in range(len(c)):
    if c[i] > 14 :
        print(c[i])
        
#b) 

print(np.size(np.where(c>14)))

    
          
    

##5
# Renverser c : le premier élément devient le dernier, etc.

c = c[::-1]

print(c)

##6
# Créer et afficher un tableau de type numpy.ndarray monodimensionnel (affecté à la
# variable e ) contenant 10 valeurs aléatoires comprises entre 0 et 1 (voir la documentation
# de numpy.random.uniform )

e = np.random.uniform(0,1,10)

print(e, len(e))

 1.
##7
# Créer et afficher un tableau de type numpy.ndarray monodimensionnel (affecté à la
# variable f ) contenant 20 valeurs aléatoires comprises entre 5 et 12.

f = np.random.uniform(5,12,20)

print(f)
##8
# Afficher les valeurs minimales et maximales du tableau f précédent.

a = np.max(f)

b = np.min(f)

print(a,b)

##9
# Afficher les indices du tableau f de ses valeurs minimales et maximales.

# tab2[tab2>5]


print(f[f == a], f[f == b])
b = []

for i in range(len(a)):
    for j in range(len(a)) : 
        b.apppend(a[i,j])

print(b)
##10
# À l’aide d’une boucle for , calculer la valeur moyenne des éléments du tableau f .

moy = 0

for i in range(len(f)):
    moy += f[i]/len(f)
    
print(moy)   


##11
# Même question avec une fonction numpy .

moy2 = sum(f)/len(f) tab_d = np.vstack((tab_a,tab_b))

print(moy2)

##exercice 2

# On considère le segment [a, b] que l’on souhaite discrétiser, c’est-à-dire créer un ensemble fini
# de N points {x 0 , x 1 , . . . , x N −1 } appartenant à ce segment. Bien souvent en calcul numérique,
# on choisit ces points équi-répartis sur [a, b], c’est-à-dire équidistants les uns des autres, et tels
# que x 0 = a et x N −1 = b.
# Soit a = 4, b = 12.5, N = 11 :
# • à l’aide d’une boucle for , afficher les x i désirés.
# • même question avec une fonction numpy .b = []

for i in range(len(a)):
    for j in range(len(a)) : 
        b.apppend(a[i,j])

print(b)

#données

a = 4   #(x0)

b = 12.5  #(N-1)

N = 11

#boucle 

E1 = []

x = a

for i in range(N) :
    E1.append(x)
    x += (b-a)/N
    
print(E1)    

#numpy

print(np.arange(a,b,(b-a)/N))

###exercice3

# . Créer et afficher un tableau de type numpy.ndarray bidimensionnel (affecté à la variable
# 1 ) représentant la matrice suivante :
# 
# 
# 0 1 2
#  3 4 5 
# 6 7 8
# 2. Afficher la première ligne de A .
# 3. Afficher la dernière colonne de A .
# 4. Créer et afficher un tableau de type numpy.ndarray bidimensionnel (affecté à la variable
# I ) représentant la matrice 3 × 3 identité I 3 .
# 5. Effectuer et afficher le résultat des produits matriciels AI 3 et I 3 A.
# 6. Transformer A en un tableau monodimensionnel via des boucles puis via une instruction
# numpy .



#1 

a = np.arange(9).reshape(3, 3)

#2

print(a[0])

#3

print(a[:,1])  #parcours le tableau

#4 tab_d = np.vstack((tab_a,tab_b))

I = np.identity(3)

#5

print("Ia =",I@a,"\n ","\n "," aI = ", a@I)

#6
#boucle

b = []

for i in range(len(a)):
    for j in range(len(a)) : 
        b.append(a[i,j])

print(b)


#numpy 

print(np.ravel(a))

##exercice4
#a

N = 10

a = np.arange(N+1).reshape(N+1,1)

print(a)

b = a[::-1]

print(b)
 tab_d = np.vstack((tab_a,tab_b))
#b

c = a + b

d = a - b

#c

# def print2(nom):
#     print(nom)

# print(print2("hey"))



def AfficheVecteur(nom,tab) :
    x = np.ravel(tab)
    print(nom)
    for i in range(len(x)) :
        print(x[i])

        
def fct_bidon(x):
    return(42)

AfficheVecteur("a", a)

print(fct_bidon(5))

#d

M = np.zeros(N**2).reshape(N,N)

# for i in range(N):
#     for j in range(N):
        
#e


# tab_a = np.arange(5)
# tab_b = tab_a[::-1]
# tab_c = np.hstack((tab_a,tab_b))
# print("tab_c=",tab_c)
# tab_d = np.vstack((tab_a,tab_b))
# print("tab_d=",tab_d)        



N = 10



M = np.zeros(N**2).reshape(N,N) + np.diag(np.ones(N)) + np.diag(np.ones(N-1),1) + np.diag(np.ones(N-1),-1)





        



