## CCP 2017 Modélisation PC
## Corrigé

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt



# Méthode de Jacobi

def nouveau_potentiel(V, rhos, frontiere, i, j):
    '''renvoie le nouveau potentiel au point (i,j) in [1, N - 1]^2'''
    return( (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1] + \
    rhos[i, j]) / 4 )

def iter_J(V, rhos, frontiere):
    somme_ek, N = 0, 0  # initialisations du calcul de l'erreur
    taille = len(V)     # taille du tableau V
    Vk = np.copy(V)
    for i in range(taille):
        for j in range(taille):
            # parcourt de tout le tableau V
            if not frontiere[i, j]:
                # le point (i, j) n'est pas sur la frontière
                V[i, j] = nouveau_potentiel(Vk, rhos, frontiere, i, j)
                # le calcul d'erreur ne se fait que sur les points 
                # hors frontière
                somme_ek += (V[i, j ] - Vk[i, j]) ** 2
                N += 1
    return(pow(somme_ek / N, 0.5))

def Poiss(f_iter, V, rhos, frontiere, eps):
    '''fonction qui modifie sur place V, elle ne renvoie donc rien.'''
    erreur = f_iter(V, rhos, frontiere)
    while erreur > eps:
        erreur = f_iter(V, rhos, frontiere)

def Poisson(f_iter, V, rhos, frontiere, eps):
    '''fonction qui modifie sur place V, elle ne renvoie donc rien.'''
    while f_iter(V, rhos, frontiere) > eps:
        None

# Méthode de Gauss-Seidel

def iter_GS(V, rhos, frontiere):
    somme_ek, N = 0, 0  # initialisations du calcul de l'erreur
    taille = len(V)     # taille du tableau V
    for i in range(taille):
        for j in range(taille):
            # parcourt de tout le tableau V
            if not frontiere[i, j]:
                # le point (i, j) n'est pas sur la frontière
                Vk = V[i, j]    # mémorisation de V_k[i, j]
                V[i, j] = nouveau_potentiel(V, rhos, frontiere, i, j)
                # le calcul d'erreur ne se fait que sur les points 
                # hors frontière
                somme_ek += (V[i, j ] - Vk) ** 2
                N += 1
    return(pow(somme_ek / N, 0.5))

# Méthode de Gauss-Seidel adaptative

def nouveau_potentiel_SOR(V, rhos, frontiere, i, j, omega):
    '''renvoie le nouveau potentiel au point (i,j) in [1, N - 1]^2'''
    return( (1 - omega) * V[i, j] + omega * \
    (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1] + rhos[i, j]) / 4 )

def iter_SOR(V, rhos, frontiere):
    somme_ek, N = 0, 0  # initialisations du calcul de l'erreur
    nl, nc = V.shape     # dimensions du tableau V
    omega_opt = 2 / (1 + np.pi / (nl - 1))
    for i in range(nl):
        for j in range(nc):
            # parcourt de tout le tableau V
            if not frontiere[i, j]:
                # le point (i, j) n'est pas sur la frontière
                Vk = V[i, j]    # mémorisation de V_k[i, j]
                V[i, j] = nouveau_potentiel_SOR(\
                V, rhos, frontiere, i, j, omega_opt)
                # le calcul d'erreur ne se fait que sur les points 
                # hors frontière
                somme_ek += (V[i, j ] - Vk) ** 2
                N += 1
    return(pow(somme_ek / N, 0.5))
    
# Détermination du champ électrique

def calc_ExEy(Ex, Ey, V, h, L = .2):
    nl, nc = V.shape
    # Calcul du champ aux bords
    for j in range(nc):
        # Ex(0,j)
        Ex[0, j] = - ( V[1, j] - V[0, j] ) / ( h * L )
    for j in range(nc):
        # Ex(N,j)
        Ex[N, j] = - ( V[N, j] - V[N - 1, j] ) / ( h * L )
    for i in range(nl):
        # Ex(i,0)
        Ex[i, 0] = - ( V[i, 1] - V[i, 0] ) / ( h * L )
    for i in range(nl):
        # Ex(i,N)
        Ex[i, N] = - ( V[i, N] - V[i, N - 1] ) / ( h * L )
    # Calcul du champ hors bords
    for i in range(1, nl - 1):
        for j in range(1, nc - 1):
            Ex[i, j] = - ( V[i + 1, j] - V[i - 1, j] ) / ( 2 * h * L )
            Ey[i, j] = - ( V[i, j + 1] - V[i, j - 1] ) / ( 2 * h * L )
            
    
## Fil cylindrique chargé uniformément

# Données physiques
R = 0.05            # rayon du fil cylindrique
L = 4 * R           # Largeur du maillage
eps0 = 8.85e-12     # epsilon_0
rho = 1e-5          # densité volumique de charge rho

# Etude theorique
def E(r, eps0 = 8.85e-12, rho = 1e-5, R = 0.05):
    if r <= R :
        return(rho * r / (2 * eps0))
    else :
        return(rho * pow(R, 2) / (2 * r * eps0))

