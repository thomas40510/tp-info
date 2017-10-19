
'''
Ex. 1

l=[2,3,5]
L=[1,3,5,7]
 
def estCroissant(L):
    for i in range(0, len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True

def isArithmetic (L):
    for i in range(0,len(L)-2):
        n = L[i+1]-L[i]
        x = L[i+2]-L[i+1]
        if n!=x:
            return False

    return (True, n)
'''

'''
Ex. 2


from random import randrange as rr

def lancer():
    i = rr(6)+1
    return i

def liste_lancers(n):
    for k in range(n):
        print(rr(5)+1)

def is6():
    i=0
    while i!=6:
        i = lancer()
        print (i)
    return True
'''

'''
Ex. 3


a="aeiouyâêîôûàéèioù"

def isConsonne(c):
    return (c not in a) and c!=" "

def isVoyelle(c):
    return c in a

def trad(text):
    L = list(text)
    for n in range (len(L)-1):
        if (isConsonne(L[n]) and isVoyelle(L[n+1])):
            L[n]+="av"
    return ''.join(L)
'''

'''
Ex. 4
'''

def isPrime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True

def isPrime2(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i == 0):
            return False
    return True

def Verif(n):
    for i in range(n+1):
        print((i,isPrime(i),isPrime2(i)))
