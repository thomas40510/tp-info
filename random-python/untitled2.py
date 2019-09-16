import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from math import pi

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

# x = [65,66,61,62,61,63,59,65,60,63]
# print(len(x))
# print(sigma(x))
#
# print(incert(x))
