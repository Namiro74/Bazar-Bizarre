import turtle
import DessinsElements
from random import *

def background(): #on appelle une fonction qui ne vas rien renvoyer elle va juste l'éxecuter
    turtle.setup(600,600,0,0) #dimension de la fenêtre turtle ouverte
    turtle.bgcolor("#FAF0E6") #couleur de fond bg=background # le # sert à dire que c'est de l'hexadécimal dont on touve les ref sur internet qui correspondent aux couleurs
    turtle.hideturtle() #on cache la flèche, ou tortue
    turtle.speed(0) #on augmente la vitesse pr que ce soit quasi instantanné
    turtle.up() #on lève le pinceau

    turtle.down()
    turtle.color(0,0.9,0)
    turtle.begin_fill()
    DessinsElements.rectangle(300,125,600,275)
    turtle.end_fill()
    for n in range(1,5):
        turtle.up()
        turtle.goto(randint(-295,295),randint(-150,110))
        turtle.down()
        turtle.color("white")
        turtle.begin_fill()
        for f in range(0,4):
            turtle.circle(5,360)
            turtle.rt(90)
        turtle.end_fill()
        turtle.rt(90)
        turtle.up()
        turtle.fd(5)
        turtle.left(90)
        turtle.down()
        turtle.color("yellow")
        turtle.begin_fill()
        turtle.circle(5,360)
        turtle.end_fill()
        #turtle.color("green")
        #turtle.seth(90)
        #turtle.fd(10)
    turtle.color(0,0.8,1)
    turtle.begin_fill()
    DessinsElements.rectangle(300,300,600,175)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-300,125)
    turtle.down()
    turtle.color(0.5,0.5,0.5)
    turtle.begin_fill()
    for m in range(0,5):
        turtle.goto(-300+m*120+60,275)
        turtle.goto(-300+(m+1)*120,125)
    turtle.goto(-300,125)
    turtle.end_fill()
    turtle.up()

    turtle.color("#FAF0E6")
    turtle.begin_fill()
    DessinsElements.rectangle(300,-150,600,150)
    turtle.end_fill()
    
    #pr dessiner le trait rouge 
    turtle.color("red") #on choisit la couleur rouge pour les traits suivant
    turtle.goto(-1000,-150) #on se déplace à l'extrémité
    turtle.down() #on pose le pinceau
    turtle.goto(1000,-150) #on fait le trait

    #DessinsElements.rectangle qui représente la carte choisit
    turtle.color("#FAF0E6") #on choisit la couleur du trait
    turtle.begin_fill()
    DessinsElements.rectangle(60, 90, 120, 200) #on dessine un DessinsElements.rectangle de...
    turtle.end_fill()
    turtle.color(0.3,0.3,0.3) #on choisit la couleur du trait
    turtle.pensize(2)
    DessinsElements.rectangle(60, 90, 120, 200) #on dessine un DessinsElements.rectangle de...
    turtle.pensize(1)

    turtle.color("red")
    turtle.begin_fill()
    DessinsElements.rectangle(100, -175, 200, 100)
    turtle.end_fill()
    turtle.pensize(4)
    turtle.color(0,0,0.4)
    DessinsElements.rectangle(100, -175, 200, 100)
    turtle.pensize(1)
    turtle.up()
    turtle.goto(0, -235)
    turtle.write("Commencer", False, "center", ("Uroob", 24, "bold"))
    
    #on dessine les trois cartes
    turtle.color("black")
    for x in range(-200, 360, 120): #on fait varier x de -160 à 340 avec un pas de 100
        DessinsElements.rectangle(x, 205, 80, 80) #on donne les mesures de chaque DessinsElements.rectangle qui prennent chacun une valeur x différente

def endScreen(score):
    turtle.begin_fill()
    turtle.color("#FAF0E6")
    DessinsElements.rectangle(300, 300, 600, 600)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0,20)
    turtle.color("black")
    turtle.write("Partie terminée !", False, "center", ("Arial", 20, "bold"))
    turtle.goto(0, -20)
    turtle.write("Score : " + str(score), False, "center", ("Arial", 20, "bold"))
    turtle.color("red")
    DessinsElements.rectangle(100, -40, 200, 50)
    turtle.up()
    turtle.goto(0, -75)
    turtle.write("Quitter", False, "center", ("Arial", 16, "bold"))
    partieTerminee = True

def dessinerCarte(carte):
    couleur1 = carte[0][1]
    if(carte[0][0] == "Vent"):
        DessinsElements.vent(0, 50, couleur1)
    if(carte[0][0] == "Feu"):
        DessinsElements.feu(0, 50, couleur1)
    if(carte[0][0] == "Eau"):
        DessinsElements.eau(0, 50, couleur1)
    if(carte[0][0] == "Eclair"):
        DessinsElements.eclair(0, 50, couleur1)
    if(carte[0][0] == "Terre"):
        DessinsElements.terre(0, 50, couleur1)

    couleur2 = carte[1][1]
    if(carte[1][0] == "Vent"):
        DessinsElements.vent(0, -50, couleur2)
    if(carte[1][0] == "Feu"):
        DessinsElements.feu(0, -50, couleur2)
    if(carte[1][0] == "Eau"):
        DessinsElements.eau(0, -50, couleur2)
    if(carte[1][0] == "Eclair"):
        DessinsElements.eclair(0, -50, couleur2)
    if(carte[1][0] == "Terre"):
        DessinsElements.terre(0, -50, couleur2)

def dessinerPions():
    turtle.color("black")
    DessinsElements.vent(-240, 165, "white")
    DessinsElements.feu(-120, 165, "red")
    DessinsElements.eau(0, 165, "blue")
    DessinsElements.eclair(120, 165, "yellow")
    DessinsElements.terre(240, 165, "green")
