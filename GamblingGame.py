from tkinter import *
from random import *
import sys

# 전역변수

def Start():
    gamblingLabel.place_forget()
    startButton.place_forget()
    quitButton.place_forget()

    n = 15
    for i in range(0, 3):
        button[i].place(x=n, y=50)
        n += 60

def Quit():
    sys.exit()

def numChange(button, n):
    num = randint(0, 3)
    button.configure(text=num)
    button.configure(bg="#ffe37a")

    if (n == 2):
        equalNum(button1['text'], button2['text'], button3['text'])

def equalNum(n1, n2, n3):
    if (n1 == n2):
        if (n1 == n3):
            text1 = "SUCCESS!!"
            xx = 40
        else:
            text1 = "FAIL"
            xx = 75
    else:
        text1 = "FAIL"
        xx = 75

    text2 = "[Click to do again]"

    resultLabel1.configure(text=text1)
    resultLabel2.configure(text=text2)
    resultLabel1.place(x=xx, y=130)
    resultLabel2.place(x=10, y=160)

def ReStart(event):
    resultLabel1.place_forget()
    resultLabel2.place_forget()

    button1.configure(text=0, bg="#ffcfbc")
    button2.configure(text=0, bg="#ffcfbc")
    button3.configure(text=0, bg="#ffcfbc")

# elt
window = Tk()
window.title("Unit Converter")
window.geometry("200x240")
window.resizable(False, False)
window.configure(bg="#ffa07a")

# main
gamblingLabel = Label(window, text="GamblingGame", bg="#ffa07a")
startButton = Button(window, text="Start", width="10", command=Start)
quitButton = Button(window, text="Quit", width="10", command=Quit)
gamblingLabel.configure(font=("Arial", 18))
startButton.configure(font=("Courier", 16))
quitButton.configure(font=("Courier", 16))


# start
button1 = Button(window, text=0, width="3", height="2", bg="#ffcfbc", command = lambda : numChange(button1, 0))
button2 = Button(window, text=0, width="3", height="2", bg="#ffcfbc", command = lambda : numChange(button2, 1))
button3 = Button(window, text=0, width="3", height="2", bg="#ffcfbc", command = lambda : numChange(button3, 2))
button = [button1, button2, button3]

button1.configure(font=("Courier", 16))
button2.configure(font=("Courier", 16))
button3.configure(font=("Courier", 16))

resultLabel1 = Label(window, text="", fg="blue", bg="#ffa07a")
resultLabel2 = Label(window, text="", fg="blue", bg="#ffa07a")
resultLabel1.configure(font=("Arial", 16))
resultLabel2.configure(font=("Arial", 16))
resultLabel2.bind('<Button-1>', ReStart)

# place
gamblingLabel.place(x=10, y=50)
startButton.place(x=30, y=120)
quitButton.place(x=30, y=170)


window.mainloop()
