"""Équation de la diffusion thermique à deux dimensions
Resolution numérique utilisant une méthode de différences finies.
Le domaine spatial d'intégration est rectangulaire."""

import numpy as np
import matplotlib.pyplot as plt
# de vieux "trucs" qui ne fonctionnent plus....
#if 'qt' in plt.get_backend().lower():
# try:
# from PyQt4 import QtGui
# except ImportError:
# from PySide import QtGui
from PyQt5 import QtWidgets
# Paramètres physiques
K = 0.5 # Diffusivité thermique
lambdat =0.1 # Conductivité thermique
Lx = 1.0 # Dimension du domaine en x
Ly = 2.0 # Dimension du domaine en y
Time = 0.4 # Durée totale d'intégration
# Paramètres numériques
NT = 8000 #Nombre de pas temporels
NX = 100 #Nombre de points dans la direction x
NY = 100 #Nombre de points dans la direction y
dt = Time/NT #Pas temporel élémentaire (temps)
dx = Lx/(NX-1) #Pas de la grille dans la direction x
dy = Ly/(NY-1) #Pas de la grille dans la direction y
xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)
plt.ion()
plt.figure()
### MAIN PROGRAM ###
# Terme de source ; ici il est mis à zéro
S = np.zeros((NY,NX))
# Température initiale
T = np.zeros((NY,NX))
# RHS = Right Hand Side = Membre de droite de l'équation
# RHS = np.zeros((NX,NY))
# Initialisation du tableau jQ ; on l'initialise à zéro.
# En fait seuls les "bords" de ce tableau vont servir -> à améliorer
jQ = np.zeros((NY,NX))
# Conditions aux limites :
# elles peuvent être, sur chaque frontière
# (et même en chaque point de chaque frontière, mais on ne poussera pas ici le raffinement
# à ce point), de deux types différents. Soit on fixe la
# température, soit on fixe la densité de flux thermique.
# On initialise des grandeurs pour les deux conditions (conditions
# bien évidemment incompatibles). On n'utilisera pour chaque frontière qu'une
# seule des deux conditions ; le choix sera fait plus loin dans la boucle principale

# Ici nous allons fixer la température T sur les bords ; ces valeurs ne seront pas modifiées par la suite, ce qui correspond
# à une condition de température fixée et constante sur les frontières (contact avec un thermostat)
# bord gauche
T[:,0] = np.zeros((NY))
# bord haut
T[-1,:] = np.zeros((1,NX))
# bord droit
T[:,-1] = np.zeros((NY))
# bord bas
T[0,:] = np.zeros((1,NX))
# Ici nous allons fixer la densité de flux thermique jQ sur les bords
# ces valeurs ne seront pas modifiées par la suite, ce qui correspond
# à un flux fixé et constant sur les frontières. Les valeurs ont déjà été fixées à zéro
# plus haut (ce qui correspond à une face isolée thermiquement) ; ces lignes ne sont
# donc vraiment utiles que si on fixe le flux à une valeur différente de zéro.
# bord gauche
jQ[:,0] = np.zeros((NY))
# bord haut
jQ[-1,:] = np.zeros((1,NX))
# bord droit
jQ[:,-1] = np.zeros((NY))
# bord bas
jQ[0,:] = np.ones((1,NX))
# On peut ici éventuellement rajouter une zone "source" (siège de réactions exo-
# ou endo-thermiques
# S[30:35,30:35] = 100*np.ones((5,5))
# Boucle principale
for n in range(0,NT):
    RHS = S[1:-1,1:-1]*dt + K*dt*( (T[2:,1:-1]-2*T[1:-1,1:-1]+T[:-2,1:-1])/(dy**2) + (T[1:-1,2:]-2*T[1:-1,1:-1]+T[1:-1,:-2])/(dx**2) )
    T[1:-1,1:-1] += RHS
# C'est dans les quatre lignes qui suivent que l'on choisit la condition aux limites
# finalement retenue pour chacune des quatre frontières.
# Si la ligne correspondante est commentée, c'est la température qui est fixée sur la
# frontière.
# Si la ligne n'est pas commentée, c'est le flux thermique qui est fixé
# (et la température de la frontière est alors modifiée).
    T[:,0] = T[:,1]+dx/lambdat*jQ[:,0] # bord gauche
    T[-1,:] = T[-2,:]-dy/lambdat*jQ[-1,:] # bord haut
    T[:,-1] = T[:,-2]-dx/lambdat*jQ[:,-1] # bord droit
    T[0,:] = T[1,:]+dy/lambdat*jQ[0,:] # bord bas
#Plot every 100 time steps
    if (n%100 == 0):
        plotlabel = "t = %1.2f" %(n * dt)
        # vmin=0 et vamx=1 sont absolument nécessaires pour "calibrer" l'échelle des couleurs,
        # sinon elle va de la température min à la température max,et ce, à chaque date t fixée :
        # si par exemple, on fixe T initiale à 0 partout et les 4 bords à 1, on ne verra JAMAIS
        # le centre se "réchauffer" si on ne met pas cette option.
        # Par contre cette option poserait un problème si on devait aboutir à des températures qui sortent
        # de cet intervalle (ce qui est possible si on fixe non pas T sur un bord mais jQ) :
        # à revoir donc, dans ce cas
        plt.pcolormesh(xx,yy,T, shading='gouraud',cmap='rainbow',vmin=0,vmax=1)
        plt.title(plotlabel)
        plt.axis('image')
        plt.draw()
        if 'qt' in plt.get_backend().lower():
         QtWidgets.QApplication.processEvents()
plt.show()
