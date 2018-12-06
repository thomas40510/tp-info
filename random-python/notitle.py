import random as rd
import numpy as np
import time
import sys

alpha='azertyuiopqsdfghjklmwxcvbn'

def shakespeare(n):
    t=''
    l=[]
    for i in range(n):
        c = rd.randrange(26)
        l.append(alpha[c])
    return(t.join(l))
    #return (l.count(t))
def search(word):
    a = 0
    i=0
    while a==0:
        s = shakespeare(10000)
        print(s)
        a = s.count(word)
        i+=1
    print(i*10000)
    print(a)
#print(shakespeare(1000000).count("hello"))

def pgcd():
    a,b = 0,0
    p = 1
    while a>=b:
        a = int(input('entrer a :'))
        b = int(input('entrer b :'))
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            p = i
    return p

def f(n):
    a=['x']
    for u in range(1,n+1):
        a.append(u)
    print(a)
    b = a
    for i in range(1,n+1):
        b[0]=i
        for y in range(1,n+1):
            b[y]=a[y]*a[i]
        print(b)

def divs(n):
    a = [1]
    for i in range (2,n//2):
        if (n%i==0):
            a.append(i)
    a.append(n)
    print(a)


#print('pgcd =',pgcd())
