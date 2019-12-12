import numpy as np
import matplotlib.pyplot as plt
import random
import time

import os
os.chdir("/Users/Elie/Documents/Enseignement/1920_CPES2_Python_prof/TDs 19-20/TD_note_19")
from mesFonctionsTri import *


## Question 1

def triBullesK(L, k):
    for i in range(len(L)-k, 0, -1):
        fini = True
        for j in range(i):
            if L[j+k] < L[j]:
                L[j+k], L[j] = L[j], L[j+k]
                fini = False
        if fini:
            return


def triOrdre0(L):
    for k in range(len(L)-1, 0, -1):
        triBullesK(L, k)


## Question 2

def listeAlea(n):
    l=[]
    for i in range(n):
        l.append(random.uniform(-1000,1000))
    return l

L = listeAlea(5000)
t0 = time.time()
triOrdre0(L)
print("Temps d'execution de triOrdre0() :'", time.time() - t0)


## Question 3

def triOrdre1(L, f):
    k = len(L)
    while k > 1:
        k = int(k/f)
        if k <= 1:
            triBullesOpti(L)
        else:
            triBullesK(L, k)

## Question 4

L = listeAlea(5000)
t0 = time.time()
triOrdre1(L, 1.2)
print("Temps d'execution de triOrdre1() :'", time.time() - t0)


## Question 5

def triOrdre2(L, f):
    k = len(L)
    while k > 1:
        k = int(k/f)
        if k <= 1:
            triBullesOpti(L)
        else:
            for i in range(len(L)-k):
                if L[i] > L[i+k]:
                    L[i], L[i+k] = L[i+k], L[i]


## Question 6

L = listeAlea(5000)
t0 = time.time()
triOrdre2(L, 1.2)
print("Temps d'execution de triOrdre2() :'", time.time() - t0)


## Question 7

plt.figure('Question 7')

n = 10000
L = listeAlea(n)
fs = np.arange(1.1, 2.1, .1)
num_fs = len(fs)
tps1 = np.zeros(num_fs)
tps2 = np.zeros(num_fs)
for i in range(num_fs):
    f = fs[i]

    t0 = time.time()
    triOrdre1(L[:], f)
    tps1[i] = time.time()-t0

    t0 = time.time()
    triOrdre2(L[:], f)
    tps2[i] = time.time()-t0

plt.plot(fs, tps1, label='triOrdre1')

plt.plot(fs, tps2, label='triOrdre2')

plt.title("Temps d'execution du tri par ordre pour f de 1.1 a 2.0")
plt.xlabel('f')
plt.ylabel('t')
plt.legend()
plt.show()
plt.savefig('7.png')


## Question 8

plt.figure('Question 8')

n = 10000
fs = np.arange(1.2, 1.42, .02)
num_fs = len(fs)
tps1 = np.zeros(num_fs)
tps2 = np.zeros(num_fs)
reps = 10
for rep in range(reps):
    L = listeAlea(n)
    for i in range(num_fs):
        f = fs[i]

        t0 = time.time()
        triOrdre1(L[:], f)
        tps1[i] += time.time()-t0

        t0 = time.time()
        triOrdre2(L[:], f)
        tps2[i] += time.time()-t0

tps1 /= reps
tps2 /= reps

plt.plot(fs, tps1, label='triOrdre1')

plt.plot(fs, tps2, label='triOrdre2')

plt.title("Temps d'execution moyenne du tri par ordre pour f de 1.2 a 1.4")
plt.xlabel('f')
plt.ylabel('t')
plt.legend()
plt.show()
plt.savefig('8.png')

print("Différence des minima :", min(tps2)-min(tps1))


## Question 9

plt.figure('Question 9')

f = fs[np.argmin(tps2)]
num_tailles = 20
tailles = np.logspace(2, 5, num_tailles, dtype='int')
tps_ord = np.zeros(num_tailles)
tps_rap = np.zeros(num_tailles)
reps = 10
for rep in range(reps):
    for i in range(num_tailles):
        L = listeAlea(tailles[i])

        t0 = time.time()
        triOrdre2(L[:], f)
        tps_ord[i] += time.time()-t0

        t0 = time.time()
        triRapideEnPlace(L[:])
        tps_rap[i] += time.time()-t0

tps_ord /= reps
tps_rap /= reps

plt.plot(tailles, tps_ord, label='ordre')

plt.plot(tailles, tps_rap, label='rapide')

plt.title("Comparaison des temps d'execution du tri par ordre et du tri rapide")
plt.xlabel('n')
plt.ylabel('t')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
plt.savefig('9.png')



## Question 10

