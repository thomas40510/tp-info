import numpy as np
import matplotlib.pyplot as plt


class Pile :
    '''implémentation de la classe 'pile', ie un LIFO '''
    def __init__(self, L = []):
        self.val = L

    def creer(self):
        return ([])


    def empile(self, el):
        if type(el) == list:
            for i in el:
                self.val.append(i)
        else:
            self.val.append(el)
        return self.val


    def depile(self):
        x = self.val[-1]
        self.val = [self.val[i] for i in range(len((self.val))-1)]
        return x


    def lire_sommet(self):
        return self.val[-1]


    def affiche(self):
        print(self.val)


    def inverse(self):
        v = [self.val[i] for i in range(len(self.val)-1,-1,-1)]
        self.val = v


p = Pile()
ls = [i for i in range(10)]
p.empile(ls)
p.depile()
p.affiche()
p.inverse()
p.affiche()
