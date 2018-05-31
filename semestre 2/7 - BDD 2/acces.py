import sqlite3

#~On ouvre le fichier contenant la base de données:
mabase = sqlite3.connect('world.db')

#~On crée un objet curseur permettant d'accéder à la base:
cur = mabase.cursor()

#~La commande "execute" prend en entrée une requête SQL,
#~sous forme de chaîne de caractères:
cur.execute('SELECT Code, Name FROM country WHERE Population > 1e9;')

#~Dans le cas d'un \verb+SELECT+, le résultat est stocké dans le curseur,
#~on utilise \verb+fetchall()+ ou \verb+fetchone()+ pour le récupérer.

#~Méthode 1:
#~\verb+fetchall()+ renvoie directement une liste de tuple:

res = cur.fetchall()
Code = []
Name = []
for entree in res:
    Code.append(entree[0])
    Name.append(entree[1])

#~Méthode 2:
#~\verb+fetchone()+ renvoie un tuple correspondant
#~à une entrée à chaque appel (à la manière de \verb+readline+):

cur.execute('SELECT Code, Name FROM country WHERE Population > 1e9;')
Code = []
Name = []
entree = cur.fetchone()
while entree != None :
    Code.append(entree[0])
    Name.append(entree[1])
    entree = cur.fetchone()

#~Si on a modifié la BDD, il faut valider
#~la transaction en cours pour qu'elle prenne effet:
mabase.commit()

#~Pour finir, on ferme la base de données:
mabase.close()

