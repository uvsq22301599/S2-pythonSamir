from tkinter import *
from random import randint

window = Tk()

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j,width=0,fill=color)

def aleatoire():
    for i in range (256):
        for j in range(256):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            draw_pixel(i,j,get_color(r,g,b))

def degrade_gris():
    for i in range (256):
        for j in range (256):
            draw_pixel(i,j,get_color(i,i,i))


def degrade_2d():
    for i in range (256):
        for j in range(256):
            draw_pixel(i,j,get_color(i,0,j))



canvas = Canvas(window,height=256,width=256,highlightbackground="cornsilk4",highlightthickness=3,background='black')
canvas.grid(row=0,column=1,rowspan=3)

Bouton_aleatoire = Button(window, text="Aléatoire", command=aleatoire)
Bouton_aleatoire.grid(row=0,column=0)

Bouton_degrade_gris = Button(window, text="Gégradé Gris", command= degrade_gris)
Bouton_degrade_gris.grid(row=1, column=0)

Bouton_degrade_2d = Button(window, text="Degra2d", command=degrade_2d)
Bouton_degrade_2d.grid(row=2,column=0)

mainloop()