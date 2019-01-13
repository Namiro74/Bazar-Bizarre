#GONZALES Garance, MOLLET-JULIEN Ethan, BAUDET Romain

#Projet Programmation Impérative
#Module contenant les méthodes

#Pour la bonne compréhension du programme, veuillez lire le programme principal
#consoleGame.py et vous reporter à ce programme chaque fois que le principal appelle une
#méthode de cardEditor

#importation du module d'aléatoire
import random

#Cette fonction renvoie une carte choisie aléatoirement
#Une carte est en fait une liste, composée de deux sous-listes représentant les dessins de
#la carte
#Une carte est de la forme : [[O,C],[O,C]], avec O un objet et C une couleur (2 différents)
def creerCarte(pions):

    #initialisation de la variable carte
    carte = []

    #a et b sont des variables aléatoires qui vont décider de l'objet et de la couleur du
    #1er élément de la carte
    a = random.randint(0, 4)
    b = random.randint(0, 4)

    #on initialise 2 autres variables aléatoires pour le 2e élément, mais on les tirera au
    #sort après
    c = a
    d = b

    #on ajoute à carte une liste représentant le 1er élément
    carte.append([pions[a][0], pions[b][1]])

    #c et d NE DOIVENT PAS valoir ni a, ni b : dans le cas contraire, on se retrouverait
    #ds une contradiction: on aura une carte avec le même 2ème objet ou la même 2ème couleur. 
    while (c == a or c == b):
        c = random.randint(0, 4)
    while (d == b or d == a):
        d = random.randint(0, 4)

    #on ajoute à carte une liste représentant le 2e élément
    carte.append([pions[c][0], pions[d][1]])

    #renvoie une liste contenant 2 sous-listes avec les objets et les couleurs
    return carte

#méthode de vérification de la réponse de l'utilisateur
#cette méthode peut sembler compliquée, mais elle ne l'est pas : elle fait seulement une
#disjonction de cas et vérifie simplement si la réponse de l'utilisateur est correcte
#les conditions des if sont longues car il y a plusieurs cas à traiter, il ne faut pas s'y
#attarder, mais seulement retenir que la fonction vérifie la réponse.
def verification(carte, reponse, pions):

    #1er cas : le 1er élément de la carte est un pion des objets du jeu
    if ([carte[0][0], carte[0][1]] in pions):

        #si l'objet et la couleur de la réponse de l'utilisateur sont les mêmes que
        #l'élément de la carte qui est un pion, alors bonne réponse
        if (pions[reponse - 1][0] == carte[0][0] and pions[reponse - 1][1] == carte[0][1]):
            return "Bonne réponse !"

        #sinon, mauvaise réponse
        else:
            return "Mauvaise réponse !"

    #2e cas : le 2e élément de la carte est un pion des objets du jeu
    elif ([carte[1][0], carte[1][1]] in pions):

        #si l'objet et la couleur de la réponse de l'utilisateur sont les mêmes que l'élément de
        #la carte qui est un pion, alors bonne réponse
        if (pions[reponse - 1][0] == carte[1][0] and pions[reponse - 1][1] == carte[1][1]):
            return "Bonne réponse !"
        
        #sinon, mauvaise réponse
        else:
            return "Mauvaise réponse !"

    #3e cas : aucun des éléments de la carte n'est un pion des objets du jeu.
    #on met un else car c'est le dernier cas, et le seul qui reste
    else:

        #il faut que la réponse de l'utilisateur soit l'"intruse"
        #si ce n'est pas le cas, mauvaise réponse
        if (pions[reponse - 1][0] == carte[0][0]
            or pions[reponse - 1][1] == carte[0][1]
            or pions[reponse - 1][0] == carte[1][0]
            or pions[reponse - 1][1] == carte[1][1]):
            return "Mauvaise réponse !"

        #sinon, bonne réponse
        else:
            return "Bonne réponse !"

#une dernière fonction pour la route (la plus simple): elle affiche seulement la description d'une
#carte de manière structurée, car si on fait print(carte), on aura quelque chose d'affiché
# de la forme [[Objet,Couleur],[Objet,Couleur]] et on ne vuet pas ça du tout
def afficherCarte(carte):
    print("La carte est : ", carte[0][0], carte[0][1], " et ", carte[1][0], carte[1][1])
