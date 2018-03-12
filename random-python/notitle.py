import random as rd

alpha='azertyuiopqsdfghjklmwxcvbn'

def shakespeare(n):
    t=''
    l=[]
    for i in range(n):
        c = rd.randrange(26)
        l.append(alpha[c])
    return(t.join(l))
    #return (l.count(t))

a = 0
while a==0:
    s = shakespeare(100000)
    print(s)
    a = s.count("hamlet")
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

print('pgcd =',pgcd())
