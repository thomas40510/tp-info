import numpy as np
import matplotlib.pyplot as plt

def calc_norme(x):
    return None

def CalcTkp1(M,d):
    return None

def schema_implicite(T0, ItMax = 2000, Dt = 0.05, e = 7e-3, Lambda = 0.192, Rho = 960, c = 2180, T_int = 310, T_ext = 283, epsilon = 1e-2):
    '''renvoie le nombre d'itérations effectuées et une matrice de N+2 lignes contenant les températures à l'instant k en chaque point déclaré de la paroi par la méthode des différences
    finies en utilisant un schéma implicite.'''

    Alpha = Rho * c / Lambda
    N = len(T0)-2
    Dx = e/(N+1)
    r = Dt/(Alpha*pow(Dx, 2))

    if (r>0.5) :
        raise Exception('''r doit être inférieur à 0.5''')

    T_tous_k = np.zeros((N + 2, ItMax + 1))
    T_tous_k[:,0] = T0[:] # question (ii)

    # question (iii)
    T_tous_k[0,1:] = (ItMax-1) * [T_int]
    T_tous_k[N+1,1:] = (ItMax-1) * [T_ext]

    # question (iv)
    M = np.zeros((N+2,N+2))
    for i in range(N+2):
        M[i,i] = 1+2*r
        if i!=0 :
            M[i,i-1] = -r
            M[i-1,i] = -r
        v = np.zeros((N+2,1))
        v[0] = T_int
        v[-1] = T_ext

        # question (v)
        k = 1
        T_tous_k[:,k] = CalcTkp1(M,T_tous_k[:,0] + r*v[:,0]))[:,0]

        while (calc_norme(T_tous_k[:,k]-T_tous_k[:,k-1])>=1e-2 and k < ItMax):
            k+=1
            T_tous_k[:,k] = CalcTkp1(M,T_tous_k[:,k-1] + r*v[:,0])[:,0]

        # question (vi)
        return (k, T_tous_k)

# programme principal

# question a.
epais = 7e-3
conduc = 0.192
rho = 960
Cp = 2180
T_int = 310.15 # 37 celsius
T_ext1 = 293.15 # 20 celsius
T_ext2 = 283.15 # 10 celsius
N = 60
Dt = 0.05

# question b.
a = (T_ext1-T-int)/epais
b = T_int

# question c.
Dx = epais/(N+1)
x = [i*Dx for i in range(1,N+2)]

# question d.
T0 = [a*x[i] + b for i in range(N+1)]

# question e.
alpha = rho*c/conduc
r = Dt/(alpha*pow(Dx,2))

# question 2.

print('Quelle méthode préférez-vous ? [1] implicite ; [2] explicite')
pref = 0
while pref not in (1,2):
    pref = int(input("Votre choix (1 ou 2) : "))

if pref == 1:
    nbIter, T_tous_k = schema_implicite(T0, epais, alpha, Dt, T_int, T_ext2)
else :
    nbIter, T_tous_k = schema_explicite(T0, epais, alpha, Dt, T_int, T_ext2)

# question 3.
for i in range(nbIter//100):
    plt.plot(x, T_tous_k[:,k])

plt.title('RP atteint en '+nbIter * Dt +'secondes')
plt.show()





x = np.zeros((10,10))
print(x)
x[:,0] = 10*[1]
print(x)
x[0,1:] = 9*[2]
print(x)
x[9, 1:] = 9*[3]
print(x)
