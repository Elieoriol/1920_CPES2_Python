## Exercice 1 : Tri Sélection

def triSelection(T):
    for cpt in range(len(T)-1):
        # on cherche le min de T[cpt:] et sa position
        m = T[cpt]
        indMin = cpt
        for k in range(cpt+1, len(T)):
            if T[k] < m :
                m = T[k]
                indMin = k
        T[cpt], T[indMin] = T[indMin], T[cpt]   # on echange le terme a la position cpt et le min de T[cpt:]


## Exercice 2 : Tri Insertion

def triInsertion(T):
    for i in range(1, len(T)):
        j = i-1
        while j >= 0 and T[j+1] < T[j]:
            T[j], T[j+1] = T[j+1], T[j]   # on echange les elements aux positions j et j+1
            j = j-1


## Exercice 3 : Tri Rapide

# 3.2
import random as rd

def separationEnPlace(S, d, f):
    # on choisit aleatoirement un pivot
    indPivot = rd.randint(d, f)
    pivot = S[indPivot]

    # on construit les listes avec les termes inferieurs, egaux et superieurs au pivot
    moins, egal, plus = [], [], []
    for x in S[d:f+1]:
        if x < pivot:
            moins.append(x)
        elif x == pivot:
            egal.append(x)
        else:
            plus.append(x)
    Sp = moins + egal + plus

    # on remplace la sous-liste entre d et f
    S[d:f+1] = Sp[:]

    return len(moins), len(moins+egal)


# 3.3
def triRapideEnPlace(L, d=0, f=-1):
    # pour eviter de donner d=0, f=len(L)-1 systematiquement
    if f == -1:
        f = len(L)-1

    # condition d'arret : la sous-liste est de longueur 0 ou 1
    if f-d <= 1:
        return

    # on place le(s) pivot, on recupere son (ses) indice(s)
    m, p = separationEnPlace(L, d, f)

    # on trie recursivement les 2 sous-listes separees par le(s) pivot(s)
    triRapideEnPlace(L, d, d+m)
    triRapideEnPlace(L, d+p, f)


# 3.4
import random as rd

def separation(L):
    # on choisit aleatoirement un pivot
    indPivot = rd.randint(0, len(L)-1)
    pivot = L[indPivot]

    # on construit les listes avec les termes inferieurs, egaux et superieurs au pivot
    moins, egal, plus = [], [], []
    for x in L:
        if x < pivot:
            moins.append(x)
        elif x == pivot:
            egal.append(x)
        else:
            plus.append(x)
    return moins, egal, plus

def triRapide(L):
    # condition d'arret : la sous-liste est de longueur 0 ou 1
    if len(L) <= 1:
        return L

    # on recupere les trois sous-listes des elements inferieurs, egaux et superieurs a un pivot de L
    moins, egal, plus = separation(L)

    # on retourne la concatenation de ces 3 sous-listes en triant recursivement les 2 sous-listes moins et plus
    return triRapide(moins) + egal + triRapide(plus)


## Exercice 4 : Tri Fusion

# 4.1
def fusion(L1, L2):
    i, j = 0, 0
    L = []

    # i et j parcourent L1 et L2 respectivement, on ajoute a L les elements de L1 et L2 dans l'ordre croissant
    while i < len(L1) and j < len(L2):
        if L1[i] > L2[j]:
            L.append(L2[j])
            j += 1
        else:
            L.append(L1[i])
            i += 1

    # une liste aura fini d'etre parcourue avant l'autre, on ajoute le reste de cette liste a L
    if i == len(L1):
        L.extend(L2[j:])
    else:
        L.extend(L1[i:])
    return L


# 4.2
def triFusion(L):
    # condition d'arret : la sous-liste est de longueur 0 ou 1
    if len(L) <= 1:
        return L

    # on separe la liste en 2 sous-listes de tailles egales (a 1 pres) et on trie les 2 sous-listes
    moitie = len(L)//2
    L1 = triFusion(L[:moitie])
    L2 = triFusion(L[moitie:])

    # on retourne le resultat de la fusion des sous-listes triees
    return fusion(L1, L2)


## Exercice 5 : Tri à Bulles

# 5.2
def triBulles(L):
    for i in range(len(L)-1, 0, -1):
        for j in range(i):
            if L[j+1] < L[j]:
                L[j+1], L[j] = L[j], L[j+1]


# 5.3
def triBullesOpti(L):
    for i in range(len(L)-1, 0, -1):
        fini = True
        for j in range(i):
            if L[j+1] < L[j]:
                L[j+1], L[j] = L[j], L[j+1]
                fini = False
        if fini:
            return
