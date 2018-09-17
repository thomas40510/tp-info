import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D


w0 = 1.0
global epsilon, sol
#epsiLs = [0.0,0.5,1.0,1.5,2.0]
epsiLs = np.linspace(0,4,100)
global periodLs
periodLs = []

def f(X,t):
    y,v=X[0],X[1]
    return np.array([v, epsilon*w0*(1-y**2)*v-w0**2*y])

ts = np.linspace(0,30,1000)
'''
for i in range(1,5):
    sol = odeint(f, np.array([i, 0.0]), ts)
    plt.plot(sol[:,0], sol[:,1])
'''

def max_locaux(epsilon):
    maxLs = [0.0]
    absc = sol[:,0]
    for i in range(1,len(absc)-1):
        if absc[i]>absc[i+1] and absc[i]>absc[i-1]:
            maxLs.append(ts[i])
    return maxLs

def periode(epsilon):
    s = 0
    maxLs = max_locaux(epsilon)
    return((maxLs[-1]-maxLs[0])/(len(maxLs)-1))

for i in epsiLs:
    epsilon = i
    sol = odeint(f, np.array([2, 0.0]), ts)
    #plt.plot(ts, sol[:,0])
    periodLs.append(periode(epsilon))
    print(max_locaux(epsilon))
    print("p",periode(epsilon))


plt.plot(epsiLs, periodLs)
plt.show()