def triOrdreInsertion(L, f):
    k = len(L)
    while k > 1:
        k = int(k/f)
        if k <= 1:
            triInsertion(L)
        else:
            for i in range(len(L)-k):
                if L[i] > L[i+k]:
                    L[i], L[i+k] = L[i+k], L[i]

plt.figure('Question 10')

n = 10000
fs = np.arange(1.2, 1.42, .02)
num_fs = len(fs)
tps1 = np.zeros(num_fs)
tps2 = np.zeros(num_fs)
reps = 10
for rep in range(reps):
    L = listeAlea(n)
    for i in range(num_fs):
        f = fs[i]

        t0 = time.time()
        triOrdre2(L[:], f)
        tps1[i] += time.time()-t0

        t0 = time.time()
        triOrdreInsertion(L[:], f)
        tps2[i] += time.time()-t0

tps1 /= reps
tps2 /= reps

plt.plot(fs, tps1, label='triOrdre2')

plt.plot(fs, tps2, label='triOrdreInsertion')

plt.title("Temps d'execution moyenne du tri par ordre pour f de 1.2 a 1.4")
plt.xlabel('f')
plt.ylabel('t')
plt.legend()
plt.show()
plt.savefig('10.png')

print("Différence des minima :", min(tps2)-min(tps1))



## Question 11

plt.figure('Question 11')

f1, f2 = fs[np.argmin(tps1)], fs[np.argmin(tps2)]
num_tailles = 20
tailles = np.logspace(2, 5, num_tailles, dtype='int')
tps_ord = np.zeros(num_tailles)
tps_oi = np.zeros(num_tailles)
tps_rap = np.zeros(num_tailles)
reps = 10
for rep in range(reps):
    for i in range(num_tailles):
        L = listeAlea(tailles[i])

        t0 = time.time()
        triOrdre2(L[:], f1)
        tps_ord[i] += time.time()-t0

        t0 = time.time()
        triOrdreInsertion(L[:], f2)
        tps_oi[i] += time.time()-t0

        t0 = time.time()
        triRapideEnPlace(L[:])
        tps_rap[i] += time.time()-t0

tps_ord /= reps
tps_oi /= reps
tps_rap /= reps

plt.plot(tailles, tps_ord, label='ordre')

plt.plot(tailles, tps_oi, label='insertion')

plt.plot(tailles, tps_rap, label='rapide')

plt.title("Comparaison des temps d'execution du tri par ordre et du tri rapide")
plt.xlabel('n')
plt.ylabel('t')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
plt.savefig('11.png')



## Question 12

def triShell(L, f):
    k = len(L)
    while k > 1:
        k = int(k/f)
        if k <= 1:
            triInsertion(L)
        else:
            for i in range(k, len(L)):
                j = i-k
                while j >= 0 and L[j+k] < L[j]:
                    L[j], L[j+k] = L[j+k], L[j]
                    j -= k


## Question 13

plt.figure('Question 13')

n = 10000
fs = np.arange(2, 3.1, .1)
num_fs = len(fs)
tps = np.zeros(num_fs)
reps = 10
for rep in range(reps):
    L = listeAlea(n)
    for i in range(num_fs):
        f = fs[i]

        t0 = time.time()
        triShell(L[:], f)
        tps[i] += time.time()-t0

tps /= reps

plt.plot(fs, tps, label='Shell')


plt.title("Temps d'execution moyenne du tri Shell pour f de 2.0 a 3.0")
plt.xlabel('f')
plt.ylabel('t')
plt.legend()
plt.show()
plt.savefig('13.png')




## Question 14

plt.figure('Question 14')

f3 = fs[np.argmin(tps)]
num_tailles = 20
tailles = np.logspace(2, 5, num_tailles, dtype='int')
tps_she = np.zeros(num_tailles)
tps_oi = np.zeros(num_tailles)
tps_rap = np.zeros(num_tailles)
reps = 10
for rep in range(reps):
    for i in range(num_tailles):
        L = listeAlea(tailles[i])

        t0 = time.time()
        triShell(L[:], f3)
        tps_she[i] += time.time()-t0

        t0 = time.time()
        triOrdreInsertion(L[:], f2)
        tps_oi[i] += time.time()-t0

        t0 = time.time()
        triRapideEnPlace(L[:])
        tps_rap[i] += time.time()-t0

tps_she /= reps
tps_oi /= reps
tps_rap /= reps

plt.plot(tailles, tps_she, label='shell')

plt.plot(tailles, tps_oi, label='ordre')

plt.plot(tailles, tps_rap, label='rapide')

plt.title("Comparaison des temps d'execution des tris shell, par ordre et rapide")
plt.xlabel('n')
plt.ylabel('t')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
plt.savefig('14.png')