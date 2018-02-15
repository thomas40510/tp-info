###############################
#      Pivot de Gauss         #
###############################

# A tester sur les cas suivants
# Cas 1
A=[[1,2,3],[4,5,6],[7,8,10]]
B=[1,4,-1]
# solution : -7,16,-8

# Cas 2 (Système 4x4)
# A=[[1,3,5,7],[3,5,7,1],[5,7,1,3],[7,1,3,5]]
# B=[12,0,4,16]
# Solution : [1.0, -1.0, 0.0, 2.0]

############################
#  Fonctions Elémentaires  #
############################

# Affichage d'une matrice 
def Affiche(M):
    nligne=len(M)
    ncolonne=len(M[0])
    for i in range(0,nligne):
        for j in range(0,ncolonne) :
            print(M[i][j],end=' ')
        print()

# Copie d'une matrice
# Ne fonctionne que pour une matrice carrée
def Copie(M):
    n=len(M)
    R=[None]*n
    for i in range(n):
        R[i]=M[i][:]
    return R

# Extraction de la colonne d'une matrice
def Colonne(M,i):
    n=len(M)
    B=[]
    for j in range(0,n):
        B.append(M[j][i])
    return B

# Matrice augmentée
def Augmente(M,N):
    m=len(M)
    n=len(N)
    R=Copie(M) 
    if (m==n) :
        for i in range(0,m):
            R[i].append(N[i])
        return R
    else :
        print("Tailles incompatibles")

# Opérations élémentaires
# Dilatation
def Dilat(M,i,a):
    n=len(M[0])
    R=Copie(M)
    for k in range(0,n):
        R[i][k]=a*R[i][k]
    return R

# Transvection
def Transvec(M,i,j,a):
    n=len(M[0])
    R=Copie(M)
    for k in range(0,n):
        R[j][k]=R[j][k]+a*R[i][k]
    return R

    
# Obtention d'une matrice échelonnée en ligne
def Echelon(M):
    n=len(M)
    R=Copie(M)
    i=0
    j=0
    while i<=n-2 :
        for k in range(i+1,n): 
            a=-R[k][j]/R[i][j]
            R=Transvec(R,i,k,a)
        i=i+1
        j=j+1
    return R

# Normalisation des coefficients diagonaux d'une MEL
def Diagnorm(M):
    n=len(M)
    R=Copie(M)
    for i in range(0,n):
        R=Dilat(R,i,1/R[i][i])
    return R

############################################
# Algorithme du pivot de Gauss à compléter #
############################################

# def Gauss(A,B):
    
