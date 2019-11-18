import random as rdm

def tri_insert(L):
    T = L[:]
    for i in range(1, len(T)):
        temp = T[i]
        j = i
        while j>0 and temp<T[j-1]:
            T[j] = T[j-1]
            j-=1
        T[j] = temp
    return T

def fusion(A,B,tab = []):
    if len(A) == 0 or len(B) == 0:
        return (tab+A+B)
    if A[0]<=B[0]:
        return fusion(A[1:], B, tab+[A[0]])
    else:
        return fusion(A, B[1:], tab+[B[0]])

def tri_fusion(L):
    if len(L)<2:
        return L
    else:
        m = len(L)//2
        return (fusion(tri_fusion(L[:m]), tri_fusion(L[m:])))



L = [rdm.randrange(1,11) for i in range(10)]

print(L)
print(tri_insert(L))
print(tri_fusion(L))
