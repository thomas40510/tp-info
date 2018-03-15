import numpy as np
from matplotlib import pyplot as plt
'''
Ex. 1

c = np.linspace(-10, 10, 21)
x = np.linspace(-2,2,1000)


def fc(arr,c):
    f = (-np.log(abs(1-arr))+c)/arr
    return f

for i in range(len(c)):
    f = fc(x,c[i])
    plt.plot(x,f)

plt.ylim(-10,10)
plt.show()
'''
'''
Ex. 2

x = [0]
y = [0]

t = np.random.uniform(0,1,1000)
t = 2*np.pi*t

for i in range(0,1000):
    r = np.random.exponential()
    x.append(x[i]+r*np.cos(t[i]))
    y.append(y[i]+r*np.sin(t[i]))

plt.plot(x,y)
plt.show()
'''
'''
Ex. 3
'''
basex = np.array([0,0,4,4,2,2,3,3,1,1,5])
basey = np.array([0,4,4,1,1,2,2,3,3,0,0])

motx=basex
moty=basey



plt.ylim(-8,12)

def translate(motx):
    for i in range(0,15):
        motx = basex+5*i
        plt.plot(motx,moty, color="blue")

translate(motx)
plt.show()
