import random as rdm


def tri_insert(L):
    T = L[:]
    for i in range(1, len(T)):
        temp = T[i]
        j = i
        while j > 0 and temp < T[j - 1]:
            T[j] = T[j - 1]
            j -= 1
        T[j] = temp
    return T


def fusion(A, B, tab=[]):
    if len(A) == 0 or len(B) == 0:
        return tab + A + B
    if A[0] <= B[0]:
        return fusion(A[1:], B, tab + [A[0]])
    else:
        return fusion(A, B[1:], tab + [B[0]])


def tri_fusion(L):
    if len(L) < 2:
        return L
    else:
        m = len(L) // 2
        return fusion(tri_fusion(L[:m]), tri_fusion(L[m:]))


def tri_rapide(L):
    if len(L) < 2:
        return L
    else:
        inf = []
        sup = []
        pivot = L[0]
        for i in range(1, len(L)):
            if L[i] < pivot:
                inf.append(L[i])
            else:
                sup.append(L[i])
        return tri_rapide(inf) + [pivot] + tri_rapide(sup)


L = [rdm.randrange(1, 21) for i in range(30)]

print(L)
print(tri_insert(L))
print(tri_fusion(L))
print(tri_rapide(L))


def estMin(i, L):
    res = True
    for k in range(len(L)):
        if L[k] < L[i]:
            res = False
    return res


def rechercheMin1(L):
    i_min = 0
    for k in range(len(L)):
        if estMin(k, L):
            i_min = k
    return L[i_min], i_min


print(rechercheMin1(L))


def rechercheMin2(L):
    i_min = 0
    while not estMin(i_min, L):
        i_min += 1
    return L[i_min], i_min


print(rechercheMin2(L))


def rechercheMin3(L):
    min = L[0]
    i_min = 0
    for i in range(len(L)):
        if L[i]<min:
            min = L[i]
            i_min = i
    return min, i_min

print(rechercheMin3(L))


def expoRapide(x, n):
    return x**(n%2)*expoRapide(x,n//2)**2 if n!=0 else 1

print(expoRapide(2,10))
print(pow(2,10))


def mediane(L):
    return tri_rapide(L)[len(L)//2]

print(mediane(L))


def partition(L):
    med = L[0]
    inf, sup = [], []
    for l in L:
        if l < med:
            inf.append(l)
        else:
            sup.append(l)
    return inf, sup

print(partition(L))
