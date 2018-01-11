import pendu_fonctions as hm
import drawhm as dHM

    
def init():
    global mot
    mot = hm.choisir_mot("mots_francais.txt")
    score = 6
    letters=[""]
    play(score,letters)

def play(score,letters):
    c = hm.entrer_lettre()
    letters.append(c)
    if (hm.mot_trouve(mot, letters)):
        hm.gameEnd(c,True,mot,score)
        if (hm.askNG()):
            init()
    elif ((c not in mot)):
        score = score-1
        dHM.drawhm(6-score)
        if (score==0):
            hm.gameEnd(c,False,mot,score)
            if (hm.askNG()):
                init()
    print(hm.mot_etoiles(mot, letters))
    play(score,letters)


if(input("Bienvenue dans le pendu. Une petie partie ? (Y/N) ")=="Y"):
    init()
else :
    exit()
