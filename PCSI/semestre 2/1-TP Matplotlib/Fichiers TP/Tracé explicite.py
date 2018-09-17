#-------------------------------------------------------------------------------
#             Exemple de tracé explicite d'une fonction f(u)
#              Utilisation de la bibliothèque "pylab"
#-------------------------------------------------------------------------------

# Importation de pylab
from pylab import *


# définition de la fonction (relation explicite) de la forme f(u)
def f(u):
   return u*sin(u**2)

# définition de la grille en X et calcul des valeurs de Y correspondantes
X   = linspace(-10, 10, 500)
Y   = f(X)

# tracé de la fonction

plot(X, Y, color='blue',linewidth=2)

# habillage
xlabel('abscisses x')
ylabel('ordonnées y')
title('y=f(x)')
xticks(arange(-10, 15 , 5))
yticks([-10,-5,0,5,10])
grid()

show()
