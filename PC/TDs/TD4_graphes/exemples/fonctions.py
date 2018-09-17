import numpy as np
from numpy import inf

def voisins(Graphe, Sommet): #où on peut aller en partant de Sommet 
    indice=0
    while indice <= len(Graphe[0])-1 and Graphe[0][indice] != Sommet:
        indice = indice +1
    
    Liste_voisins = []
    for j in range (len(Graphe[1])) :
        if Graphe[1][indice][j] !=0 and Graphe[1][indice][j] != inf:
            Liste_voisins.append(Graphe[0][j])
    return(Liste_voisins)
    
    
def adjacents(Graphe, Sommet): #d'où on peut partir pour aller à Sommet 
    indice=0
    while indice <= len(Graphe[0])-1 and Graphe[0][indice] != Sommet:
        indice = indice +1
    
    Liste_adjacents = []
    for j in range (len(Graphe[1])) :
        if Graphe[1][j][indice] !=0 and Graphe[1][j][indice] != inf:
            Liste_adjacents.append(Graphe[0][j])
    return(Liste_adjacents)
    
def degre_sortant(Graphe, Sommet):
    return(len(voisins(Graphe, Sommet)))
    
def degre_entrant(Graphe, Sommet):
    return(len(adjacents(Graphe, Sommet)))
    
def parc_prof(Graphe, Depart):
    memoire=voisins(Graphe, Depart)
    parcours=[Depart]
    while memoire != [] :
        suivant=memoire.pop()
        memoire=memoire + voisins(Graphe, suivant)
        if suivant not in parcours :
            parcours.append(suivant)
    return(parcours)

def parc_larg(Graphe, Depart):
    memoire=voisins(Graphe, Depart)
    parcours=[Depart]
    while memoire != [] :
        suivant = memoire[0]
        memoire= memoire[1:] + voisins(Graphe, suivant)
        if suivant not in parcours :
            parcours.append(suivant)
    return(parcours)
    
def Dijkstra(Graphe, Depart, Arrivee=Graphe[0]):
    distances_min=[]
    parcours=[]
    
    
    
G_1 = [['A', 'B', 'C', 'D', 'E', 'F', 'G'], \
       np.array([[0, 1, 1, 0, 1, 0, 0],\
                 [0, 0, 0, 1, 0, 1, 0],\
                 [0, 0, 0, 0, 0, 0, 1],\
                 [0, 0, 0, 0, 0, 0, 0],\
                 [0, 0, 0, 0, 0, 1, 0],\
                 [0, 0, 0, 0, 0, 0, 0],\
                 [0, 0, 0, 0, 0, 0, 0]])]
                 
G_2 = [['A', 'B', 'C', 'D', 'E', 'F'], \
       np.array([[  0.,  inf,   3.,  inf,  inf,   1.],\
                 [ inf,   0.,   2.,   3.,   1.,  inf],\
                 [  3.,   2.,   0.,  inf,   3.,   1.],\
                 [ inf,   3.,  inf,   0.,   1.,  inf],\
                 [ inf,   1.,   3.,   1.,   0.,   5.],\
                 [  1.,  inf,   1.,  inf,   5.,   0.]])]
                 
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