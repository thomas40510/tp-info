def nrm(x):
    n=pow(sum(pow(i,2)for i in x),0.5)
    return n

def unitaire(d):
    return [i/nrm(d) for i in d]

# d=[4,-5,2]
# print(unitaire(d))


class Point:
    '''Définition d'un point en coordonnées cartésiennes 3D'''
    def __init__(self, px=0, py=0, pz=0):
        self.abscisse = px
        self.ordonnee = py
        self.cote = pz
    def affichage(self):
        print('(',str(self.abscisse), ',', str(self.ordonnee), ',', str(self.cote),')')
    def format_tuple(self):
        return (self.abscisse, self.ordonnee, self.cote)
    def format_liste(self):
        return ([self.abscisse, self.ordonnee, self.cote])
    def bipoint(self, p):
        return Vecteur(p.abscisse-self.abscisse, p.ordonnee-self.ordonnee, p.cote-self.cote)

class Vecteur:
    '''Définition d'un vecteur en coordonnées cartésiennes 3D'''
    def __init__(self, ux=0, uy=0, uz=0):
        self.vx=ux
        self.vy=uy
        self.vz=uz
    def affichage(self):
        print('(',str(self.vx), ',', str(self.vy), ',', str(self.vz),')')
    def format_tuple(self):
        return (self.vx, self.vy, self.vz)
    def format_liste(self):
        l = [self.vx, self.vy, self.vz]
        return [int(i) for i in l]
    def __add__(self, other):
        return Vecteur(self.vx + other.vx, self.vy + other.vy, self.vz+other.vz)
    def __mul__(self, k):
        return Vecteur(k*self.vx, k*self.vy, k*self.vz)
    def norme(self):
        return pow(sum(pow(i,2) for i in self.format_liste()), 0.5)
    def unit(self):
        l=[i/self.norme() for i in self.format_liste()]
        return Vecteur(l[0], l[1], l[2])

def scal(x,y):
    xl=x.format_liste()
    yl=y.format_liste()
    l = [xl[i]*yl[i] for i in range(len(xl))]
    return (sum(k for k in l))

x=Vecteur(1,2,3)
y=Vecteur(2,3,2)

