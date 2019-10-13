import os
os.chdir("C:/Users/Elie/Documents/Enseignement/1920_CPES2_Python_prof/TDs 19-20/TD4")

from mesFonctionsTri import *

## Exercice 1 : Tri Sélection

T = [9,3,12,5,1]
triSelection(T)
print("Selection :", T)

## Exercice 2 : Tri Insertion

T = [9,3,12,5,1]
triInsertion(T)
print("Insertion :", T)


## Exercice 3 : Tri Rapide

# 3.3
T = [9,3,12,5,1]
triRapideEnPlace(T)
print("Rapide (en place) :", T)
