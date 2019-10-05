## Exercice 1

# 1
def sommeRec(n):
    if n == 0:
        return 0
    return n + sommeRec(n-1)
print(sommeRec(100))

# 2
def sommeRecBornes(debut, fin):
    if debut == fin:
        return debut
    return fin + sommeRecBornes(debut, fin-1)
print(sommeRecBornes(50, 100))

def sommeRecBornes2(debut, fin):
    if debut == fin:
        return debut
    return debut + sommeRecBornes2(debut+1, fin)
print(sommeRecBornes2(50, 100))


## Exercice 2

# 1
def FibIt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    k = 2
    a, b = 0, 1
    while k <= n:
        tmp = a + b
        a = b
        b = tmp
        k += 1
    return b


def FibIt2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    k = 2
    a, b = 0, 1
    while k <= n:
        a, b = b, a+b
        k += 1
    return b

# 2
def FibRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FibRec(n-1)+FibRec(n-2)

# 3
import time
print("\t35\t\t\t70")
t0 = time.time()
FibIt(35)
t1 = time.time()
FibIt(70)
t2 = time.time()
print("FibIt\t"+str(t1-t0)+"\t"+str(t2-t1))

# Commenté car trop long à éxécuter
# t0 = time.time()
# FibRec(35)
# t1 = time.time()
# FibRec(70)
# t2 = time.time()
# print("FibRec\t"+str(t1-t0)+"\t"+str(t2-t1))

# 4
def Fib2Rec(n):
    return Fib2RecLoop(n,0,1)

def Fib2RecLoop(n, a, b):
    if n == 1:
        return b
    return Fib2RecLoop(n-1,b,a+b)

print("\t\t35\t\t\t\t\t\t70")
t0 = time.clock()
Fib2Rec(35)
t1 = time.clock()
Fib2Rec(70)
t2 = time.clock()
print("Fib2Rec\t"+str(t1-t0)+"\t"+str(t2-t1))

def Fib2Rec2(n):
    return Fib2RecLoop(n, [0,1])

def Fib2Rec2Loop(n, t):
    if len(t) == n:
        return t[-1]
    t.append(t[-2]+t[-1])
    return Fib2RecLoop(n, t)


## Exercice 3

def calcDiff(t):
    if len(t) == 1:
        return t[0]
    diff = []
    for k in range(len(t)-1):
        diff.append(t[k+1]-t[k])
    return calcDiff(diff)

t = [3, 5, 10]
print(calcDiff(t))


## Exercice 4

# 1
def powerIt(a, n):
    mult = a
    for k in range(n-1):
        mult *= a
    return mult

# 2
def powerRec(a, n):
    global c
    c += 1
    if n == 0:
        return 1
    return a*powerRec(a, n-1)

# 3
def power2Rec(a, n):
    global c
    c += 1
    if n == 0:
        return 1
    if n%2 == 0:
        return power2Rec(a, n//2)**2
    else:
        return a*power2Rec(a, (n-1)//2)**2

# 4
a, N = 2, 30
print("Rec1")
for k in range(N+1):
    c = 0
    print(powerRec(a,k), "\t", c)
print("\nRec2")
for k in range(N+1):
    c = 0
    print(power2Rec(a,k), "\t", c)


