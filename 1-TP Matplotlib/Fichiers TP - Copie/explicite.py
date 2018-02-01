#-------------------------------------------------------------------------------
#             Exemple de tracé explicite d'une fonction f(u)
#              Utilisation de la bibliothèque "pylab"
#-------------------------------------------------------------------------------

# Importation de pylab
from pylab import *

l=1000
a = 300
b = 150

# définition de la fonction (relation explicite) de la forme f(u)
def f(l,teta):
   return 2*l*sin(teta)
def Lambda(l,teta,a,b):
   return ((l-a-b)**2+4*b*(l-a)*(sin(teta))**2)**0.5

def course(Y,teta):
   tmin, tmax = 0,0
   for i in range(len(teta)-1):
      if (f(l,teta[i])<=200 and f(l,teta[i+1])>=200):
         tmin=teta[i]
      elif (f(l,teta[i])<=1700 and f(l,teta[i+1])>=1700):
         tmax=teta[i]
   print(int(Lambda(l,tmax,a,b)-Lambda(l,tmin,a,b)))

# définition de la grille en X et calcul des valeurs de Y correspondantes
X   = linspace(-10, 10, 500)
teta = linspace(0,pi/2,1000)
Y   = f(l,teta)
L = Lambda(l,teta,a,b)

# tracé de la fonction

plot(L,Y , color='blue',linewidth=2)
lsp = linspace(550,775,1000)
plot(lsp,len(lsp)*[200],'--')
plot(lsp,len(lsp)*[1700],'--')

lsp = linspace(200,1700,1000)
plot(len(lsp)*[550],lsp,'--')
plot(len(lsp)*[775], lsp, '--')

# habillage
xlabel('abscisses x')
ylabel('ordonnées y')
title('y=f(x)')
xticks(arange(500,850,50))
yticks(arange(0, 2000 , 250))
grid()



show()
course(L,teta)
