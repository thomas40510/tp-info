import numpy as np
from matplotlib import pyplot as plt

n=0.1
x = np.linspace(-n,n,10000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#spine placement data centered

ax.spines['left'].set_position(('zero'))
ax.spines['bottom'].set_position(('zero'))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.grid()
#plt.plot(x,np.exp(x), color='blue')
plt.plot(x,np.sin(1/x))
#fig.set_size_inches(20,15)
#plt.savefig('figure.png')
plt.show()
