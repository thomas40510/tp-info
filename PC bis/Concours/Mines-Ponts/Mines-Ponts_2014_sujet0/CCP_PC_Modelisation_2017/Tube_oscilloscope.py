## CCP 2017 Modélisation PC
## Mouvement d'un électron dans un tube d'oscilloscope
## Déviation verticale


## Données physiques à modifier
V0 = 950            # Tension du canal d'accélération (V)
Vp = 180            # Potentiel des plaques de condensateur (V)
D = 7e-2            # Distance écran - centre du condensateur (m)
d = 2e-2            # distance entre les deux plaques du condensateur (m)
l = 4e-2            # longueur des plaques du condensateur (m)
L = 10e-2           # longueur du côté de l'enceinte carrée au potentiel nul (m)
c = 3e-2            # Position du centre des plaques par rapport au côté de
                    # l'enceinte carrée (m)
N = 100             # taille du maillage
eps = 1e-5          # seuil de convergence
# Pour les tracés
n_grille = 5        # nombre de valeurs sur la grille des tracés
n_equip = 40        # nombre d'équipotentielles à tracer

## Constantes
m = 9.11e-31        # masse d'un électron (kg)
e = 1.6e-19         # charge élémentaire (C)
eps0 = 8.85e-12     # epsilon_0

## Conditions initiales du mouvement de l'électron
v0 = pow(2 * e * V0 / m, 0.5)   # vitesse initiale de l'électron
x0 = 0                          # abscisse initiale de l'électron
y0 = L/2                        # ordonnée initiale de l'électron
Npts = 200                      # nbre de pts pour le tracé de la trajectoire
dt = L / (v0 * Npts)            # incrément temporel


## Programme

# Importation des modules
import numpy as np
import matplotlib.pyplot as plt

# tableaux des coordonnées x et y de l'électron
lx = np.zeros(Npts) ; ly = np.zeros(Npts)
# tableaux des vitesses en x et en y
lvx = np.zeros(Npts) ; lvy = np.zeros(Npts)
# conditions initiales
lx[0] = x0 / L ; ly[0] = y0 / L
lvx[0] = v0 ; lvy[0] = 0


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
            # parcours de tout le tableau V
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
def calc_ExEy(Ex, Ey, V, h, L):
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
h = 1 / N           # distance entre deux points consécutifs du maillage
rhos_osc = np.zeros((N + 1, N + 1))
V_osc = np.zeros((N + 1, N + 1))
Ex_osc = np.zeros((N + 1, N + 1))
Ey_osc = np.zeros((N + 1, N + 1))

# frontiere
frontiere_osc = np.zeros((N + 1, N + 1), bool)

# Initialisation des charges et de la frontiere
def initialise_frontiere_condensateur(tab_V, tab_f, L = 10e-2, c = 3e-2, \
l = 4e-2, d = 2e-2, Vp = 180):
    '''Place les points des plaques de condensateur à leur potentiel
    Met à True les points appartenant à la frontière (plaques et enceinte).
    Modification sur place.'''
    nl, nc = tab_f.shape
    # initialisation des plaques de condensateur
    X_gche = int((c - l/2) / L * N)
    X_dte = int((c + l/2) / L * N)
    Y_sup = int((L / 2 + d / 2) / L * N)
    Y_inf = int((L / 2 - d / 2) / L * N)
    for i_abscisse in range(X_gche, X_dte + 1):
        tab_V[i_abscisse, Y_sup] = Vp
        tab_f[i_abscisse, Y_sup] = True
    for i_abscisse in range(X_gche, X_dte + 1):
        tab_V[i_abscisse, Y_inf] = -Vp
        tab_f[i_abscisse, Y_inf] = True
    # initialisation de l'enceinte
    for i_abscisse in range(nl):
        tab_f[i_abscisse, 0] = True
        tab_f[i_abscisse, nc - 1] = True
    for j_ordonnee in range(1, nc - 1):
        tab_f[0, j_ordonnee] = True
        tab_f[nl -1, j_ordonnee] = True


# Simulation numérique du tube d'oscilloscope
initialise_frontiere_condensateur(V_osc, frontiere_osc)
Poisson(iter_SOR, V_osc, rhos_osc, frontiere_osc, eps)
calc_ExEy(Ex_osc, Ey_osc, V_osc, h, L)

