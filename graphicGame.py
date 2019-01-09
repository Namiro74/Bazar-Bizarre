import cardEditor #on importe le programme de création de cartes
import turtle #on importe le programme de dessin turtle
import time
import draw

objets = ["Vent", "Feu", "Eau", "Eclair", "Terre"]
couleurs = ["Blanc", "Rouge", "Bleu", "Jaune", "Vert"]
pions = []
carte = []
aCommence = False
temps1 = 0
temps2 = 0
score = 0
manche = 0
resultat = ""
partieTerminee = False

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

    #pr dessiner le trait rouge 
    turtle.color("red") #on choisit la couleur rouge pour les traits suivant
    turtle.goto(-1000,-150) #on se déplace à l'extrémité
    turtle.down() #on pose le pinceau
    turtle.goto(1000,-150) #on fait le trait

    #rectangle qui représente la carte choisit
    turtle.color("green") #on choisit la couleur du trait
    rectangle(60, 90, 120, 200) #on dessine un rectangle de...

    turtle.color("blue")
    rectangle(100, -175, 200, 100)
    turtle.up()
    turtle.goto(0, -235)
    turtle.write("Commencer", False, "center", ("Arial", 15, "bold"))

    #on dessine les trois cartes
    turtle.color("black")
    for x in range(-160, 340, 100): #on fait varier x de -160 à 340 avec un pas de 100
        rectangle(x, 250, 80, 80) #on donne les mesures de chaque rectangle qui prennent chacun une valeur x différente

def ecrireCarte(carte):
    turtle.color("green")
    turtle.up()
    turtle.goto(0, -10)
    turtle.write(carte[0][0]+" "+carte[0][1], False, "center", ("Arial", 12, "normal"))
    turtle.goto(0, -30)
    turtle.write(carte[1][0]+" "+carte[1][1], False, "center", ("Arial", 12, "normal"))

def afficherPionsTexte(pions):
    turtle.color("black")
    turtle.up()
    turtle.goto(-200,210)
    turtle.write(pions[0][0], False, "center", ("Arial", 12, "normal"))
    turtle.goto(-200,190)
    turtle.write(pions[0][1], False, "center", ("Arial", 12, "normal"))

    turtle.up()
    turtle.goto(-100,210)
    turtle.write(pions[1][0], False, "center", ("Arial", 12, "normal"))
    turtle.goto(-100,190)
    turtle.write(pions[1][1], False, "center", ("Arial", 12, "normal"))

    turtle.up()
    turtle.goto(0,210)
    turtle.write(pions[2][0], False, "center", ("Arial", 12, "normal"))
    turtle.goto(0,190)
    turtle.write(pions[2][1], False, "center", ("Arial", 12, "normal"))

    turtle.up()
    turtle.goto(100,210)
    turtle.write(pions[3][0], False, "center", ("Arial", 12, "normal"))
    turtle.goto(100,190)
    turtle.write(pions[3][1], False, "center", ("Arial", 12, "normal"))

    turtle.up()
    turtle.goto(200,210)
    turtle.write(pions[4][0], False, "center", ("Arial", 12, "normal"))
    turtle.goto(200,190)
    turtle.write(pions[4][1], False, "center", ("Arial", 12, "normal"))

def afficherPions():
    turtle.color("black")
    draw.vent(-200, 210, "white")
    draw.feu(-100, 210, "red")
    draw.eau(0, 210, "blue")
    draw.eclair(100, 210, "yellow")
    draw.terre(200, 210, "green")

def onClick(x,y):

    global pions
    global carte
    global aCommence
    global temps2
    global temps1
    global score
    global resultat
    global manche
    
    reponse = 0
    if(x < 100 and x > -100):
        if(y < -40 and y > -90):
            if(partieTerminee):
                turtle.bye()
            
    if(y < 250 and y > 170):
        if(x < -160 and x > -240):
            reponse = 1
        if(x < -60 and x > -140):
            reponse = 2
        if(x < 40 and x > -40):
            reponse = 3
        if(x < 140 and x > 60):
            reponse = 4
        if(x < 240 and x > 160):
            reponse = 5
        if(reponse <= 5 and reponse >= 1):
            manche += 1
            resultat = cardEditor.verification(carte, reponse, pions)
            temps2 = time.time()
            if(resultat == "Bonne réponse !"):
                score += 15 - (int(temps2) - int(temps1))
            else:
                score -= 15
            turtle.color("#FAF0E6")
            turtle.begin_fill()
            rectangle(300, -200, 220, 50)
            turtle.end_fill()
            turtle.color("black")
            turtle.up()
        if(manche < 5):
            nouvelleManche(pions)
        else:
            endScreen()

    if(y < -175 and y > -275 and x < 100 and x > -100):
        if(not aCommence):
            aCommence = True
            nouvelleManche(pions)

def endScreen():
    global score
    global partieTerminee
    
    turtle.begin_fill()
    turtle.color("#FAF0E6")
    rectangle(300, 300, 600, 600)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0,20)
    turtle.color("black")
    turtle.write("Partie terminée !", False, "center", ("Arial", 20, "bold"))
    turtle.goto(0, -20)
    turtle.write("Score : " + str(score), False, "center", ("Arial", 20, "bold"))
    turtle.color("red")
    rectangle(100, -40, 200, 50)
    turtle.up()
    turtle.goto(0, -75)
    turtle.write("Quitter", False, "center", ("Arial", 16, "bold"))
    partieTerminee = True

def nouvelleManche(pions):
    
    global carte
    global temps1
    global aCommence
    global score
    
    turtle.color("#FAF0E6")
    turtle.begin_fill()
    rectangle(300, -150, 600, 150)
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
    carte = cardEditor.creerCarte(pions)
    turtle.begin_fill()
    turtle.color("#FAF0E6")
    rectangle(60, 90, 120, 200)
    turtle.end_fill()
    turtle.color("green")
    rectangle(60, 90, 120, 200)
    ecrireCarte(carte)
    afficherPions()
    temps1 = time.time()

#construction de la liste de pions dynamiquement
for parcours in range(0, len(objets)):
    pions.append([objets[parcours], couleurs[parcours]])
setup()
turtle.getscreen().onclick(onClick)
