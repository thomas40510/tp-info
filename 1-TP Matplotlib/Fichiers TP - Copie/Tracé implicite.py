#-------------------------------------------------------------------------------
#      Exemple de tracé implicite d'une relation entre 2 variables (x,y)
#              avec utilisation de la fonction "contour" du module "pyplot"
#              de la bibliothèque "matplotlib"
#-------------------------------------------------------------------------------

# Importation des modules
from pylab import *
from mpl_toolkits.mplot3d import *  # Axes3D

# définition de la relation implicite entre (x,y)
def relation(x, y):
   return sqrt(x**2+y**2)

# définition de la grille en (x,y) avec un même "pas" de discrétisation
pas = 0.3
x   = arange(-5, 5 + pas, pas)
y   = arange(-5, 5 + pas, pas)
X,Y = meshgrid(x, y)
Z=relation(X,Y)

# tracé en 3D
fig1 = figure(1)    # Fenêtre vide - conteneur
ax = Axes3D(fig1)
ax.plot_surface(X,Y,Z, rstride=1,cstride=1,cmap=cm.jet)


# tracé de la courbe de niveau (=0)
figure(2)
axis("equal")
contour(X, Y, Z, levels=[2],colors='red')
grid()

show()
