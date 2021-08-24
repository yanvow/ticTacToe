from turtle import *
from math import *
from tictactoe import *


def init():
    global couleur
    couleur = str(input("Indicate the COLOR of your game : "))
    
def titre():
    title("Tic Tac Toc")
    up()
    goto(-150,180)
    down()
    write("player1 = O ")
    up()
    goto(-150,150)
    down()
    write("Player2 = X ")
    up()
    goto(0,0)
    down()

def grille():
    global taille
    taille=size()
    color(couleur)
    forward(100*taille)
    up()
    right(90)
    forward(33*taille)
    right(90)
    down()
    forward(100*taille)
    up()
    left(90)
    forward(33*taille)
    left(90)
    forward(33*taille)
    left(90)
    down()
    forward(100*taille)
    up()
    right(90)
    forward(33*taille)
    right(90)
    down()
    forward(100*taille)
    up()
    goto(0,0)



        
    
