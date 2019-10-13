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