# # Tracé de la courbe représentative de E(r)
# r_ab = np.linspace(0, 10 * R, 2000)
# E_ord = [E(ri, eps0, rho, R) for ri in r_ab]
# plt.figure('Profil_E')
# plt.title(r'Profil du champs électrique')
# plt.xlabel(r'$r$')
# x_valeurs = [0, R, 2 * R, 5 * R, 10 * R]
# x_etiquettes = [r'$0$'] + [ r'$R$', r'$2 \times R$', r'$5 \times R$', r'$10 \times R$']
# plt.xticks(x_valeurs, x_etiquettes)
# plt.ylabel(r'$E(r)$')
# plt.plot(r_ab, E_ord)
# plt.plot([R, R], [0, E(R)], color = 'black', linestyle = ':')
# plt.grid()
# plt.savefig('Profil_E.png')
# plt.show()

# Initialisation du calcul
N = 100             # taille du maillage
h = L / N           # distance entre deux points consécutifs du maillage

rhos_cyl = np.zeros((N + 1, N + 1))
V_cyl = np.zeros((N + 1, N + 1))
Ex_cyl = np.zeros((N+ 1, N+ 1))
Ey_cyl = np.zeros((N+ 1, N+ 1))

# frontiere
frontiere_cyl = np.zeros((N + 1, N+1), bool)

# Initialisation des charges et de la frontiere

def dans_cylindre(x, y, xc, yc, R):
    '''renvoie un booléen indiquant si le point de coordonnées (x, y) est à l'intérieur ou sur le bord du cercle de centre (xc, yc) et de rayon R.'''
    return ( (y - yc) ** 2 + (x - xc) ** 2 <= R ** 2 )

def initialise_rhos_cylindre(tab_rhos, N = 100, L = 0.2, R = 0.05, \
eps0 = 8.85e-12, rho = 1e-5):
    '''initialise le tableau tab_rhos contenant les valeurs de la densité volumique de charge adimensionnée rho_ad = rho * (L ** 2) * pas / eps0. Modification sur place'''
    pas = L / N     # pas spatial
    rho_ad = rho * (L ** 2) * (pas ** 2) / eps0  # rho adimensionnée
    for i_abscisse in range(N + 1):
        for i_ordonnee in range(N + 1):
            if dans_cylindre(i_abscisse * pas, i_ordonnee * pas, \
            pas * (N + 1) / 2, pas * (N + 1) / 2, R) :
                tab_rhos[i_abscisse, i_ordonnee] = rho_ad

def initialise_frontiere_cylindre(tab_f):
    '''met à True les points appartenant à la frontière. 
    Modification sur place.'''
    nl, nc = tab_f.shape
    for i_abscisse in range(nl):
        tab_f[i_abscisse, 0] = True
        tab_f[i_abscisse, nc - 1] = True
    for j_ordonnee in range(1, nc - 1):
        tab_f[0, j_ordonnee] = True
        tab_f[nl - 1, j_ordonnee] = True

# Simulation numérique du fil cylindrique plein
eps = 1e-5
initialise_rhos_cylindre(rhos_cyl)
initialise_frontiere_cylindre(frontiere_cyl)
Poisson(iter_SOR, V_cyl, rhos_cyl, frontiere_cyl, eps)
calc_ExEy(Ex_cyl, Ey_cyl, V_cyl, h)

# # Tracé Potentiels
# plt.figure('Potentiels')
# X = np.linspace(0, L, N + 1)
# Y_V = V_cyl[:, (N + 1) // 2]
# plt.title('V(x, y  = L/2) (V)')
# plt.xlabel(r'$x(m)$')
# x_valeurs = [0.05 * k for k in range(5)]
# x_etiquettes = ['0.00', '0.05', '0.10', '0.15', '0.20']
# plt.xticks(x_valeurs, x_etiquettes)
# plt.ylabel('')
# plt.plot(X, Y_V)
# plt.grid()
# plt.show()

# # Tracé Champs électrique
# plt.figure('Champs_electrique')
# X = np.linspace(0, L, N + 1)
# Y_E = Ex_cyl[:, (N + 1) // 2]
# plt.title('E(x, y = L/2) (V/m)')
# plt.xlabel(r'$x(m)$')
# plt.xticks(x_valeurs,x_etiquettes)
# plt.plot(X, Y_E)
# plt.grid()
# plt.show()

# # Tracé équipotentielles
# plt.figure('Equipotentielles_lignes')
# X = np.linspace(0, L, N + 1)
# Y = np.linspace(0, L, N + 1)
# XY = np.meshgrid(X, Y)
# fig = plt.contour(X, Y, V_cyl, 17)
# plt.clabel(fig, inline = True, fontsize = 10)
# plt.show()
# plt.figure('Equipotentielles_surfaces')
# X = np.linspace(0, L, N + 1)
# Y = np.linspace(0, L, N + 1)
# XY = np.meshgrid(X, Y)
# fig = plt.contourf(X, Y, V_cyl)
# plt.clabel(fig, inline = True, fontsize = 10)
# plt.show()

