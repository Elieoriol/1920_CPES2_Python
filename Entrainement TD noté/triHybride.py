import math
import random
import os
import matplotlib.pyplot as plt
import time

os.chdir("C:/Users/Elie/Documents/Enseignement/1920_CPES2_Python_prof/TDs 19-20/TD_note_18")
from mesFonctionsTri import *

## Tri Hybride


def listeAlea(n):
    l=[]
    for i in range(n):
        l.append(random.uniform(-1000,1000))
    return l

def triHybrideEnPlace(L, n0, d=0, f=-1):
    # pour eviter de donner d=0, f=len(L)-1 systematiquement
    if f == -1:
        f = len(L)-1

    if f-d < n0:
        Lp = L[d:f+1]
        triInsertion(Lp)
        L[d:f+1] = Lp
    else:
        m, p = separationEnPlace(L, d, f)
        triHybrideEnPlace(L, n0, d+p, f)
        triHybrideEnPlace(L, n0, d, d+m)


def triHybride(L, n0):
    if len(L) < n0:
        Lp = L[:]
        triInsertion(Lp)
        return Lp
    else:
        moins, egal, plus = separation(L)
        return triHybride(moins, n0) + egal + triHybride(plus, n0)


n = 50000
L = listeAlea(n)
tps = []
n0s = range(1, 31, 3)
for n0 in n0s:
    t0 = time.time()
    triHybride(L[:], n0)
    tps.append(time.time()-t0)

plt.plot(n0s, tps, label='basique')

print(min(tps)-tps[0])


def triHybrideVarianteLoop(L, n0):
    if len(L) < n0:
        return L

    moins, egal, plus = separation(L)
    return triHybrideVariante(moins, n0) + egal + triHybrideVariante(plus, n0)

def triHybrideVariante(L, n0):
    Lp = triHybrideVarianteLoop(L, n0)
    triInsertion(Lp)
    return Lp

tps_var = []
for n0 in n0s:
    t0 = time.time()
    triHybrideVariante(L[:], n0)
    tps_var.append(time.time()-t0)

plt.plot(n0s, tps_var, label='variante')
plt.legend()
plt.show()