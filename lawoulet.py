import pickle
import random
import os
nb_min=10
nb_max = 100
statut = True
Nombre_secret = 55
itilizate = {}
liste_user = []
fichier = "database.pkl"


def fichierpickle(fichier):
    try:
        with open(fichier, "rb") as file:
            liste_user = pickle.load(file)
    except FileNotFoundError:
        liste_user = []
    return liste_user


def save_user(fichier, liste_user):
    with open(fichier, "wb") as fichier_pickle:
        pickle.dump(liste_user, fichier_pickle)


def games_md():
    clear()
    print("                   Bienvenue au jeu de la roulette !")
    print(
        "2 :Dans ce jeu, un nombre aleatoire sera choisi  un nombre secret entre 1 et 100."
    )
    print(
        "3 :Votre tâche est de deviner ce nombre magique en utilisant le moins de tentatives possibles."
    )
    print("4 :Vous aurez au total 10 tentatives pour trouver le nombre secret")
    print(
        "5 :Après chaque tentative, l'ordinateur vous dira si votre nombre est plus grand ou plus petit que le nombre secret."
    )
    print(
        "6 :Vous pouvez continuer à deviner jusqu'à ce que vous trouviez le nombre secrer ou que vous epuisez vos tentatives."
    )
    print("7 :Amusez-vous et que la meilleure devinette gagne!")
    start_game = input("Etes-vous pret? (Y for yes or any key for exit):")
    if start_game.lower() != "y":
        exit()
    else:
        clear()

def search_user(username):
    username=username.lower()
    while " " in username:
        username = input("entrez un username valide : ")
    search=fichierpickle(fichier)
    for individu in search:
        if individu['username']==username:
            info_user=individu
            return info_user
    return None
        
    

def Login():
    global liste_user
    print("(Votre Username ne doit pas avoir d'espace)")
    individu_trouve = 0
    username = input("Entrez un username : ").lower()
    while " " in username:
        username = input("entrez un username : ")
    liste_user=fichierpickle(fichier)
    search=search_user(username)
    if search is None:
        info_user = {"username": username, "score": 0}
        liste_user.append(info_user)
        save_user(fichier, liste_user)
        clear()
        print(f"                   Bienvenue {info_user['username']}!          ")
        print(
                f"            Username : {info_user['username']}   Ancien score : {info_user['score']}"
            )
        return info_user
    clear()
    print(f"                   Bienvenue {search['username']}!          ")
    print(
        f"            Username : {search['username']}   Ancien score : {search['score']}"
        )
    return search


def test_int():
    while True:
        try:
            nbtest = int(
                input(f"choose your number ( between {nb_min} and {nb_max} ) :")
            )

            return nbtest
        except:
            print(f" is not a number, please retry")


def demande(nb_min, nb_max):
    nombre = test_int()
    while nombre <= nb_min or nombre > nb_max:
        nombre = test_int()
    return nombre

def update_score(itilizate,newscore):
    liste_user=fichierpickle(fichier)
    for liste in liste_user:
        if liste['username']==itilizate['username']:
            liste['score']+=newscore
            retr=liste['score']
            save_user(fichier,liste_user)
            return retr

    return None

def play_game():
    games_md()
    global itilizate
    itilizate = Login()
    ancien_score = itilizate["score"]
    newscore=0
    life = 10
    while life > 0:
        print(f"il vous reste {life} chance")
        inpt=demande(nb_min,nb_max)
        if inpt>nb_max:
            print("le nombre secret est plus petit")
        elif inpt<nb_min:
            print("le nombe secret est plus grand")    
        elif inpt==Nombre_secret:
            newscore=(life*30)
            update=update_score(itilizate,newscore)
            print('         BRAVO VOUS AVEZ GAGNE')
            print(f"            votre nouveau score est :{update}")
            break
        life-=1
    else:
        print(f"vous avez perdu et votre score reste {ancien_score}")
        print(f"le nombre secret etait : {Nombre_secret}")


def clear():os.system("cls")
