import numpy as np
import math
import matplotlib.pyplot as plt
import numpy.linalg as alg
import numpy.random as rd
from numpy.polynomial import Polynomial

# ORAL CCS Maths 2 : 1er sujet

def somme(n):
    s=0
    for k in range (1,n+1):
        s+=pow(-1,k)*np.log(1+(1/k))
    return(s)

print(somme(1000))
print(np.log(2/(np.pi)))

def somme2(n,x):
    s=0
    for k in range(1,n+1):
        s+=pow(-1,k)*np.log(1+(1/k))*pow(x,k)
        
def f(x):
    s=0
    for k in range(1,1000):
        s+=pow(-1,k)*np.log(1+(1/k))*pow(x,k)
    return(s)
    
X=np.linspace(-1,1,100)
Y=[ f(x) for x in X]
plt.plot(X,Y)
plt.show()

# Oral 2

def matriceA(n):
    M=np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            if i<=j:
                M[i][j]=1/(j+1)
    return(M)
    
def tirages(k,n):
    liste=[]
    boules=n
    for k in range(k+1):
        a=rd.randint(0,boules+2)
        boules=a
        liste.append(a)
    return(liste)
    
#Oral 4 

P = [0] + [1]*[4]
P = Polynomial(P)**3 

















