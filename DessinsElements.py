#GONZALES Garance, MOLLET-JULIEN Ethan, BAUDET Romain

from turtle import *
from random import *
from math import *

def eclair(x,y,couleur):
    seth(0)
    speed(0)
    hideturtle()
    up()
    goto(x,y)
    goto(x+(40/7),y+(40/7))
    down()
    color(couleur) #0.9,0.9,0
    begin_fill()
    fd(20*4/7)
    rt(180-degrees(atan(2)))
    fd(40*sqrt(5)*4/7)
    rt(180-degrees(atan(1/2)))
    fd(60*4/7)
    left(90)
    fd(20*4/7)
    rt(180-degrees(atan(2)))
    fd(40*sqrt(5)*4/7)
    rt(180-degrees(atan(1/2)))
    fd(60*4/7)
    end_fill()

def vent(x,y,couleur):
    seth(0)
    hideturtle()
    speed(0)
    up()
    goto(x,y-40)
    down()
    color(couleur)
    begin_fill()
    circle(40,360)
    end_fill()
    color("black")
    for n in range(0,3):
        up()
        goto(x-25,y+15-15*n)
        down()
        seth(300)
        circle(15,120)
        seth(60)
        circle(-15,120)

def feu(x,y,couleur):
    seth(0)
    speed(0)
    hideturtle()
    up()
    goto(x,y)
    goto(x-(40*8/11),y-(15*8/11))
    down()
    rt(90)
    color(couleur)
    begin_fill()
    circle(40*8/11,180)
    left(30)
    circle(-50*8/11,60)
    left(150)
    circle(40*8/11,50)
    seth(90)
    circle(60*8/11,50)
    seth(270)
    circle(-110*8/11,30)
    rt(120)
    circle(-50*8/11,50)
    left(154)
    circle(70*8/11,40)
    goto(x-(40*8/11),y-(15*8/11))
    end_fill()

def terre(x,y,couleur):
    seth(0)
    speed(0)
    hideturtle()
    up()
    goto(x,y)
    goto(x,y-40)
    left(90)
    down()
    color(couleur)
    fd(20)
    up()
    goto(x-20,y)
    down()
    rt(180)
    begin_fill()
    circle(20,180)
    goto(x,y+40)
    goto(x-20,y)
    end_fill()
    up()
    goto(x,y+40)
    down()
    pencolor("black")
    fd(-60)
    up()
    goto(x,y-5)
    for n in range(0,8) :
        seth(180)
        fd(16-2*n)
        down()
        fd(-(32-4*n))
        up()
        y=y+5
        goto(x,y-5)

def eau(x,y,couleur):
    seth(0)
    speed(0)
    hideturtle()
    up()
    goto(x,y)
    goto(x-25,y-15)
    rt(90)
    color(couleur)
    begin_fill()
    circle(25,180)
    goto(x,y+40)
    goto(x-25,y-15)
    end_fill()

def rectangle(x, y, largeur, hauteur): #x et y pts et largeur et hauteurs côtés
    up() #on lève le pinceau (on se déplace sans dessiner)
    goto(x, y) #on se place aux coordonnées x et y
    down() #on pose le pinceau
    setheading(0) #on choisit l'angle entre x et y pour commencer à dessiner
    for i in range(0, 4): #pr i allant de 0 à 4(4 angles)
        right(90) #la flèche s'oriente de 90° vers le bas
        if(i%2 == 0): #pr faire un rectangle si i est / par 2 alors il avance de sa hauteur 
            forward(hauteur)
        else:
            forward(largeur) #sinon il avance de sa largeur def par la fonct°
