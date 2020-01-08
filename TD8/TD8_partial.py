import numpy as np
import random
import time
import itertools


## Exercice 1

# 1.1 & 1.2
class Graphe0:
    def __init__(self, n, L=[], orientation=True):
        self.nb_sommets = n
        self.arcs = {}
        self.mat_adj = np.zeros((n,n))
        self.orientation = orientation
        for e in L:
            self.ajouter_arc(e)

    def ajouter_arc(self, e):
        i, j = e
        if not self.orientation:
            i, j = min(i, j), max(i, j)
        if i not in self.arcs.keys():
            self.arcs[i] = []
        if j not in self.arcs[i]:
            self.arcs[i].append(j)
            self.mat_adj[i,j] = 1

    def enlever_arc(self, e):
        i, j = e
        if not self.orientation:
            i, j = min(i, j), max(i, j)
        if i in self.arcs.keys():
            if j in self.arcs[i]:
                self.arcs[i].remove(j)
                self.mat_adj[i,j] = 0

# 1.3
class Graphe:
    def __init__(self, n, L=[], orientation=True):
        self.nb_sommets = n
        self.arcs = {}
        self.poids = np.zeros((n,n))
        self.orientation = orientation
        for e in L:
            self.ajouter_arc(e)

    def mat_adj(self):
        A = np.copy(self.poids)
        A[A!=0] = 1
        return A

    def ajouter_arc(self, e):
        if len(e) == 3:
            i, j, p = e
        else:
            i, j = e
            p = 1
        if not self.orientation:
            i, j = min(i, j), max(i, j)
        if i not in self.arcs.keys():
            self.arcs[i] = []
        if j not in self.arcs[i]:
            self.arcs[i].append(j)
            self.poids[i,j] = p

    def enlever_arc(self, e):
        i, j = e
        if not self.orientation:
            i, j = min(i, j), max(i, j)
        if i in self.arcs.keys():
            if j in self.arcs[i]:
                self.arcs[i].remove(j)
                self.poids[i,j] = 0

    # def ajouter_arc_bi(self, e):
    #     if len(e) == 2:
    #         e += (1,)
    #     i, j, p = e
    #     if i not in self.arcs.keys():
    #         self.arcs[i] = []
    #     if j not in self.arcs[i]:
    #         self.arcs[i].append(j)
    #         self.poids[i,j] = p
    #         if not self.orientation:
    #             if j not in self.arcs.keys():
    #                 self.arcs[j] = []
    #             self.arcs[j].append(i)
    #             self.poids[j,i] = p
    #
    # def enlever_arc_bi(self, e):
    #     i, j = e
    #     if i in self.arcs.keys():
    #         if j in self.arcs[i]:
    #             self.arcs[i].remove(j)
    #             self.poids[i,j] = 0
    #             if not self.orientation:
    #                 self.arcs[j].remove(i)
    #                 self.poids[j,i] = 0


## Exercice 2

# 2.1
def explore(G, i):
    global ind_ouvert, ind_ferme
    etat[i] = True
    # On indique l'ouverture du sommet i
    pref[i] = ind_ouvert
    ind_ouvert += 1
    for j in G.arcs[i]:
        if not etat[j]:
            # On explore les sommets non explorés
            A.append((i,j))
            explore(G, j)
    # On indique la fermeture du sommet i
    suff[i] = ind_ferme
    ind_ferme += 1

def DFS(G):
    global A, etat, pref, suff, ind_ouvert, ind_ferme
    n = G.nb_sommets
    A = []
    etat = [False]*n
    pref, suff = [0]*n, [0]*n
    ind_ouvert, ind_ferme = 1, 1
    for i in range(n):
        if not etat[i]:
            explore(G,i)

    print('prefixe :', pref)
    print('suffixe :', suff)
    arcs_avant, arcs_arriere, arcs_croises = [], [], []
    for i in G.arcs:
        for j in G.arcs[i]:
            p, s = pref[i]<pref[j], suff[i]<suff[j]
            if p:
                l = arcs_avant
            else:
                l = arcs_arriere if s else arcs_croises
            l.append((i,j))

    print('Ensemble des arcs d\'arbre:', A)
    print('Arcs avant :', arcs_avant)
    print('Arcs arrière :', arcs_arriere)
    print('Arcs croises :', arcs_croises)

# 2.2
n=5
L=[(0,1),(0,3),(1,0),(1,2),(1,4),(2,3),(3,1),(4,2),(4,3)]
G=Graphe(n,L)

DFS(G)