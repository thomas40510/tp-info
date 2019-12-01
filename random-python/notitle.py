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

I0 = 10
l1 = 589.6
l2 = 589
s1 = 1/l1
s2 = 1/l2
s0 = (s1+s2)/2
ds = s2-s1
dp = 2*np.pi

def I(x):
    return 4*I0*(1+np.cos(dp*np.rad2deg(x)*s0)*np.cos(dp*np.rad2deg(x)*0.5*ds))
x = np.linspace(-10000,10000,100000)
plt.plot(x,I(x))
plt.plot(x,4*I0*(1+np.cos(dp*np.rad2deg(x)*ds/2)))
#plt.plot(x,4*I0*np.cos(dp*x*s0)+4*I0)
plt.show()



# print('pgcd =',pgcd())
