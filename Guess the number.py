import os.path
import random
from tkinter import *
import os, sys

screen = Tk()
screen.configure(background="black")
screen.geometry('350x300')
screen.title("Geess the number")
screen.resizable(height=False, width=False)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


tries = 0
up = PhotoImage(file=resource_path("uparrow.png"))
down = PhotoImage(file=resource_path("downarrow.png"))
correct = PhotoImage(file=resource_path("correct.png"))
dice = PhotoImage(file=resource_path("dice.png"))


def checka(event):
    global x, tries
    b = int(e.get())
    e.delete(0, END)
    if b == x:
        lbl9.configure(image=correct)
    elif b > x:
        lbl9.configure(image=down)
    elif b < x:
        lbl9.configure(image=up)

    tries += 1
    lbl8.configure(text="Tries:" + str(tries))
    e.delete(0, END)


def randomize():
    global x
    a = choice.get()
    if a == 1:
       x = random.randint(0, 50)
       #print(x)
    elif a == 2:
        x = random.randint(0, 100)
        #print(x)
    else:
        x = random.randint(0, 200)
        #print(x)

    tries = 0
    lbl8.configure(text="Tries:" + str(tries))
    e.delete(0, END)
    lbl9.configure(image=dice)


choice = IntVar()
choice.set(1)



lbl = Label(screen, text="GUESS THE NUMBER", background="black", foreground="light blue")
lbl.grid(row=0, column=1, columnspan=3)


lbl1 = Label(screen, text="", background="black", foreground="light blue")
lbl1.grid(row=1, column=1, columnspan=3)


rb = Radiobutton(screen, text="Easy:0-50", value=1, variable=choice, background="black", foreground="light blue")
rb.grid(row=2, column=1)

rb2 = Radiobutton(screen, text="Medium:0-100", value=2, variable=choice, background="black", foreground="light blue")
rb2.grid(row=2, column=2)

rb3 = Radiobutton(screen, text="Hard:0-200", value=3, variable=choice, background="black", foreground="light blue")
rb3.grid(row=2, column=3)


lbl4 = Label(screen, text="", background="black", foreground="light blue")
lbl4.grid(row=3, column=1, columnspan=3)


lbl5 = Label(screen, text="-In this game you will try to guess the right number that", background="black", foreground="light blue")
lbl5.grid(row=4, column=1, columnspan=3)
lbl6 = Label(screen, text=" is randomly chosen every round with the least possible tries", background="black", foreground="light blue")
lbl6.grid(row=5, column=1, columnspan=3)


lbl7 = Label(screen, text="", background="black", foreground="light blue")
lbl7.grid(row=6, column=1, columnspan=3)


e = Entry(screen)
e.grid(row=7, column=2)


btn = Button(screen, text="Exit", background="black", foreground="light blue")
btn.grid(row=7, column=3)


lbl9 = Label(screen, image=dice, background="black", foreground="light blue")
lbl9.grid(row=8, rowspan=8, column=1)


lbl8 = Label(screen, text="Tries:", background="black", foreground="light blue")
lbl8.grid(row=8, column=2)


btn1 = Button(screen, text="Randomize", background="black", foreground="light blue", command=randomize)
btn1.grid(row=8, column=3)







screen.bind('<Return>', checka)

screen.mainloop()