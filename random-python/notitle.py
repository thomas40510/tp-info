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

t = 0
for i in range(1,10000):
    d = 0
    for j in range(1,20):
        import random as rd
        p = rd.randint(0,1)
        if (p==0):
            d+=1
    if (d==10):
        t+=1
print("fréquence :",t/10000)


#print('pgcd =',pgcd())
