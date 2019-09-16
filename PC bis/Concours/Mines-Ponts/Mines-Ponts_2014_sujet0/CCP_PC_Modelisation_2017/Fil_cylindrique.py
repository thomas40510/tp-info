## CCP 2017 Modélisation PC
## Fil cylindrique


## Données physiques à modifier
Re = 0.05           # rayon extérieur du fil cylindrique
Ri = 0.025         # rayon intérieur du fil cylindrique
L = 4 * Re          # Largeur du maillage
eps0 = 8.85e-12     # epsilon_0
rho = 1e-5          # densité volumique de charge rho
N = 100             # taille du maillage
eps = 1e-5          # seuil de convergence
# Pour les tracés
n_grille = 5        # nombre de valeurs sur la grille des tracés
n_equip = 17        # nombre d'équipotentielles à tracer
Vmin = 0            # Valeur mini tracé du potentiel
Vmax = 1200         # Valeur maxi tracé du potentiel
Emin = -30000       # Valeur mini tracé du champ électrique
Emax = +30000       # Valeur maxi tracé du champ électrique

## Programme

# Importation des modules
import numpy as np
import matplotlib.pyplot as plt


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
                somme_ek += (V[i, j] - Vk) ** 2
                N += 1
    return(pow(somme_ek, 0.5) / N)

# Résolution de l'équation de Poisson
def Poisson(f_iter, V, rhos, frontiere, eps):
    '''fonction qui modifie sur place V, elle ne renvoie donc rien.'''
    while f_iter(V, rhos, frontiere) > eps:
        None
    
# Détermination du champ électrique
def calc_ExEy(Ex, Ey, V, h, L = 0.2):
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
            
    

## Simulation numérique

# Initialisation du calcul
h = 1 / N           # pas adimensionnel
rhos_cyl = np.zeros((N + 1, N + 1))
V_cyl = np.zeros((N + 1, N + 1))
Ex_cyl = np.zeros((N + 1, N + 1))
Ey_cyl = np.zeros((N + 1, N + 1))

# frontiere
frontiere_cyl = np.zeros((N + 1, N + 1), bool)

# Initialisation des charges et de la frontiere
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

def dans_cylindre_creux(x, y, xc, yc, Ri, Re, L):
    '''renvoie un booléen indiquant si le point de coordonnées (x, y) est à l'intérieur ou sur le bord du cercle de centre (xc, yc) et de rayon R.'''
    ri = Ri / L     # adimensionnalisation de Ri
    re = Re / L     # adimensionnalisation de Re
    return ( ri ** 2 <= (y - yc) ** 2 + (x - xc) ** 2 <= re ** 2 )

def initialise_rhos_cylindre_creux(tab_rhos, N = 100, L = 0.2, Re = 0.05, \
eps0 = 8.85e-12, rho = 1e-5, Ri = 0.025):
    '''initialise le tableau tab_rhos contenant les valeurs de la densité volumique de charge adimensionnée rho_ad = rho * (L ** 2) * pas / eps0. Modification sur place'''
    pas = 1 / N     # pas spatial
    rho_ad = rho * (L ** 2) * (pas ** 2) / eps0  # rho adimensionnée
    for i_abscisse in range(N + 1):
        for i_ordonnee in range(N + 1):
            if dans_cylindre_creux(i_abscisse * pas, i_ordonnee * pas, \
            pas * (N + 1) / 2, pas * (N + 1) / 2, Ri, Re, L) :
                tab_rhos[i_abscisse, i_ordonnee] = rho_ad
                

# Simulation numérique du fil cylindrique creux
initialise_frontiere_cylindre(frontiere_cyl)
initialise_rhos_cylindre_creux(rhos_cyl, N, L, Re, eps0, rho, Ri)
Poisson(iter_SOR, V_cyl, rhos_cyl, frontiere_cyl, eps)
calc_ExEy(Ex_cyl, Ey_cyl, V_cyl, h)


## Tracé

############################
# Pour respecter les indices i et j initiaux, les tableaux sont ordonnés de telle
# sorte que les lignes représentent les abscisses et les colonnes les 
# ordonnées.Il faut donc transposer les tableaux de résultat avant le tracé.
V_cyl_T = np.transpose(V_cyl)
Ex_cyl_T = np.transpose(Ex_cyl)
############################
X = np.linspace(0, 1, N + 1)
Y = np.linspace(0, 1, N + 1)
plt.figure('Simulation_electrostatique_fil_creux', figsize = (14, 4))
plt.title('Simulation numérique champs électrostatique par un fil creux')
# Tracé équipotentielles
plt.subplot(1, 3, 1)
plt.title('équipotentielles')
XY = np.meshgrid(X, Y)
fig = plt.contour(X, Y, V_cyl_T, n_equip)
plt.clabel(fig, inline = True, fontsize = 10)
plt.xlabel(r'$x(m)$')
x_valeurs = [k / (n_grille - 1) for k in range(n_grille)]
x_etiquettes = [str(round(L * k / (n_grille - 1), 2)) for k in range(n_grille)]
plt.xticks(x_valeurs, x_etiquettes)
plt.ylabel(r'$y(m)$')
plt.yticks(x_valeurs, x_etiquettes)
# Tracé Potentiels
plt.subplot(1, 3, 2)
plt.title('V(x, y  = L/2) (V)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs, x_etiquettes)
plt.plot(X, V_cyl_T[:, (N + 1) // 2])
plt.grid(linestyle = '--')
plt.xlim([0, 1])
plt.ylim([Vmin, Vmax])
# Tracé Champs électrique
plt.subplot(1, 3, 3)
plt.title('E(x, y = L/2) (V/m)')
plt.xlabel(r'$x(m)$')
plt.xticks(x_valeurs,x_etiquettes)
plt.plot(X, Ex_cyl[:, (N + 1) // 2])
plt.grid(linestyle = '--')
plt.xlim([0, 1])
plt.ylim([Emin, Emax])

plt.show()