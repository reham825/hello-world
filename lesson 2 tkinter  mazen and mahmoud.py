from tkinter import *
window = Tk()
window.geometry("400x100")
# window.title("login window")
# name1 = Label(text="first name", font=("bold", 20))
# name1.grid(row=0, column=0, padx=20, pady=20)
# ent1 = Entry(font=("bold", 15))
# ent1.grid(row=0, column=1)
#
# name2= Label(text="lastName", font=("bold", 20))
# name2.grid(row=1, column=0)
#
# ent2 = Entry(font=("bold", 15))
# ent2.grid(row=1, column=1)
#
# btn = Button(text="log in", font=("bold", 15))
# btn.grid(row=2, column=0)
#
#
def increase():
    num = int(number["text"])
    num += 1
    number["text"] = str(num)


def decrease():
    num = int(number["text"])
    num -= 1
    number["text"] = str(num)

plus_button = Button(text="+", font=("bold", 30), command=increase)
minus_button = Button(text="-", font=("bold", 30), command=decrease)
number = Label(text="1", font=("bold", 30))

minus_button.grid(row=0, column=0, padx=10, pady=10)
number.grid(row=0, column=1, padx=10, pady=10)
plus_button.grid(row=0, column=2, padx=10, pady=10)
window.mainloop()