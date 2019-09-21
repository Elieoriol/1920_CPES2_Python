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
    thetas = np.linspace(0,2*np.pi,200)
    plt.plot(np.cos(thetas), np.sin(thetas))
    plt.plot(x, y, 'ro')
    plt.title(str(N)+' points tires aleatoirement')
    plt.xlim((-1.45,1.45))
    plt.show()

N = 200
piApprox(N)

