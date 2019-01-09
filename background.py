import turtle
from random import *

def rectangle(x, y, largeur, hauteur): #x et y pts et largeur et hauteurs côtés
    turtle.up() #on lève le pinceau (on se déplace sans dessiner)
    turtle.goto(x, y) #on se place aux coordonnées x et y
    turtle.down() #on pose le pinceau
    turtle.setheading(0) #on choisit l'angle entre x et y pour commencer à dessiner
    for i in range(0, 4): #pr i allant de 0 à 4(4 angles)
        turtle.right(90) #la flèche s'oriente de 90° vers le bas
        if(i%2 == 0): #pr faire un rectangle si i est / par 2 alors il avance de sa hauteur 
            turtle.forward(hauteur)
        else:
            turtle.forward(largeur) #sinon il avance de sa largeur def par la fonct°
            
def setup(): #on appelle une fonction qui ne vas rien renvoyer elle va juste l'éxecuter
    turtle.setup(600,600,0,0) #dimension de la fenêtre turtle ouverte
    turtle.bgcolor("#FAF0E6") #couleur de fond bg=background # le # sert à dire que c'est de l'hexadécimal dont on touve les ref sur internet qui correspondent aux couleurs
    turtle.hideturtle() #on cache la flèche, ou tortue
    turtle.speed(0) #on augmente la vitesse pr que ce soit quasi instantanné
    turtle.up() #on lève le pinceau

    turtle.down()
    turtle.color(0,0.9,0)
    turtle.begin_fill()
    rectangle(300,125,600,275)
    turtle.end_fill()
    for n in range(1,50):
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
    rectangle(300,300,600,175)
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
    rectangle(300,-150,600,150)
    turtle.end_fill()
    
    #pr dessiner le trait rouge 
    turtle.color("red") #on choisit la couleur rouge pour les traits suivant
    turtle.goto(-1000,-150) #on se déplace à l'extrémité
    turtle.down() #on pose le pinceau
    turtle.goto(1000,-150) #on fait le trait

    #rectangle qui représente la carte choisit
    turtle.color("#FAF0E6") #on choisit la couleur du trait
    turtle.begin_fill()
    rectangle(60, 90, 120, 200) #on dessine un rectangle de...
    turtle.end_fill()

    turtle.color("blue")
    rectangle(50, -175, 200, 100)
    turtle.up()
    turtle.goto(-50, -235)
    turtle.write("Commencer", False, "center", ("Uroob", 24, "bold"))
    
    #on dessine les trois cartes
    turtle.color("black")
    for x in range(-200, 360, 120): #on fait varier x de -160 à 340 avec un pas de 100
        rectangle(x, 205, 80, 80) #on donne les mesures de chaque rectangle qui prennent chacun une valeur x différente

setup()
