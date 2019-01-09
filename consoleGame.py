#Projet Programmation Impérative
#Programme principal

#Pour la bonne compréhension du programme, lire celui-ci et se reporter au fichier cardEditor.py
#à chaque fois que celui-ci est mentionné (c'est lui qui contient les méthodes)

#cette version est la première, il ne s'agit donc pas de faire une version sans aucune imperfection
#par exemple, les couleurs peuvent être mal accordées selon l'objet qui est tiré au sort (comme "canapé verte")
#veuillez ne pas y prêter attention.

#importation des méthodes de notre module
import cardEditor

# listes d'objets, de couleurs et de pions
objets = ["Vent", "Feu", "Eau", "Eclair", "Terre"]
couleurs = ["Blanc", "Rouge", "Bleu", "Jaune", "Vert"]

#on déclare la variable pions comme étant une liste. On la remplit juste après
#(automatiquement,pas manuellement)
pions = []

#On va construire la liste de pions à partir des listes d'objets et de couleurs
#La liste pions sera de la forme suivante :
#[[O,C],[O,C],[O,C],[O,C],[O,C]], avec O un objet et C une couleur (5 différents)
#On choisit un objet aléatoiremt ds parcours et une couleur aléatoire ds parcours pr former
#l'objet.
for parcours in range(0, len(objets)):
    pions.append([objets[parcours], couleurs[parcours]])

# variable pour continuer à jouer ou pas
continuer = "o"

#1 tour de cette boucle ==> 1 manche de jeu
#et on joue tant que l'utilisateur le souhaite
while (continuer == "o"):

    #affichage de tout les pions et leurs numéros associés
    for i in range(0, len(pions)):
        print("Pions n°", i + 1, " : ", pions[i][0], pions[i][1])

    #on créé une carte, on l'affiche et on la stocke en mémoire dans la variable carte
    #une carte n'est rien d'autre qu'une liste générée aléatoirement par la méthode
    #creerCarte
    #(se reporter au fichier cardEditor.py)
    carte = cardEditor.creerCarte(pions)

    #la méthode afficherCarte sert à afficher proprement une carte
    #de la forme : "La carte est :  Canapé Rouge  et  Bouteille Verte"
    cardEditor.afficherCarte(carte)

    # on attend une réponse, puis on la vérifie
    reponse = int(input("Réponse ? \n"))
    print(cardEditor.verification(carte, reponse, pions))
    #la méthode verification ne fait que renvoyer du texte indiquand la réussite/l'échec
    #se reporter à cardEditor.py

    #l'utilisateur veut-il continuer ?
    continuer = ""
    #o et n sont les deux seules réponses possibles
    while (continuer != "o" and continuer != "n"):
        continuer = input("Continuer ? \n")
