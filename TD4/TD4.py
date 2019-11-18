import os
os.chdir("C:/Users/Elie/Documents/Enseignement/1920_CPES2_Python_prof/TDs 19-20/TD4")

from mesFonctionsTri import *

## Exercice 1 : Tri Sélection

T = [9,3,12,5,1]
triSelection(T)
print("Selection :", T)

## Exercice 2 : Tri Insertion

T = [9,3,12,5,1]
triInsertion(T)
print("Insertion :", T)


## Exercice 3 : Tri Rapide

# 3.3
T = [9,3,12,5,1]
triRapideEnPlace(T)
print("Rapide (en place) :", T)

# 3.4
T = [9,3,12,5,1]
T = triRapide(T)
print("Rapide :", T)

# 3.5
import time
import random as rd

for size in [1000, 10000, 100000]:
    l=[]
    for i in range(size):
        l.append(rd.randint(-50, 50))
    tps = time.time()
    triRapide(l)
    print('Tri rapide (taille '+str(size)+') :',  time.time()-tps)


## Exercice 4 : Tri Fusion

T = [9,3,12,5,1]
T = triFusion(T)
print("Fusion :", T)


## Exercice 5 : Tri à Bulles

# 5.2
T = [9,3,12,5,1]
triBulles(T)
print("Bulles :", T)

# 5.3
T = [9,3,12,5,1]
triBullesOpti(T)
print("Bulles opti :", T)


## Exercice 6 : Comparaison

# 6.1
import numpy as np
import random as rd

def listeAlea(n):
    l=[]
    for i in range(n):
        l.append(rd.uniform(-1000, 1000))
    return l

    # une possibilite plus rapide avec numpy :
    # return np.random.uniform(-1000, 1000, size=n)


# 6.2
from mesFonctionsTri import *
import time

fich = open("tri_results.txt", 'w')
fich.write("Taille\tTB\tTS\tTI\tTR\tTF\tPS\n")

result = np.zeros((6,10))
cpt = 0
reps = 10
for n in range(1000, 10001, 1000):
    print(n, end=" ")
    fich.write(str(n))
    tps = np.zeros(6)

    # on repete 10 fois, on ajoute les temps de chaque algo de tri
    # on passe a chaque fois en argument l[:] pour copier l, car sinon on va trier la liste une premiere fois avec triSelection() puis appeler les autres fonctions sur cette liste triee
    for i in range(reps):
        l = listeAlea(n)

        t0 = time.time()
        triBullesOpti(l[:])
        tps[0] += time.time()-t0

        t0 = time.time()
        triSelection(l[:])
        tps[1] += time.time()-t0

        t0 = time.time()
        triInsertion(l[:])
        tps[2] += time.time()-t0

        t0 = time.time()
        triRapide(l[:])
        tps[3] += time.time()-t0

        t0 = time.time()
        triFusion(l[:])
        tps[4] += time.time()-t0

        t0 = time.time()
        l[:].sort()
        tps[5] += time.time()-t0

    # on moyenne les temps sur les 10 repetitions et on ecrit les resultats dans le fichier
    for k in range(6):
        result[k,cpt] = tps[k]/reps
        fich.write("\t"+str(round(result[k,cpt], 4)))
    fich.write("\n")
    cpt += 1
fich.close()


# 6.3
import matplotlib.pyplot as plt

plt.figure('10')
x = range(1000, 10001, 1000)
plt.plot(x, result[0], label="Tri bulles")
plt.plot(x, result[1], label="Tri selection")
plt.plot(x, result[2], label="Tri insertion")
plt.plot(x, result[3], label="Tri rapide")
plt.plot(x, result[4], label="Tri fusion")
plt.plot(x, result[5], label="Python sort")
plt.yscale(’log’)
plt.legend()
plt.title("Temps moyen d’execution des algorithmes de tri")
plt.xlabel("Taille")
plt.ylabel("Temps")
plt.savefig(’tps.jpg’)
plt.show()


