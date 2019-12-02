import numpy as np
import matplotlib.pyplot as plt

#\ddot(theta) = -g/l sin(theta)
#T = 2*pi*sqrt(l/g)

pi = np.pi
dpi = 2*pi

def eqdf(theta, l=1, g=9.81):
    return -g/l * np.sin(np.rad2deg(theta))

def EQDF(Y, eqdf, l=1, g=9.81):
    return (np.array([Y[1], eqdf(Y[0], l, g)]))

def create_time(N, l=1, g=9.81, n=1000):
    return (np.linspace(0,N*dpi*pow(l/g, 0.5), n))

def euler_explicite(eqdf, T, g=9.81, l=1, theta0=0):
    Theta = [theta0]
    for i in range(1,len(T)):
        Theta.append(Theta[i-1] + (T[i]-T[i-1])*eqdf(Theta[i-1]))
    return Theta

def Euler_vect(Theta0, eqdf, T, g=9.81, l=1):
    Theta = [Theta0]
    for i in range(1,len(T)):
        dt = T[i]-T[i-1]
        Theta.append(Theta[i-1] + dt*EQDF(Theta[i-1], eqdf, g, l))
    return np.array(Theta)

Theta0 = np.array([-pi/4, 0])
T_terre = create_time(10)

Theta = Euler_vect(Theta0, eqdf, T_terre)
print(Theta)
plt.plot(T_terre, Theta[:,0])
plt.show()

plt.plot(Theta[:,0], Theta[:,1], color="red")
plt.title("portrait de phase")
plt.grid()
plt.show()
