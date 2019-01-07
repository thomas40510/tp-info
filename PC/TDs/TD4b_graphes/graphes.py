import numpy as np
from numpy import inf


G_1 = [['A','B','C','D','E','F','G'], \
    np.array([[0,1,1,0,1,0,0],\
            [0,0,0,1,0,1,0],\
            [0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,0],\
            [0,0,0,0,0,1,0],\
            [0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0]])]
            
G_2 = [['A', 'B', 'C', 'D', 'E', 'F'], \
       np.array([[  0.,  inf,   3.,  inf,  inf,   1.],\
                 [ inf,   0.,   2.,   3.,   1.,  inf],\
                 [  3.,   2.,   0.,  inf,   3.,   1.],\
                 [ inf,   3.,  inf,   0.,   1.,  inf],\
                 [ inf,   1.,   3.,   1.,   0.,   5.],\
                 [  1.,  inf,   1.,  inf,   5.,   0.]])]
                 

G_3 = [['Routeur 1', 'Routeur 2', 'Routeur 3', 'Routeur 4', 'Routeur 5',\
        'Routeur 6'], \
       np.array([[  0.,   1.,  10.,  inf,  inf,  inf],\
                 [  1.,   0.,  inf,  22.,  inf,  inf],\
                 [ 10.,  inf,   0.,   3.,   1.,   3.],\
                 [ inf,  22.,   3.,   0.,   4.,  inf],\
                 [ inf,  inf,   1.,   4.,   0.,   1.],\
                 [ inf,  inf,   3.,  inf,   1.,   0.]])]
                 
G_4_distance = [['Parme', 'La Spezia', 'Bologne', 'Florence', 'Pérouse', \
                 'Rome'], \
                np.array([[   0.,  124.,  104.,   inf,   inf,   inf],\
                          [ 124.,    0.,   inf,  163.,   inf,   inf],\
                          [ 104.,   inf,    0.,  131.,  245.,   inf],\
                          [  inf,  163.,  131.,    0.,  150.,  283.],\
                          [  inf,   inf,  245.,  150.,    0.,  181.],\
                          [  inf,   inf,   inf,  283.,  181.,    0.]])]

G_4_duree = [['Parme', 'La Spezia', 'Bologne', 'Florence', 'Pérouse', \
                 'Rome'], \
             np.array([[   0.,  83.,  71.,   inf,   inf,   inf],\
                       [ 83.,    0.,   inf,  106.,   inf,   inf],\
                       [ 71.,   inf,    0.,  99.,  174.,   inf],\
                       [  inf,  106.,  99.,    0.,  103.,  168.],\
                       [  inf,   inf,  174.,  103.,    0.,  127.],\
                       [  inf,   inf,   inf,  168.,  127.,    0.]])]

G_4_cout = [['Parme', 'La Spezia', 'Bologne', 'Florence', 'Pérouse', \
                 'Rome'], \
            np.array([[   0.,  25.,  16.,   inf,   inf,   inf],\
                      [ 25.,    0.,   inf,  43.,   inf,   inf],\
                      [ 16.,   inf,    0.,  22.,  30.,   inf],\
                      [  inf,  43.,  22.,    0.,  20.,  42.],\
                      [  inf,   inf,  30.,  20.,    0.,  22.],\
                      [  inf,   inf,   inf,  42.,  22.,    0.]])]
                      
