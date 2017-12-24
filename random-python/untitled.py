import numpy as np
import matplotlib.pyplot as plt

#data generation
x = np.arange(-10,20,0.2)
y = 1.0/(1.0+np.exp(-x)) # nunpy does the calculation elementwise for you
x=[4,-1]
y=[-3,2]

fig, ax1 = plt.subplots(ncols=1, figsize=(15,10))


# Eliminate upper and right axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# Show ticks on the left and lower axes only (and let them protrude in both directions)
ax1.xaxis.set_tick_params(bottom='on', top='off', direction='inout')
ax1.yaxis.set_tick_params(left='on', right='off', direction='inout')

# Make spines pass through zero of the other axis
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

ax1.set_ylim(-3.5,2.5)
ax1.set_xlim(-4.5,4.5)

# No ticklabels at zero
#ax1.set_xticks([-10,-5,5,10,15,20])
#ax1.set_yticks([-0.4,-0.2,0.2,0.4,0.6,0.8,1.0])

ax1.plot(x,y,'x',color='r', markersize=8)
plt.grid()
labels=['A','B']
for label, xpt,ypt in zip(labels,x,y):
    plt.text(xpt+0.1,ypt+0.1,label)
#fig.savefig('fig.png')
plt.show()
