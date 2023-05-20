import tkinter
import Connect4
from tkinter import *
from tkinter import messagebox

window=tkinter.Tk()
window.title("Connect 4")

algorithm = StringVar()
difficulty = tkinter.StringVar()

def startGame():
    chosen_algorithm = algorithm.get()
    chosen_difficulty = difficulty.get()

    Connect4.Game(chosen_algorithm,chosen_difficulty)

#Choosing the algorithm type
label = tkinter.Label(window,text="Select an Algorithm")
label.pack()

alphabetaButton=tkinter.Radiobutton(window,text="Alpha-Beta",variable=algorithm,value="Alpha-Beta")
alphabetaButton.pack()

minimaxButton=tkinter.Radiobutton(window,text="Minimax",variable=algorithm,value ="Minimax")
minimaxButton.pack()

#Choosing the difficulty level
labell = tkinter.Label(window,text="Select a difficulty level")
labell.pack()

easyRadioButton=tkinter.Radiobutton(window,text="Easy",variable=difficulty,value="Easy")
easyRadioButton.pack()

mediumRadioButton=tkinter.Radiobutton(window,text="Medium",variable=difficulty,value="Medium")
mediumRadioButton.pack()

hardRadioButton=tkinter.Radiobutton(window,text="Hard",variable=difficulty,value="Hard")
hardRadioButton.pack()

startButton=tkinter.Button(window,text="Start Game",command=startGame)
startButton.pack()


window.mainloop()


