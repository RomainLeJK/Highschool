import random

def choix_mot():
    compteur = 0
    ind_mot = random.randint(0,835)
    file = open("dico.txt", "r")
    for mots in file:
        if compteur != ind_mot :
            compteur += 1
        else :
            mot = mots.replace('\n', '')
            break
    
    return mot

def dessin_pendu(nb):
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |      _O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |      _O_
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |      _O_
       |       |
       |      /
       |
    ==============
    """,
    """
       +-------+
       |       |
       |      _O_
       |       |
       |      / \
       |
    ==============
    """
    ]
    return tab[nb]

def affichage(mot_en_cours, nb_tentative, mauvaises_lettres):
    for i in lettre_utilisées:
        if i==lettre_choisie:
            return(f"Vous avez déja choisi la lettre {lettre_choisie}")
    if mot_en_cours==mot_a_trouver:
        return(f"\nVous avez gagné avec {nb_tentative} tentatives restantes.\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==6:
        print(dessin_pendu(0))
        return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==5:
        print(dessin_pendu(1))
        return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==4:
        print(dessin_pendu(2))
        return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==3:
            print(dessin_pendu(3))
            return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==2:
        print(dessin_pendu(4))
        return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==1:
        print(dessin_pendu(5))
        return(f"Mot en cours : {mot_en_cours}\nIl vous reste {nb_tentative} tentatives\nMauvaises lettres : {mauvaises_lettres}")
    elif nb_tentative==0:
        print(dessin_pendu(6))
        return(f"Mot en cours : {mot_en_cours}\nIl ne vous reste plus de tentative, vous avez perdu.\nMauvaises lettres : {mauvaises_lettres}")



def proposition_lettre():
    lettre=input("Choisissez une lettre ").upper()
    return(lettre)

def actualiser_echecs(nb_tentative, mot_a_trouver, lettre_choisie):
    for i in mot_a_trouver:
        if i==lettre_choisie:
            return(nb_tentative)
    for i in lettre_utilisées:
        if i==lettre_choisie:
            return(nb_tentative)
    nb_tentative-=1
    mauvaises_lettres.append(lettre_choisie)
    return(nb_tentative)
        
        

    
def actualiser_mot(mot_en_cours, mot_a_trouver, lettre_choisie):
    liste_mot_en_cours=[]
    for i in mot_en_cours:
        liste_mot_en_cours.append(i)
    for i in range (len(mot_a_trouver)):
        if mot_a_trouver[i]==lettre_choisie:
            liste_mot_en_cours[i]=lettre_choisie
    mot_en_cours=liste_mot_en_cours[0]
    for i in range (1,len(mot_a_trouver)):
        mot_en_cours+=liste_mot_en_cours[i]
    return(mot_en_cours)

def difficulté():
    while True:
        choix_difficulté=input("Choisissez la difficulté entre Facile//Moyen//Difficile ").lower()
        Mot=choix_mot()
        if choix_difficulté=="facile":
            while len(Mot)<8:
                Mot=choix_mot()
            break
        elif choix_difficulté=="moyen":
            while len(Mot)>8 or len(Mot)<4:
                Mot=choix_mot()
            break
        elif choix_difficulté=="difficile":
            while len(Mot)>4:
                Mot=choix_mot()
            break
        else:
            print("La difficulté que vous avez choisi n'existe pas.")
    return(Mot)
        
# Boucle de jeu principale
partie = True
mot_a_trouver = difficulté() # Appel de la fonction déterminant le mot à trouver
mot_en_cours = "_"*len(mot_a_trouver) # Dans l'état actuel, on donne le mot caché par des _
nb_tentative = 6
mauvaises_lettres = []
lettre_utilisées=[]
print(affichage(mot_en_cours, nb_tentative, mauvaises_lettres))

while partie:
    if nb_tentative!=0 and mot_en_cours!=mot_a_trouver:
        lettre_choisie=proposition_lettre()
        mot_en_cours=actualiser_mot(mot_en_cours, mot_a_trouver, lettre_choisie)
        nb_tentative=actualiser_echecs(nb_tentative, mot_a_trouver, lettre_choisie)
        print(affichage(mot_en_cours, nb_tentative, mauvaises_lettres))
        lettre_utilisées+=lettre_choisie
    else:
        partie=False
        print(f"Le mot était {mot_a_trouver}")