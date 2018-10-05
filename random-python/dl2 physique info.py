import numpy as np
import matplotlib.pyplot as plt
import math

'''
http://pikeroen.free.fr/Site/FB2402D4-CB34-4140-80EF-D1269DF1A259_files/Mod%2017%20CCPc.pdf
'''

V[i,j] #potentiels
rhos[i,j] #dérivées secondes
frontiere[i,j] #booléens

def nouveau_potentiel(V,rhos,fontiere,i,j):
    if !frontiere[i,j]:
        V[i,j]=0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1]+rhos[i,j])
    return V[i,j]

def itere_J(V,rhos,frontiere):
    '''calcul_erreur(V0,V) focntion de calcul d'erreur (suivant la formule donnée)'''
    V0 = np.copy(V)
    for i in range(V.shape[0]):
        for j in range(V.shape[1]):
            V[i,j]=nouveau_potentiel(V0,rhos,frontiere,i,j)
    err = calcul_erreur(V0,V)
    return err

def poisson(f_iter,V,rhos,frontiere,eps):
    err = 2*eps
    while (err>eps):
        err = f_iter(V,rhos,frontiere)

def itere_GS(V,rhos,frontiere):
    V0 = np.copy(V)
    m,n = V.shape
    for i in range(m):
        for j in range(n):
            V[i,j]=nouveau_potentiel(V,rhos,frontiere,i,j)
    return calcul_erreur(V0,V)

def nouveau_potentiel_SOR(V,rhos,frontiere,i,j,omega):
    return (1-omega)*V[i,j]+0.25*omega*nouveau_potentiel(V,rhos,frontiere,i,j)

def itere_SOR(V,rhos,frontiere):
    V0 = np.copy(V)
    m,n = V.shape
    omega = 2/(1+math.pi/n)
    for i in range(m):
        for i in range(n):
            V[i,j]=nouveau_potentiel_SOR(V,rhos,frontiere,i,j,omega)
    return calcul_erreur(V0,V)


def dans_cylindre(x,y,xc,yc,R):
    rs = pow(x-xc,2)+pow(y-yc,2)
    return (rs =< R**2)

eps0,L,N,rho
rhos_cyl,Ex_cyl,Ey_cyl,frontiere_cyl

def initialise_rhos_cylindre(tab_rhos):
    rhos = rho*(L**2)*(h**2)/eps0
    for i in range(N+1):
        for j in range(N+1):
            if (dans_cylindre(i,j,L/2,L/2,L/4):
                tab_rhos[i,j] = rhos

def initialise_frontiere_cylindre(tab_f):
    for i in range(N+1):
        tab_f[i,0]=True
        tab_f[i,N]=True
        tab_f[0,i]=True
        tab_f[N,i]=True

V0,Vp,m,e,rhos_osc,V_osc,Ex_osc,Ey_osc,frontiere_osc

def initialise_frontiere_condensateur(tab_V,tab_f):
    initialise_frontiere_cylindre(tab_f)
    for i in range(10,50): #tube de l'oscillateur
        tab_f[i,40] = True
        tab_V[i,40] = -Vp
        tab_f[i,60] = True
        tab_V[i,60] = Vp

'''
Question 33
'''
v0  = pow(2*e*V0/m,0.5)
dt = L/(200*V0)
lx[0]= 1E-2 ; ly[0] = 5E-2
lvx[0] = V0 ; lvy[0] = 0
