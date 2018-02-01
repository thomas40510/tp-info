#-------------------------------------------------------------------------------
#      Exemple de tracé implicite d'une relation entre 2 variables (x,y)
#              avec utilisation de la fonction "contour" du module "pyplot"
#              de la bibliothèque "matplotlib"
#-------------------------------------------------------------------------------

# Importation des modules
from pylab import *
from mpl_toolkits.mplot3d import *  # Axes3D

d = 45
r = 65
l = 45
h = 65

# définition de la relation implicite entre (x,y)
def relation(x, t):
   return ((x-d+r*sin(t))**2+(r*cos(t)-h)**2)**0.5

def explicit(x,t):
   a=[]
   l = relation(x,t)
   for i in range(len(l)-1):
      a.append((l[i+1]-l[i]))
   print(average(a))
      

# définition de la grille en (x,y) avec un même "pas" de discrétisation
pas = 0.3
x   = linspace(-50, 150, 500)
#y   = arange(-60, 60+pas, pas)
y = linspace(-pi/4, pi/4, 500)
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

explicit(x,y)
#show()
