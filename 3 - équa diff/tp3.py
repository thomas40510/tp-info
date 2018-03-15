import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

'''
#Ex. 1

w0=np.sqrt((9.81/0.1))
Wc = 2*w0
T0 = 2*np.pi/w0

def f(X,t):
    t = X[0]
    w = X[1]
    return (np.array([w,-9.81/0.1*np.sin(t)]))
    #return (np.array([w,-9.81/0.1*t]))

    
def euler(f,y0,t0,t1,h):
    t = t0
    Y = y0
    ts = []
    Ys = []
    while(t<=t1):
        ts.append(t)
        Ys.append(Y)
        Y = Y+h*f(Y,t)
        t+=h
    return np.array(ts), np.array(Ys)
    
for i in range(1,6):
    t,Y = euler(f,np.array([0,i*Wc/5]),0,2*T0,T0/1000)
    plt.plot(Y[:,0],Y[:,1])
    
#plt.plot(t,Y[:,0])

plt.show()
'''
'''
#Ex. 2
'''

sigma = 10
rho = 28
beta = 8/3

def g(X,t):
    x,y,z=X[0],X[1],X[2]
    return np.array([sigma*(y-x),rho*x-y-x*z, x*y-beta*z])

ts = np.linspace(0,100,10000)

sol = odeint(g, np.array([1.0, 1.0, 1.0]), ts)
solp = odeint(g, np.array([1+1e-9, 1, 1]),ts)

#plt.plot(ts,sol[:,0])
#plt.plot(ts,solp[:,0])

plt.figure()
plt.gca(projection='3d')
plt.plot(sol[:,0],sol[:,1],sol[:,2])
plt.plot(solp[:,0],solp[:,1],solp[:,2])
plt.show()
