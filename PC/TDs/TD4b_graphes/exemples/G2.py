import numpy as np
from numpy import inf

G_2 = [['A', 'B', 'C', 'D', 'E', 'F'], \
       np.array([[  0.,  inf,   3.,  inf,  inf,   1.],\
                 [ inf,   0.,   2.,   3.,   1.,  inf],\
                 [  3.,   2.,   0.,  inf,   3.,   1.],\
                 [ inf,   3.,  inf,   0.,   1.,  inf],\
                 [ inf,   1.,   3.,   1.,   0.,   5.],\
                 [  1.,  inf,   1.,  inf,   5.,   0.]])]