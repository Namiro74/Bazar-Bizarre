import EditeurDeCarte #on importe le programme de création de cartes
import turtle #on importe le programme de dessin turtle
import time
import DessinsElements
import DessinsFenetre
from random import *

objets = ["Vent", "Feu", "Eau", "Eclair", "Terre"]
couleurs = ["white", "red", "blue", "yellow", "green"]
pions = []
carte = []
aCommence = False
temps1 = 0
temps2 = 0
score = 0
manche = 0
resultat = ""

partieTerminee = False

def onClick(x,y):

    global pions
    global carte
    global aCommence
    global temps2
    global temps1
    global score
    global resultat
    global manche
    global partieTerminee
    
    reponse = 0
    if(x < 100 and x > -100):
        if(y < -40 and y > -90):
            if(partieTerminee):
                turtle.bye()
            
    if(y > 125 and y < 205):
        if(x < -200 and x > -280):
            reponse = 1
        if(x < -80 and x > -160):
            reponse = 2
        if(x < 40 and x > -40):
            reponse = 3
        if(x < 160 and x > 80):
            reponse = 4
        if(x < 280 and x > 200):
            reponse = 5
        if(reponse <= 5 and reponse >= 1):
            manche += 1
            resultat = EditeurDeCarte.verification(carte, reponse, pions)
            temps2 = time.time()
            if(resultat == "Bonne réponse !"):
                score += 15 - (int(temps2) - int(temps1))
            else:
                score -= 15
            turtle.color("#FAF0E6")
            turtle.begin_fill()
            DessinsElements.rectangle(300, -200, 220, 50)
            turtle.end_fill()
            turtle.color("black")
            turtle.up()
            if(manche < 5):
                nouvelleManche(pions)
            else:
                partieTerminee = True
                DessinsFenetre.endScreen(score)

    if(y < -175 and y > -275 and x < 100 and x > -100):
        if(not aCommence):
            aCommence = True
            nouvelleManche(pions)
            DessinsFenetre.dessinerPions()

def nouvelleManche(pions):
    
    global carte
    global temps1
    global aCommence
    global score
    
    turtle.color("#FAF0E6")
    turtle.begin_fill()
    DessinsElements.rectangle(300, -150, 600, 150)
    turtle.end_fill()
    turtle.color("red") #on choisit la couleur rouge pour les traits suivant
    turtle.goto(-1000,-150) #on se déplace à l'extrémité
    turtle.down() #on pose le pinceau
    turtle.goto(1000,-150) #on fait le trait
    turtle.up()
    turtle.goto(-200, -235)
    turtle.color("black")
    turtle.write("score : " + str(score), False, "center", ("Arial", 15, "bold"))
    turtle.goto(0, -235)
    turtle.write(resultat, False, "center", ("Arial", 15, "bold"))
    carte = EditeurDeCarte.creerCarte(pions)
    turtle.begin_fill()
    turtle.color("#FAF0E6")
    DessinsElements.rectangle(60, 90, 120, 200)
    turtle.end_fill()
    turtle.color("green")
    DessinsElements.rectangle(60, 90, 120, 200)
    DessinsFenetre.dessinerCarte(carte)
    temps1 = time.time()

#construction de la liste de pions dynamiquement
for parcours in range(0, len(objets)):
    pions.append([objets[parcours], couleurs[parcours]])
DessinsFenetre.background()
turtle.getscreen().onclick(onClick)
