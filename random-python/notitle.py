import random as rd
import numpy as np
import matplotlib.pyplot as plt

alpha = 'azertyuiopqsdfghjklmwxcvbn'


def shakespeare(n):
    t = ''
    l = []
    for i in range(n):
        c = rd.randrange(26)
        l.append(alpha[c])
    print(t.join(l))
    return (t.join(l))
    # return (l.count(t))


def search(word):
    a = 0
    i = 0
    while a == 0:
        s = shakespeare(10000)
        print(s)
        a = s.count(word)
        i += 1
    print(i * 10000)
    print(a)


#print(shakespeare(1000000).count("hamlet"))

def pgcd():
    a, b = 0, 0
    p = 1
    while a >= b:
        a = int(input('entrer a :'))
        b = int(input('entrer b :'))
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            p = i
    return p

x = [i for i in range(-5,19)]
y = [-0.3*k**2-4*k+10 for k in x]

plt.title('titre')
plt.plot(x,y,'ro:', ms=4, label='courbe')
plt.xlabel('labelx')
plt.ylabel("ylabel")
plt.axis('equal')
plt.grid()
plt.show()




# print('pgcd =',pgcd())
