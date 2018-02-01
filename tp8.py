from math import e
from math import exp
import numpy as np
from matplotlib import pyplot as plt

'''
Ex. 1


def f(x):
    return e**x

def rectangles(f,a,b,n):
    sum=0
    k=(b-a)/n
    for i in range(0,n):
        sum+=f(i/n)
    return (k*sum)


def trapezes(f,a,b,n):
    sum=f(a)+f(b)
    k = (b-a)/(2*n)
    for i in range(1,n):
        sum+=2*f(i/n)
    return (k*sum)



print(rectangles(f,0,1,1000000))
print(trapezes(f,0,1,1000000))
print(e-1)
'''
'''
Ex. 2
'''

l = np.linspace(-2,7,1000)

plt.plot(l,e**l-1)
plt.plot(l,l)
plt.xlim(-2.5,6)
plt.ylim(-2,6)

a=[-1.7]
u=[-1.7]
n=1
for i in range(0,12):
    t = e**a[i]-1
    if (n==1):
      a.append(a[i])
      u.append(t)
      n=2
    else :
        a.append(t)
        u.append(u[i])
        n=1
b=[0.35]
v=[0.35]
n=1
for i in range(0,12):
    t = e**b[i]-1
    if (n==1):
      b.append(b[i])
      v.append(t)
      n=2
    else :
        b.append(t)
        v.append(v[i])
        n=1
    
plt.plot(a,u)
plt.plot(b,v)
plt.show()



