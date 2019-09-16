## Sujet mines ponts zéro
##########################

## importation des modules
###########################

import random as rd
import matplotlib.pyplot as plt
import pixel as px

## définition des fonctions
############################

def calcul_n(h):
    '''renvoie le nombre de grains qui vont tomber sur la pile suivante,
pour h entier naturel.'''
    if h > 1:
        return( int( (h + 2.0) / 2 * rd.random() ) + 1 )
    else :
        return(0)

def initialisation(P):
    '''renvoie une variable piles de type liste
contenant P piles de hauteur 0.'''
    return( [0] * P )

def actualise (piles, H, perdus):
    '''revoie la variable piles acutalisée selon les règles d'évolution
affichée avec une hauteur H ainsi que le nombre de grain perdus.'''
    
    for i in range(len(piles) - 1):
        
        n = calcul_n( piles[i] - piles[i + 1] )
        piles[i] -= n
        piles[i + 1] += n

        for k in range(n):
            # On met à jour l'affichage des piles 0 à (n-2)
            px.marquer( i, H - piles[i] - (k + 1), 1 )
            px.marquer( i + 1, H - piles[i + 1] + n - (k + 1), 0 )
            px.afficher( 0.1 )
            
    np = calcul_n(piles[-1])
    perdus += np
    piles[-1] -= np
    
    for k in range(np):
        # On met à jour l'affichage de la dernière pile (n - 1)
        px.marquer((len(piles) - 1),  \
                   H - piles[-1] - (k + 1), 1)
        px.afficher(0.1)
    return(piles, perdus)

def automate(P, arret):
    '''gère l'automate et renvoie les piles à l'état final.'''
    piles = initialisation(P)
    perdus = 0
    H = int(1.2 * P)
    px.initialiser(P, H, 200 // P)
    10
    while True :
        piles[0] += 1
        # On affiche le nouveau grain
        px.marquer(0, H - piles[0], 0)
        px.afficher(0.1)
        
        for i in range(50):
            piles, perdus = actualise(piles, H, perdus)                       
                        
            if perdus > arret :
                # permet de s'arrêter dès que 1000 grains sont sortis
                return(piles, perdus)
        

## programme principal
#######################

piles_finales = automate( int(input("Taille du support ? ")), \
                          int(input("Nombre de grains perdus avant arrêt ? ")) )

# px.afficher()
