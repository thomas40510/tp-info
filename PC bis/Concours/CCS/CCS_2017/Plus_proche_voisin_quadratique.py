def plus_proche_voisin(d):
    '''d matrice des distances de l'ensemble des points d'intérêt auquel est
    adjoint la position du robot, entre eux.'''
    n = len(d) - 1
    res_chemin = [n]    # le chemin démarre de la position du robot
    point_visite = [False for _ in range(n)] # aucun point d'intérêt visité
    
    # Parcourt de tous les points d'intérêt
    for p in range(n):
        point_actuel = res_chemin[-1] # dernier point du chemin en cours
        dMin = float('inf') # initialisation de dMin au majorant des flottants
        
        # Parcourt des points d'intérêt non encore visités
        for i in [k for k in range(n) if not point_visite[k]]:
            dist = d[point_actuel, i]
            if dist < dMin:
                dMin = dist
                iMin = i
                
        res_chemin.append(iMin)
        point_visite[iMin] = True
        
    return res_chemin[1:] # pour ne pas renvoyer l'indice n 