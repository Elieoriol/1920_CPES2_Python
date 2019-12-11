import numpy as np

## Exercice 1 : Affichage d'arbres

class Arbre:
    def __init__(self, entier):
        self.noeud = entier
        self.filsDroit = None
        self.filsGauche = None
        self.pere = None

# 1.1
arbre = Arbre(12)

noeud = Arbre(20)
arbre.filsDroit = noeud
noeud.pere = arbre

noeud = Arbre(3)
arbre.filsDroit.filsDroit = noeud
noeud.pere = arbre.filsDroit

noeud = Arbre(2)
arbre.filsGauche = noeud
noeud.pere = arbre

noeud = Arbre(9)
arbre.filsGauche.filsGauche = noeud
noeud.pere = arbre.filsGauche

noeud = Arbre(4)
arbre.filsGauche.filsDroit = noeud
noeud.pere = arbre.filsGauche

noeud = Arbre(10)
arbre.filsGauche.filsDroit.filsDroit = noeud
noeud.pere = arbre.filsGauche.filsDroit

# 1.2
def taille(arbre):
    if arbre is None:
        return 0
    return 1 + taille(arbre.filsDroit) + taille(arbre.filsGauche)

print("Taille :", taille(arbre))

# 1.3
def hauteur(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.filsDroit), hauteur(arbre.filsGauche))

print("Hauteur :", hauteur(arbre))

# 1.4
def prefixe(a, marque):
    if a is not None:
        marque.append(a.noeud)
        prefixe(a.filsGauche, marque)
        prefixe(a.filsDroit, marque)

marque = []
prefixe(arbre, marque)
print("Prefixe :", marque)

# 1.5
def infixe(a, marque):
    if a is not None:
        infixe(a.filsGauche, marque)
        marque.append(a.noeud)
        infixe(a.filsDroit, marque)

marque = []
infixe(arbre, marque)
print("Infixe :", marque)

# 1.6
def postfixe(a, marque):
    if a is not None:
        postfixe(a.filsGauche, marque)
        postfixe(a.filsDroit, marque)
        marque.append(a.noeud)

marque = []
postfixe(arbre, marque)
print("Postfixe :", marque)

# 1.7
def affichage(a, marque, type):
    if a is not None:
        if type == 'prefixe':
            marque.append(a.noeud)
        affichage(a.filsGauche, marque, type)

        if type == 'infixe':
            marque.append(a.noeud)
        affichage(a.filsDroit, marque, type)

        if type == 'postfixe':
            marque.append(a.noeud)

marque = []
affichage(arbre, marque, 'prefixe')
print("Prefixe :", marque)

marque = []
affichage(arbre, marque, 'infixe')
print("Infixe :", marque)

marque = []
affichage(arbre, marque, 'postfixe')
print("Postfixe :", marque)



## Exercice 2 : ABR

# 2.1
def initialisationArbre(e):
    abr = Arbre(e)

    print('Fils Gauche de ', e)
    x = input()
    if x != '':
        noeud = initialisationArbre(int(x))
        abr.filsGauche = noeud
        noeud.pere = abr

    print('Fils Droit de ', e)
    y = input()
    if y != '':
        noeud = initialisationArbre(int(y))
        abr.filsDroit = noeud
        noeud.pere = abr
    return abr

abr = initialisationArbre(25)
marque = []
infixe(abr, marque)
print('Infixe de abr :', marque)

# 2.2
def recherche(A, x):
    while A != None:
        if x == A.noeud:
            return True
        elif x < A.noeud:
            A = A.filsGauche
        else:
            A = A.filsDroit
    return False

print('20 appartient à abr :', recherche(abr, 20))
print('3 appartient à abr :', recherche(abr, 3))

# 2.3
def maxA(abr):
    while(abr.filsDroit != None):
        abr = abr.filsDroit
    return abr.noeud

print('Maximum de abr :', maxA(abr))

# 2.4
def insereFeuille(A, x):
    if x < A.noeud:
        if A.filsGauche == None:
            noeud = Arbre(x)
            A.filsGauche = noeud
            noeud.pere = A
        else :
            insereFeuille(A.filsGauche, x)
    else :
        if A.filsDroit == None:
            noeud = Arbre(x)
            A.filsDroit = noeud
            noeud.pere = A
        else :
            insereFeuille(A.filsDroit, x)

insereFeuille(abr, 29)
marque = []
infixe(abr, marque)
print('Noeud 29 inséré :', marque)



## Exercice 3 : Suppression

# abr = initialisationArbre(5)

abr = Arbre(5)

noeud = Arbre(9)
abr.filsDroit = noeud
noeud.pere = abr

noeud = Arbre(20)
abr.filsDroit.filsDroit = noeud
noeud.pere = abr.filsDroit

noeud = Arbre(7)
abr.filsDroit.filsGauche = noeud
noeud.pere = abr.filsDroit

noeud = Arbre(16)
abr.filsDroit.filsDroit.filsGauche = noeud
noeud.pere = abr.filsDroit.filsDroit

noeud = Arbre(12)
abr.filsDroit.filsDroit.filsGauche.filsGauche = noeud
noeud.pere = abr.filsDroit.filsDroit.filsGauche

