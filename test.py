import numpy as np
from matplotlib import pyplot as plt

n=3
x = np.linspace(-n,n,10000)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#spine placement data centered
ax.spines['left'].set_position(('data', 0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.grid()
plt.plot(x,np.exp(x), color='blue')
fig.set_size_inches(20,15)
plt.savefig('fig.png')
plt.show()
