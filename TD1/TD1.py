import os
os.chdir("...")

## Exercice 1

# 1.1
def fib(file, n):
    f = open(file, 'w')
    fib_tab = [0]
    f.write(str(0))
    if n >= 1:
        fib_tab.append(1)
        f.write("\n" + str(1))
    if n > 1:
        for k in range(2, n):
            fib_tab.append(fib_tab[-2] + fib_tab[-1])
            f.write("\n" + str(fib_tab[-1]))
    f.close()

fib('fib20.txt', 20)


# 1.2
def fibError(file, error_file):
    f1, f2 = open(file, 'r'), open(error_file, 'r')
    l1, l2 = f1.readlines(), f2.readlines()
    for k in range(len(l1)):
        if l1[k] != l2[k]:
            break
    f1.close()
    f2.close()
    return k, int(l2[k])-int(l1[k])

idx, error = fibError('fib20.txt', 'fib20_erreur.txt')
print("Index :", idx)
print("Erreur :", error)

# 1.3
def fibLine(file, n):
    f = open(file, 'w')
    fib_tab = [0]
    f.write(str(0))
    if n >= 1:
        fib_tab.append(1)
        f.write(' ' + str(1))
    if n > 1:
        for k in range(2, n):
            fib_tab.append(fib_tab[-2] + fib_tab[-1])
            f.write(' ' + str(fib_tab[-1]))
    f.close()

fibLine('fib20_line.txt', 20)

# 1.4
def fibLineError(file, error_file):
    f1, f2 = open(file, 'r'), open(error_file, 'r')
    l1, l2 = f1.readline().split(' '), f2.readline().split(' ')
    for k in range(len(l1)):
        if l1[k] != l2[k]:
            break
    f1.close()
    f2.close()
    return k, int(l2[k])-int(l1[k])

idx, error = fibLineError('fib20_line.txt', 'fib20_erreur_line.txt')
print("Index :", idx)
print("Erreur :", error)


## Exercice 2

# 2.1
def occurencesDelete(L):
    x = int(input('Quelle valeur voulez-vous supprimer ? '))
    i = 0
    while i < len(L):
        if L[i] == x:
            L.pop(i)
        else:
            i += 1

L = [0,1,2,0,0,4]
occurencesDelete(L)
print(L)

# Complexite en O(n^2) car n iterations et l’appel a pop est en O(n)

def occurencesDelete2(L):
    x = int(input('Quelle valeur voulez-vous supprimer ? '))
    while x in L:
        L.remove(x)

L = [0,1,2,0,0,4]
occurencesDelete2(L)
print(L)

# Solution alternative, mais aussi complexite en O(n^2) car au pire des cas, le "x in L" parcourt la longueur de la liste, et le "L.remove(x)" aussi


# 2.2
def occurencesDeleteON(L):
    x = int(input('Quelle valeur voulez-vous supprimer ? '))
    Lp = []
    for c in L:
        if c != x:
            Lp.append(c)
    return Lp

L = [0,1,2,0,0,4]
L = occurencesDeleteON(L)
print(L)

# Complexité en O(n) car on parcourt une fois la liste


## Exercice 3

# 3
def strReverse():
    s = input("Veuillez entrer une chaine de caracteres : ")
    split_s = s.split(' ')
    split_s.reverse()
    return ' '.join(split_s)

print(strReverse())


## Exercice 4

# 4.1
def filtrage(Lr):
    c = 0
    while c < len(Lr):
        if Lr[c] < 0:
            Lr.pop(c)
        else:
            c += 1

Lr = [-2.3,5,-9,0,12.5,-6]
print("Liste avant filtrage : ", Lr)
filtrage(Lr)
print("Liste apres filtrage : ", Lr)

# 4.2
def consFiltrage(Lr):
    f_Lr = []
    for x in Lr:
        if x >= 0:
            f_Lr.append(x)
    return f_Lr

Lr = [-2.3,5,-9,0,12.5,-6]
print("Liste avant filtrage : ", Lr)
cons_Lr = consFiltrage(Lr)
print("Liste apres filtrage : ", cons_Lr)


## Exercice 5

# 5.1
def somme(c):
    return sum(c)

def coupeMin1(S):
    m = S[0]
    for i in range(len(S)):
        for j in range(i, len(S)):
            s = somme(S[i:j+1])
            if s < m:
                m = s
    return m

S = [2,-6,4,5,-10,-3,2]
print(coupeMin1(S))

# 5.2
def coupei(S):
    m = S[0]
    s = m
    for k in S[1:]:
        s += k
        if s < m:
            m = s
    return m

def coupeMin2(S):
    m = S[0]
    for i in range(len(S)):
        mi = coupei(S[i:])
        if mi < m:
            m = mi
    return m

S = [2,-6,4,5,-10,-3,2]
print(coupeMin2(S))

# 5.3
def coupeMin3(S):
    v = S[0]
    m = v
    for i in range(1, len(S)):
        m = min(m+S[i], S[i])
        v = min(v, m)
    return v

S = [2,-6,4,5,-10,-3,2]
print(coupeMin3(S))

# 5.4
import time
import random
sizes = [100 + k*500 for k in range(4)]
print("\tAlgorithme naif\t\tAlgorithme optimise\tAlgorithme lineaire")
for s in sizes:
    seq = [random.randint(-10, 10) for k in range(s)]
    t0 = time.time()
    coupeMin1(seq)
    t1 = time.time()
    coupeMin2(seq)
    t2 = time.time()
    coupeMin3(seq)
    t3 = time.time()
    print(str(s)+"\t"+str(t1-t0)+"\t"+str(t2-t1)+"\t"+str(t3-t2))


