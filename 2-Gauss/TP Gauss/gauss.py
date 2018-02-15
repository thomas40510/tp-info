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
def augmente(A,B):
    C = Copie(A)
    if (len(B)!=len(A)):
        return "error"
    else :
        for i in range(len(A)):
            C[i].append(B[i])
        return C

# Opérations élémentaires
# Dilatation
def Dilat(M,i,a):
    n=len(M[0])
    R=Copie(M)
    for k in range(0,n):
        R[i][k]=a*R[i][k]
    return R

# Transvection
def transvec(M,i,j,a):
    C = Copie(M)
    for k in range(len(C[j])):
        C[j][k] = C[j][k]+a*C[i][k]
    return C

# Obtention d'une matrice échelonnée en ligne

def echelon(M) :
    C = Copie(M)
    i = 0
    j = 0
    while (i<=len(M)-2):
        for k in range(i+1,len(M)):
            C = transvec(C,i,k,-(C[k][j]/C[i][j]))
        i+=1
        j+=1
    return C
# Normalisation des coefficients diagonaux d'une MEL

def diagnorm(M):
    C=Copie(M)
    for i in range(0,len(C)):
        C=Dilat(C,i,1/C[i][i])
    return C


############################################
# Algorithme du pivot de Gauss à compléter #
############################################

# def Gauss(A,B):
def gauss(A,B):
    C = augmente(A,B)
    S = diagnorm(echelon(C))
    j = len(S[0])-2
    print(S)
    print(S[1][2])
    for i in range(len(S)-1,0,-1):
        print('done', i,j)
        a = S[i-1][j]
        b = S[len(S)][j]
        print(a,b)
        S = transvec(S,i,i-1,-a/b)
    print(S)
