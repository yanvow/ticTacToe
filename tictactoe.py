from turtle import *
from definition import *

taille=0


def size():
    global taille
    taille = int(input("Indicate the SIZE of your game : "))
    return taille

def victoirePlayer1():
    goto(10,-260)
    write(" PLAYER 1 WIN ", font=("Arial", 30, "normal"))
    print(" CLIQUEZ POUR QUITTEZ ")
    exitonclick()
            
def victoirePlayer2():
    goto(10,-260)
    write(" PLAYER 2 WIN ", font=("Arial", 30, "normal"))
    print(" CLIQUEZ POUR QUITTEZ ")
    exitonclick()
    
global cases
cases=[1,2,3,4,5,6,7,8,9]

global H1
H1=[]

global H2
H2=[]
    
def play(player, H):
    cases.remove(player)
    H.append(player)
    placerCurseur(player)
    print(cases,H)

def placerCurseur(pos):
    global taille
    if pos==1:
        goto((13/2)*taille , (33/2)*taille)
    elif pos==4:
        goto((13/2)*taille , -(33/2)*taille)
    elif pos==7:
        goto((13/2)*taille , -((33/2)+33)*taille)
    elif pos==2:
        goto(((13/2)+33)*taille , (33/2)*taille)
    elif pos==5:
        goto(((13/2)+33)*taille , -(33/2)*taille)
    elif pos==8:
        goto(((13/2)+33)*taille , -((33/2)+33)*taille)
    elif pos==3:
        goto(((13/2)+2*33)*taille , (33/2)*taille)
    elif pos==6:
        goto(((13/2)+2*33)*taille , -(33/2)*taille)
    elif pos==9:
        goto(((13/2)+2*33)*taille , -((33/2)+33)*taille)
    else:
        print("!! Cette valeur n'est pas dans la grille !!")

y=0


def valid_input(inp):
    try:
        ret=int(inp)
        if ret not in cases:
            print ("Invalid range!! Try Again")
            return None
        return ret
    except:
        print ("Invalid input!! Try Again")
        return None

     
def player1():
    global taille
    def cercle():
        down()
        circle(taille*10)
        up()
    
    while True:
        player1=valid_input(textinput("PLAYER 1 : ","What is your next move : "))
        if player1:break
    play(player1, H1)
    cercle()
    goto(0,0)


    if 1 in H1 and 2 in H1 and 3 in H1:
       victoirePlayer1()
    elif 4 in H1 and 5 in H1 and 6 in H1:
       victoirePlayer1()
    elif 7 in H1 and 8 in H1 and 9 in H1:
        victoirePlayer1()
    elif 1 in H1 and 4 in H1 and 7 in H1:
        victoirePlayer1()
    elif 2 in H1 and 5 in H1 and 8 in H1:
        victoirePlayer1()
    elif 3 in H1 and 6 in H1 and 9 in H1:
        victoirePlayer1()
    elif 1 in H1 and 5 in H1 and 9 in H1:
        victoirePlayer1()
    elif 3 in H1 and 5 in H1 and 7 in H1:
        victoirePlayer1()
    if not cases:
        goto(10,-260)
        write(" DRAW ", font=("Arial", 30, "normal"))
        end()
    global y
    y+=1

def player2():
    global taille
    def croix():
        right(180)
        forward(taille*10)
        down()
        right(180-45)
        forward(taille*28)
        up()
        right(180-45)
        forward(taille*20)
        right(180-45)
        down()
        forward(taille*28)
        right(45+90)
        up()
    
    while True:
        player2=valid_input(textinput("PLAYER 2 : ","What is your next move : "))
        if player2:break
    play(player2, H2)
    croix()
    goto(0,0)
        
    if 1 in H2 and 2 in H2 and 3 in H2:
        victoirePlayer2()
    elif 4 in H2 and 5 in H2 and 6 in H2:
        victoirePlayer2()
    elif 7 in H2 and 8 in H2 and 9 in H2:
        victoirePlayer2()
    elif 1 in H2 and 4 in H2 and 7 in H2:
        victoirePlayer2()
    elif 2 in H2 and 5 in H2 and 8 in H2:
        victoirePlayer2()
    elif 3 in H2 and 6 in H2 and 9 in H2:
        victoirePlayer2()
    elif 1 in H2 and 5 in H2 and 9 in H2:
        victoirePlayer2()
    elif 3 in H2 and 5 in H2 and 7 in H2:
        victoirePlayer2()
    global y       
    y+=1
