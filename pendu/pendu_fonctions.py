from random import choice

def choisir_mot(nom_fichier):
    mFile = open(nom_fichier, "r")
    allWords = mFile.readlines()
    word = choice(allWords)

    return word.strip("\n")

def mot_etoiles(mot, letters):
    sWord = ""
    for c in mot:
        if c in letters:
            sWord+=(c)
        else :
            sWord+=("*")
    return sWord

def entrer_lettre():
    c=""
    while (len(c)!=1 and c!="quitter"):
        c= input("entrer une lettre : ")

    if (c=="quitter"):
        exit()
    else :
        return c
    
def mot_trouve(mot, letters):
    if ("*" in mot_etoiles(mot,letters)):
        return False
    else :
        return True

def gameEnd(lettre, gagne, mot, score):
    if (lettre=="quitter"):
        state="interrompue par l'utilisateur"
    elif (gagne):
        state="gagnée"
        extraMsg = "Il vous restait ",score," essais."
    else :
        state="perdue"
        extraMsg = "Le mot était "+"\'"+mot+"\'."
        
    print("La partie est ",state)
    print(extraMsg)

def askNG():
    return(input("Voulez-vous rejouer ? Y/N ")==("Y"))
        
