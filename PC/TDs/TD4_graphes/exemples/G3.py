import numpy as np
from numpy import inf

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