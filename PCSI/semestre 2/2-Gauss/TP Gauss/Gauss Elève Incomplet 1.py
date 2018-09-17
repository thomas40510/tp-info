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


# Opérations élémentaires
# Dilatation
def Dilat(M,i,a):
    n=len(M[0])
    R=Copie(M)
    for k in range(0,n):
        R[i][k]=a*R[i][k]
    return R

# Transvection


    
# Obtention d'une matrice échelonnée en ligne



# Normalisation des coefficients diagonaux d'une MEL



############################################
# Algorithme du pivot de Gauss à compléter #
############################################

# def Gauss(A,B):
    
