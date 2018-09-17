###########################################################################################
#
#        Tracé "dynamique" d'une courbe avec modification d'une variable par curseur
#
###########################################################################################


# Import module Pylab
from math import *
from pylab import *

# Fonction mettant à jour les ordonnées en fonction de la valeur lue sur le curseur
def update(val=1):
   tau = tauSlider.val# Affectation de la valeur du curseur à la variable "frequence"
   k = kSlider.val
   s=k*(1-e**(-temps/tau))   # Calcul des ordonnées
   courbe.set_ydata(s)           # Affectation des nouvelles ordonnées à la courbe
   draw()                            # Tracé en temps réel (attention à bien utiliser draw et non pas show)

   
# Définition des absisces
temps=linspace(0,50,1000)

# Courbe initiale à tracer (toutes les ordonnées sont à zéro)
courbe, = plot(temps,[0]*len(temps), color='blue')

# Bornes du graphique en ordonnée
ylim(-1.5,3.0)

# Habillage du graphique
xlabel("temps (s)")
xticks(arange(0,50.1,5))
ylabel("s(t)")
yticks(arange(-1.5,3.1,0.5))
grid()

# Création de la zone du curseur et dessin
# Création d'un 2ème graphique sous le premier
subplots_adjust(bottom=0.2)
# Position et taille du curseur (position horizontale, position verticale, largeur, hauteur)
# Variable "sliderDessin" créée pour plus de lisibilité. Possibilité de mettre les paramètres
# directement dans la fonction Slider
sliderDessin=axes([0.2, 0.05, 0.5, 0.02])
sliderDessinAlt=axes([0.2,0.1,0.5,0.02])
# Création du curseur avec légende, valeurs limites, valeur initiale. L'instruction "valfmt"
# permet de formater l'écriture de la valeur à coté du curseur (nombre de décimal)
tauSlider = Slider(sliderDessin, 'tau', 1, 10, 1 ,valfmt='%1.1f')
kSlider = Slider(sliderDessinAlt, 'gain', 1,10,1,valfmt='%1.1f')


# Appel de la fonction "Update" avec la nouvelle valeur lors d'un changement du curseur
tauSlider.on_changed(update)
kSlider.on_changed(update)

# Tracé
show()
