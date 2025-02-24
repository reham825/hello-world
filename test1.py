from tkinter import *
import random
window=Tk()
colours = ["red", "blue", "brown", "black", "green"]
time=30

#start game function
def start_game():
    global colours
    colour_text["text"]= colours[0]
    colour_text["fg"]=colours[1]
    random.shuffle(colours)
txt1=Label(text="type in the colour of the wotd not the word text", font=("bold", 20))
txt1.pack()
txt2=Label(text="press enter to start", font=("bold", 20))
txt2.pack()
time=Label(text="time left = 30", font=("bold", 20))
time.pack()
colour_text = Label(text="", font=("bold", 40))
colour_text.pack()
ent = Entry(width=40)
ent.pack()
start_game()
window.mainloop()