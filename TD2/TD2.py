## Exercice 1

d = {
    'nom': 'Dupuis',
    'prenom': 'Jacque',
    'age': 30
}

# 1.1
d['prenom'] = 'Jacques'

# 1.2
print(list(d.keys()))

# 1.3
print(list(d.values()))

# 1.4
print(list(d.items()))

# 1.5
print(d['prenom']+' '+d['nom']+' a '+str(d['age'])+' ans')


## Exercice 2

import numpy as np

# 2.1
def A(n, a):
    mat = np.zeros((n,n))
    for i in range(n-1):
        mat[i][i+1] = 1/a
    for i in range(1, n):
        mat[i][i-1] = a
    return mat

def A2(n, a):
    return np.diag([1/a]*n, 1) + np.diag([a]*n, -1)

# 2.2
def detDict(n_array, a_array):
    dico = {}
    for n in n_array:
        for a in a_array:
            det = round(np.linalg.det(A(n,a)), 3)
            if det not in dico:
                dico[det] = []
            dico[det].append((n,a))
    return dico
n_array, a_array = np.arange(3, 9), [-2, -1, 1, 2, 3]
dico = detDict(n_array, a_array)

# 2.3
def printDet(dico):
    for pair in dico.items():
        print('  ', pair[0], pair[1])
printDet(dico)


## Exercice 3

import matplotlib.pyplot as plt

# 3.1
x=np.array([1,3,4,6])
y=np.array([2,3,5,1])
plt.plot(x,y)
plt.show()

x=np.linspace(0,2*np.pi,30)
y=np.cos(x)
plt.figure('Fonction cosinus')
plt.plot(x,y,label="cos(x)")
plt.title('Fonction cosinus')
plt.show()

# 3.2
def plotFunction(x):
    y = x**3 - 3*x**2 + 2*x + 12
    plt.figure('Fonction personnalisée')
    plt.plot(x, y)
    plt.show()

x = np.linspace(-10, 15, 300)
plotFunction(x)

# 3.3
import random as rd
import math

def piApprox(N):
    x, y = [], []
    n = 0
    for k in range(N):
        x.append(rd.uniform(-1,1))
        y.append(rd.uniform(-1,1))
        if x[-1]**2 + y[-1]**2 <= 1:
            n += 1
    print("Approximation de pi :", 4*n/N)

    plt.figure('Approximation de pi')
    # thetas = np.linspace(0,2*np.pi,200)
    # plt.plot(np.cos(thetas), np.sin(thetas), 'b-')
    x_cercle = np.linspace(-1,1,1000)
    y_cercle = np.sqrt(1-x_cercle**2)
    plt.plot(x_cercle, y_cercle, 'b-')
    plt.plot(x_cercle, -y_cercle, 'b-')
    plt.plot(x, y, 'ro')
    plt.title(str(N)+' points tires aleatoirement')
    plt.xlim((-1.45,1.45))
    plt.show()

N = 200
piApprox(N)

# 3.4
import math

def densitiesXY(N):
    x, y = [], []
    for k in range(N):
        x.append(rd.uniform(-1,1))
        y.append(rd.uniform(-1,1))

    plt.figure('Histogramme de X')
    plt.hist(x, bins=30, density=True)
    plt.plot([-1,1], [.5, .5], 'r')
    plt.show()

    plt.figure('Histogramme de Y')
    plt.hist(y, bins=30, density=True)
    plt.plot([-1,1], [.5, .5], 'r')
    plt.show()

N = 50
densitiesXY(N)

# 3.5
def densitiesR(N):
    r2, r = [], []
    for k in range(N):
        x, y = rd.uniform(-1,1), rd.uniform(-1,1)
        r2.append(x**2+y**2)
        r.append(math.sqrt(r2[-1]))

    plt.figure('Histogramme de R2')
    plt.hist(r2, bins=30, density=True)
    plt.plot([0,1], [math.pi/4, math.pi/4], 'r')
    plt.xlim((0,1))
    plt.show()

    plt.figure('Histogramme de R')
    plt.hist(r, bins=30, density=True)
    plt.plot([0,1], [0, math.pi/2], 'r')
    plt.xlim((0,1))
    plt.show()

N = 50000
densitiesR(N)

# 3.6
def selfHistogram(N, b):
    mu, sigma = 0, 0.25
    dico = {}
    edges = np.arange(-1, 1, b)
    for band in edges:
        dico[band] = 0

    for k in range(N):
        z = rd.gauss(mu,sigma)
        if z < -1 or z > 1:
            continue
        for band in edges[1:-1]:
            if z < band+b:
                dico[band] += 1
                break

    plt.figure('Histogramme à la main')
    plt.bar(edges, np.array(list(dico.values()))/N/b, width=b, align='edge')
    x = np.linspace(-1, 1, 200)
    y = np.exp(-(x-mu)**2/(2*sigma**2))/(math.sqrt(2*math.pi)*sigma)
    plt.plot(x, y, 'r')
    plt.show()

N = 50000
b = .05
selfHistogram(N, b)


## Exercice 4

import numpy as np

def piApproxNP(N):
    r2 = np.random.uniform(-1, 1, size=N)**2 + np.random.uniform(-1, 1, size=N)**2
    n = len(r2[r2<=1])
    print("Approximation de pi :", 4*n/N)

    plt.figure('Approximation de pi')
    plt.plot(np.cos(np.linspace(0,2*np.pi,200)), np.sin(np.linspace(0,2*np.pi,200)))
    plt.plot(x, y, 'ro')
    plt.title(str(N)+' points tires aleatoirement')
    plt.xlim((-1.45,1.45))
    plt.show()

N = 200
piApproxNP(N)


import math

def densitiesXYNP(N):
    x, y = np.random.uniform(-1, 1, size=N), np.random.uniform(-1, 1, size=N)

    plt.figure('Histogramme de X')
    plt.hist(x, bins=30, density=True)
    plt.plot([-1,1], [.5, .5], 'r')
    plt.show()

    plt.figure('Histogramme de Y')
    plt.hist(y, bins=30, density=True)
    plt.plot([-1,1], [.5, .5], 'r')
    plt.show()

N = 50000
densitiesXYNP(N)


def densitiesRNP(N):
    r2 = np.random.uniform(-1, 1, size=N)**2 + np.random.uniform(-1, 1, size=N)**2
    r = np.sqrt(r2)

    plt.figure('Histogramme de R2')
    plt.hist(r2, bins=30, density=True)
    plt.plot([0,1], [math.pi/4, math.pi/4], 'r')
    plt.xlim((0,1))
    plt.show()

    plt.figure('Histogramme de R')
    plt.hist(r, bins=30, density=True)
    plt.plot([0,1], [0, math.pi/2], 'r')
    plt.xlim((0,1))
    plt.show()

N = 50000
densitiesRNP(N)


def selfHistogramNP(N, b):
    mu, sigma = 0, 0.25
    z = np.random.normal(mu, sigma, size=N)
    dico = {}
    edges = np.arange(-1, 1, b)
    for band in edges:
        dico[band] = 0

    for k in range(N):
        if z[k] < -1 or z[k] > 1:
            continue
        for band in edges[1:-1]:
            if z[k] < band+b:
                dico[band] += 1
                break

    plt.figure('Histogramme a la main')
    plt.bar(edges, np.array(list(dico.values()))/N/b, width=b, align='edge')
    x = np.linspace(-1, 1, 200)
    y = np.exp(-(x-mu)**2/(2*sigma**2))/(math.sqrt(2*math.pi)*sigma)
    plt.plot(x, y, 'r')
    plt.show()

N = 50000
b = .05
selfHistogramNP(N, b)


