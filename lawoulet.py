import pickle
import random
import os

nb_min = 50
nb_max = 200
statut = True
Nombre_secret = 55
score = 0
liste_user = []
itilizate={}

def fichierpickle():
    try:
        with open('fichier_user.pkl', "rb") as fichier_pickle:
            liste_user = pickle.load(fichier_pickle)
            fichier_pickle.close
    except FileNotFoundError:
        liste_user=[]
        with open('fichier_user.pkl','wb') as fichier_pickle:
            pickle.dump(liste_user,fichier_pickle)
            fichier_pickle.close
    return liste_user

# print('hello , Bienvenue dans le jeu de la roullette /n pressez "Q" pour commencer ')


def Login():
    print("le pseudo doit etre en minuscule et ne doit pas avoir d'espace")
    pseudo = input("entrez un pseudo : ")
    while not pseudo.islower() or " " in pseudo:
        pseudo = input("entrez un pseudo : ")
    liste_user=fichierpickle()

    for individu in liste_user:
        if individu['username']==pseudo:
            info_user=individu
            print(f"username:{info_user['username']}\n score: {info_user['score']}")

            return info_user
    info_user={'username':pseudo,'score':0}
    liste_user.append(info_user)
    with open('fichier_user.pkl','wb') as fichier_pickle:
        pickle.dump(liste_user,fichier_pickle)
        # fichier_pickle.close
    print(f"username:{info_user['username']}\n score: {info_user['score']}")
    return info_user




def afficher():
    utilisateur = {}
    try:
        with open("fichier_user.pkl", "rb") as fichier_pickle:
            utilisateur = pickle.load(fichier_pickle)
            fichier_pickle.close
    except FileNotFoundError:
        utilisateur = {}
    for pseudo, var in utilisateur.items():
        print(f"pseudo : {pseudo} \n score :{score}\n")


def test_int():
    while True:
        try:
            nbtest = int(
                input(
                    f"veuillez entrer un nombre compris entre {nb_min} et {nb_max} : "
                )
            )
            return nbtest
        except:
            print("ce nest pas un nombre")


def demande(nb_min, nb_max):
    nombre = test_int()
    while nombre < nb_min or nombre > nb_max:
        nombre = test_int()
    return nombre


def play_game():
    
    global itilizate
    itilizate=Login()
    chance = 2
    chans2=0
    chans3=3
    result = demande(nb_min, nb_max)
    while chance!=chans2:
        if result == Nombre_secret:
            ancien_score=itilizate['score']
            nouvo_score=ancien_score +(chans3*30)
            
            itilizate['score']=nouvo_score
            # sko= chans3 * 30
            # newscore=itilizate['score']+sko
            # liste_user.append(itilizate)
            print(f"bravo votre score est {nouvo_score}")
            liste_user.append(itilizate)
            with open('fichier_user.pkl','wb') as fichier_pickle:
                pickle.dump(liste_user,fichier_pickle)
                fichier_pickle.close
            print('score change')

            
            break
        else:
            chans2+=1
            chans3=chans3-1
            print(f"il vous reste {chans3} vies")

            if result < Nombre_secret:
                print("le nombre cache est plus grand")
                result = demande(nb_min, nb_max)

            else:
                print("le nombre secret est plus petit")
                result = demande(nb_min, nb_max)

    if chance == chans2:
        print("vous avez perdu la partie")
        print(f"le nombre cache etait{Nombre_secret}")
    # if itilizate['username'] in liste_user:
    
    

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


