import matplotlib.pyplot as plt
import numpy as np

t_exp = [i for i in range(50)]
kla=2
Fa_exp = [2*n-1 for n in range(50)]

def f(a,b):
    return a+b-a*b

def smc(kla, t_exp, Fa_exp1):
    s=0
    for i in range(len(t_exp)):
        s+=pow(Fa_exp1[i]-f(t_exp[i], kla), 2)
    return s

def smc2(kla, t_exp, Fa_exp1):
    n = len(t_exp)
    s = sum(pow(Fa_exp1[i]-f(t_exp[i], kla), 2) for i in range(len(t_exp)))
    return s

def z(x):
    return ((1-((3**0.5)/2)**x)/(1-(3**0.5/2)))*(8*3**0.5)/3

def sinc(x):
    return np.sin(x)/x

x = np.linspace(-2e-2,2e-2,1000)
l = 0.02e-3
lbda = 630e-9
a = 0.2e-3
D = 1

def Ir(x):
    return (1)/(D**2 + x**2)*pow(sinc((np.pi*l)/(lbda*D)*x),2)*pow(np.cos((np.pi*a)/(lbda*D)*x),2)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def plotI():
    plt.plot(x,Ir(x))
    plt.xlabel(r'\Large{$x$ (m)}')
    plt.ylabel(r'\Large{$I_r (4{E_0}^2)$}')
    plt.show()

def m(x):
    s = 0
    for i in x :
        s+=i
    return s/len(x)

def sigma(x):
    sc = 0
    for i in x:
        sc+= (i-m(x))**2
    sg = sc/(len(x)-1)
    return pow(sg,0.5)

def incert(x):
    u = 2*sigma(x)/pow(len(x),0.5)
    return (str(m(x))+" +/- "+str(u))

I0 = 5
I = I0*(1+np.cos(2*np.pi*(a*x)/(D*lbda)))

# plt.plot(x,I)
# plt.xlabel(r'\Large{$x$ (m)}')
# plt.ylabel(r'\Large{$I$}')
# plt.show()

# x = [65,66,61,62,61,63,59,65,60,63]
# print(len(x))
# print(sigma(x))
#
# print(incert(x))
def tableau(x_max, N, P) :
    T = np.zeros((N, P)) # initialisation du tableau
    X = np.linspace(0, x_max, P) # valeurs de x
    b = 0.2e-3 # valeur de b
    Y =2 + np.cos(2*np.pi*X)+ np.cos(2*np.pi*(X+b)) # ligne des valeurs de y
    for i in range(0, N) : T[i] = Y # remplissage avec des lignes identiques
    return T
N, P = 1000, 1000 # dimensions du tableau de valeurs
x_max = 10 # trac´e sur [0, x max[
plt.matshow(tableau(x_max, N, P),
cmap=plt.cm.gray, vmin = 0, vmax = 4)
# plt.cm.gray est la palette de couleurs en niveau de gris
# plt.cm.gray r donne la mˆeme en n´egatif
# vmin et vmax permettent de choisir les valeurs extrˆemes
plt.colorbar(shrink=0.7)
# affichage optionnel de l’´echelle de correspondance
# shrink permet de r´egler la taille de la barre
#plt.axis("off") # ne pas afficher les axes de coordonn´ees
plt.show()