# Tracés
X = np.linspace(0, L, N + 1)
Y = np.linspace(0, L, N + 1)
plt.figure('Simulation_electrostatique_fil_plein', figsize = (14, 4))
plt.title('Simulation numérique champs électrostatique par un fil')
# Tracé équipotentielles
plt.subplot(1, 3, 1)
plt.title('équipotentielles')
XY = np.meshgrid(X, Y)
fig = plt.contour(X, Y, V_cyl, 17)
plt.clabel(fig, inline = True, fontsize = 10)
plt.xlabel(r'$x(m)$')
x_valeurs = [0.05 * k for k in range(5)]
x_etiquettes = ['0.00', '0.05', '0.10', '0.15', '0.20']
plt.xticks(x_valeurs, x_etiquettes)
plt.ylabel(r'$y(m)$')
plt.yticks(x_valeurs, x_etiquettes)
# Tracé Potentiels
plt.subplot(1, 3, 2)
plt.title('V(x, y  = L/2) (V)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs, x_etiquettes)
plt.plot(X, V_cyl[:, (N + 1) // 2])
plt.grid(linestyle = '--')
# Tracé Champs électrique
plt.subplot(1, 3, 3)
plt.title('E(x, y = L/2) (V/m)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs,x_etiquettes)
plt.plot(X, Ex_cyl[:, (N + 1) // 2])
plt.grid(linestyle = '--')
plt.show()


# Simulation numérique du fil cylindrique creux
eps = 1e-5
Re = 0.05
peau = 1/2  # rapport (Re - Ri) / Re
Ri = Re - peau * Re

rhos_cyl_creux = np.zeros((N + 1, N + 1))
V_cyl_creux = np.zeros((N + 1, N + 1))
Ex_cyl_creux = np.zeros((N+ 1, N+ 1))
Ey_cyl_creux = np.zeros((N+ 1, N+ 1))

def dans_cylindre_creux(x, y, xc, yc, Ri, Re):
    '''renvoie un booléen indiquant si le point de coordonnées (x, y) est à l'intérieur ou sur le bord du cercle de centre (xc, yc) et de rayon R.'''
    return ( Ri ** 2 <= (y - yc) ** 2 + (x - xc) ** 2 <= Re ** 2 )

def initialise_rhos_cylindre_creux(tab_rhos, N = 100, L = 0.2, Re = 0.05, \
eps0 = 8.85e-12, rho = 1e-5, Ri = 0.025):
    '''initialise le tableau tab_rhos contenant les valeurs de la densité volumique de charge adimensionnée rho_ad = rho * (L ** 2) * pas / eps0. Modification sur place'''
    pas = L / N     # pas spatial
    rho_ad = rho * (L ** 2) * (pas ** 2) / eps0  # rho adimensionnée
    for i_abscisse in range(N + 1):
        for i_ordonnee in range(N +
         1):
            if dans_cylindre_creux(i_abscisse * pas, i_ordonnee * pas, \
            pas * (N + 1) / 2, pas * (N + 1) / 2, Ri, Re) :
                tab_rhos[i_abscisse, i_ordonnee] = rho_ad

initialise_rhos_cylindre_creux(rhos_cyl_creux)
Poisson(iter_SOR, V_cyl_creux, rhos_cyl_creux, frontiere_cyl, eps)
calc_ExEy(Ex_cyl_creux, Ey_cyl_creux, V_cyl_creux, h)

# Tracés
X = np.linspace(0, L, N + 1)
Y = np.linspace(0, L, N + 1)
plt.figure('Simulation_electrostatique_fil_creux', figsize = (14, 4))
plt.title('Simulation numérique champs électrostatique par un fil creux')
# Tracé équipotentielles
plt.subplot(1, 3, 1)
plt.title('équipotentielles')
XY = np.meshgrid(X, Y)
fig = plt.contour(X, Y, V_cyl_creux, 17)
plt.clabel(fig, inline = True, fontsize = 10)
plt.xlabel(r'$x(m)$')
x_valeurs = [0.05 * k for k in range(5)]
x_etiquettes = ['0.00', '0.05', '0.10', '0.15', '0.20']
plt.xticks(x_valeurs, x_etiquettes)
plt.ylabel(r'$y(m)$')
plt.yticks(x_valeurs, x_etiquettes)
# Tracé Potentiels
plt.subplot(1, 3, 2)
plt.title('V(x, y  = L/2) (V)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs, x_etiquettes)
plt.plot(X, V_cyl_creux[:, (N + 1) // 2])
plt.grid(linestyle = '--')
# Tracé Champs électrique
plt.subplot(1, 3, 3)
plt.title('E(x, y = L/2) (V/m)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs,x_etiquettes)
plt.plot(X, Ex_cyl_creux[:, (N + 1) // 2])
plt.grid(linestyle = '--')
plt.show()