# Calcul analytique de la trajectoire de l'électron
Xel_1 = [0, (c - l/2) / L] ; Yel_1 = [1/2, 1/2]   # avant les plaques
Xel_2 = np.linspace((c - l/2) / L, (c + l/2) / L, 200)  # entre les plaques
Yel_2 = [L/2 / L + e * Vp * pow(xi + (l/2 - c) / L, 2) / (m * d * pow(v0, 2)) * L for xi in Xel_2]
Xel_3 = [(c + l/2) / L, 1]
Yel_3 = [L/2 / L + 2 * e * Vp * l * (xi - c / L) / (m * d * pow(v0, 2)) for xi in Xel_3]

# Calcul de la trajectoire de l'électron par la méthode d'Euler
def val_Ex(Ex, Ey, x, y, h, N, L):
    '''retourne la valeur approchée de la composante suivant x du champ 
    électrique E à partir de sa valeur au noeud du maillage proche.
    x, y et h adimensionnés'''
    i, j = int(x / h), int(y / h)
    rx, ry = x - i * h, y - j * h
    return(Ex[i, j] + ((Ex[i + 1, j] - Ex[i, j]) * rx + \
    (Ex[i, j + 1] - Ex[i, j]) * ry) / h)

def val_Ey(Ex, Ey, x, y, h, N, L):
    '''retourne la valeur approchée de la composante suivant y du champ 
    électrique E à partir de sa valeur au noeud du maillage proche.
    x, y et h adimensionnés'''
    i, j = int(x / h), int(y / h)
    rx, ry = x - i * h, y - j * h
    return(Ey[i, j] + ((Ey[i + 1, j] - Ey[i, j]) * rx + \
    (Ey[i, j + 1] - Ey[i, j]) * ry) / h)
    
for k in range(1, Npts):
    lx[k] = lx[k - 1] + dt * lvx[k - 1] / L
    ly[k] = ly[k - 1] + dt * lvy[k - 1] / L
    lvx[k] = lvx[k - 1] + dt * (-e/m) * \
    val_Ex(Ex_osc, Ey_osc, lx[k - 1], ly[k - 1], h, N, L)
    lvy[k] = lvy[k - 1] + dt * (-e/m) * \
    val_Ey(Ex_osc, Ey_osc, lx[k - 1], ly[k - 1], h, N, L)


## Tracé du champs électrostatique
############################
# Pour respecter les indices i et j initiaux, les tableaux sont ordonnés de telle
# sorte que les lignes représentent les abscisses et les colonnes les 
# ordonnées.Il faut donc transposer les tableaux de résultat avant le tracé.
V_osc_T = np.transpose(V_osc)
############################
X = np.linspace(0, 1, N + 1)
Y = np.linspace(0, 1, N + 1)
plt.figure('Simulation_electrostatique_oscilloscope', figsize = (10, 10))
plt.title('Simulation numérique champs électrostatique oscilloscope')
# Tracé équipotentielles
XY = np.meshgrid(X, Y)
fig = plt.contour(X, Y, V_osc_T, 28)
plt.clabel(fig, inline = True, fontsize = 10)
plt.xlabel(r'$x(m)$')
x_valeurs = [k / (n_grille - 1) for k in range(n_grille)]
x_etiquettes = [str(round(L * k / (n_grille - 1), 2)) for k in range(n_grille)]
plt.xticks(x_valeurs, x_etiquettes)
plt.ylabel(r'$y(m)$')
plt.yticks(x_valeurs, x_etiquettes)
# Tracé des plaques
plt.plot([(c - l/2) / L, (c + l/2) / L], [(L/2 - d/2) / L, (L/2 - d/2) / L], \
color = 'black', linewidth = 2.5)
plt.plot([(c - l/2) / L, (c + l/2) / L], [(L/2 + d/2) / L, (L/2 + d/2) / L], \
color = 'black', linewidth = 2.5)
# Tracé de la trajectoire approchée analytiquement de l'électron
plt.plot(Xel_1, Yel_1, color = 'blue', linewidth = 2)
plt.plot(Xel_2, Yel_2, color = 'blue', linewidth = 2)
plt.plot(Xel_3, Yel_3, color = 'blue', linewidth = 2, label = 'trajectoire analytique')
# Tracé de la trajectoire simulée de l'électron
plt.plot(lx, ly, color = 'red', linewidth = 2, label = 'trajectoire numérique')

plt.legend(loc = 'lower right')
plt.grid(linestyle = '--')
plt.show()