noeud = Arbre(11)
abr.filsDroit.filsDroit.filsGauche.filsGauche.filsGauche = noeud
noeud.pere = abr.filsDroit.filsDroit.filsGauche.filsGauche

noeud = Arbre(13)
abr.filsDroit.filsDroit.filsGauche.filsGauche.filsDroit = noeud
noeud.pere = abr.filsDroit.filsDroit.filsGauche.filsDroit

noeud = Arbre(18)
abr.filsDroit.filsDroit.filsGauche.filsDroit = noeud
noeud.pere = abr.filsDroit.filsDroit.filsGauche

noeud = Arbre(17)
abr.filsDroit.filsDroit.filsGauche.filsDroit.filsGauche = noeud
noeud.pere = abr.filsDroit.filsDroit.filsGauche.filsGauche

noeud = Arbre(4)
abr.filsGauche = noeud
noeud.pere = abr

noeud = Arbre(1)
abr.filsGauche.filsGauche = noeud
noeud.pere = abr.filsGauche


marque = []
infixe(abr, marque)
print('Infixe de abr :', marque)

# 3.2
def supprimemax(A):
    if taille(A) == 1:
        return A.noeud

    elif A.filsDroit == None:
        return A.noeud

    else :
        courant = A.filsDroit
        while courant.filsDroit != None:
            courant = courant.filsDroit
        if courant.filsGauche == None:
            courant.pere.filsDroit = None
        else:
            courant.pere.filsDroit = courant.filsGauche
            courant.filsGauche.pere = courant.pere.filsDroit
        return courant.noeud

# 3.3
def supprimer(x, A):
    if x < A.noeud:
        A.filsGauche = supprimer(x, A.filsGauche)

    elif x > A.noeud:
        A.filsDroit = supprimer(x, A.filsDroit)

    else:
        if A.filsDroit == None and A.filsGauche == None:
            return None

        elif A.filsDroit == None :
            return A.filsGauche

        elif A.filsGauche == None :
            return A.filsDroit

        else:
            val_max = supprimemax(A.filsGauche)
            A.noeud = val_max
    return A

abr = supprimer(13, abr)
marque = []
infixe(abr, marque)
print('Infixe de abr après suppression de 13 :', marque)
abr = supprimer(20, abr)
marque = []
infixe(abr, marque)
print('Infixe de abr après suppression de 20 :', marque)
abr = supprimer(5, abr)
marque = []
infixe(abr, marque)
print('Infixe de abr après suppression de 5 :', marque)
_, abr = supprimemax(abr)
marque = []
infixe(abr, marque)
print('Infixe de abr après suppression du max :', marque)


## Exercice 4 : Le tri par tas

class Heap:
    def __init__(self):
        self.L = []
        self.n = 0

    def push(self, x):
        self.L.append(x)
        self.n += 1
        pos = self.n-1
        parent_pos = (pos+1)//2-1
        while pos > 0 and self.L[parent_pos] > self.L[pos]:
            self.L[parent_pos], self.L[pos] = self.L[pos], self.L[parent_pos]
            pos = parent_pos
            parent_pos = (pos+1)//2-1

    def fromList(self, l):
        self.L = []
        self.n = 0
        for x in l:
            self.push(x)








    def pop(self):
        to_return = self.L[0]
        self.n -= 1
        if self.n == 0:
            self.L = []
            return to_return

        self.L[0] = self.L.pop()
        pos = 0
        child_pos = 2*pos+1
        while child_pos < self.n:
            right_pos = child_pos+1
            if right_pos < self.n and self.L[right_pos] < self.L[child_pos] and self.L[right_pos] < self.L[pos]:
                child_pos = right_pos

            if self.L[pos] < self.L[child_pos]:
                break

            self.L[pos], self.L[child_pos] = self.L[child_pos], self.L[pos]
            pos = child_pos
            child_pos = 2*pos+1
        return to_return


def triTas(L):
    tas = Heap()
    tas.fromList(L)
    Ltri = []
    for k in range(tas.n):
        Ltri.append(tas.pop())
    return Ltri

L = list(np.random.randint(0, 100, 12))
print(triTas(L[:]))


import heapq

def triTasQ(L):
    n = len(L)
    Ltri = []
    heapq.heapify(L)
    for i in range(n):
        Ltri.append(heapq.heappop(L))
    return(Ltri)

print(triTasQ(L[:]))



import time
import random
import matplotlib.pyplot as plt

def listeAlea(n):
    l=[]
    for i in range(n):
        l.append(random.uniform(-1000,1000))
    return l

num = 15
tailles = np.logspace(2, 5, 15, dtype='int')
tps, tpsq = np.zeros(num), np.zeros(num)
reps = 10
for i in range(num):
    for k in range(reps):
        L = listeAlea(tailles[i])

        t0 = time.time()
        triTas(L[:])
        tps[i] += time.time()-t0

        t0 = time.time()
        triTasQ(L[:])
        tpsq[i] += time.time()-t0

tps /= reps
tpsq /= reps

plt.plot(tailles, tps, label='Heap')
plt.plot(tailles, tpsq, label='heapq')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('t')
plt.title("Comparaison des temps d'execution du tri par tas")
plt.legend()
plt.show()
