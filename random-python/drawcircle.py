import numpy as np
import matplotlib.pyplot as plt

r = 5  # rayon

X = []
Y = []

for x in np.linspace(-r, r, 1000):
    y = r
    while x ** 2 + y ** 2 - r ** 2 > .005:
        y -= .002
    X.append(x)
    X.append(x)
    Y.append(y)
    Y.append(-y)
npX = np.array(X)
npY = np.array(Y)
print('final: ', npX, npY)

plt.scatter(npX, npY, )
plt.show()
