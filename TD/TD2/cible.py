from tkinter import *

window = Tk()

canvas = Canvas(window, width=600,height =600,background="black")
canvas.grid()

colors = ["blue", "green", "black", "yellow", "magenta", "red"]

for i in range(600, 0, -20):
    print(i, 600 - i)
    canvas.create_oval(600 - i, 600 - i, i, i, fill=colors[((600 - i) // 20) % len(colors)])

mainloop()