from tkinter import *
import random

hcan = 600
wcan = 600
window = Tk()



couleur = "lightblue"

def change_couleur():
    global couleur
    couleur = input('Quelle couleur ? ')

def carre():

    cordx= random.randint(50,hcan-50)
    cordy = random.randint(50,wcan-50)
    canvas.create_rectangle(cordx-50, cordy-50, cordx+50,cordy + 50, fill=couleur)

def cercle():

    cordx= random.randint(50,hcan-50)
    cordy = random.randint(50,wcan-50)
    canvas.create_oval(cordx-50, cordy-50, cordx+50,cordy + 50, fill=couleur)

def ligne():
    cordx= random.randint(50,hcan-50)
    cordy = random.randint(50,wcan-50)
    canvas.create_line(cordx, cordy-50, cordx,cordy+50, fill=couleur)
    canvas.create_line(cordx+50, cordy, cordx-50,cordy, fill=couleur)

canvas = Canvas(window, width=wcan, height=hcan, highlightthickness=3,highlightbackground="lightgrey", bg="black")
canvas.grid(row=1,column=1,rowspan=3)

cross_Button = Button(text="Croix", command=ligne)
square_Button= Button(text="Carré", command=carre)
circle_Button = Button(text="Cercle",command=cercle)
color_Button = Button(text="Changer couleur", command=change_couleur)

cross_Button.grid(row=3,column=0)
square_Button.grid(row=2,column=0)
circle_Button.grid(row=1, column=0)
color_Button.grid(row=0, column=1)


mainloop()