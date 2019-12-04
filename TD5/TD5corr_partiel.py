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
