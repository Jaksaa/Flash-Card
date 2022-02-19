from tkinter import *
import random
import pandas


try:
    dict = pandas.read_csv("revision_list.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("word_list_en_pl.csv")
    dict = data.to_dict(orient="records")

def random_word():
    global card
    global process
    window.after_cancel(process)
    card = random.choice(dict)
    canvas.itemconfig(word_in_language, text=f"{card['English']}", fill="black")
    canvas.itemconfig(langauge, text="English", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    process = window.after(3000, card_flip)

def card_flip():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(langauge, text="Polish", fill="white")
    canvas.itemconfig(word_in_language, text=f"{card['Polish']}", fill="white")

def known_answer():
    dict.remove(card)
    data = pandas.DataFrame(dict)
    data.to_csv("revision_list.csv", index=False)
    random_word()

window = Tk()
window.title("Flash Cards")
window.minsize(width=1000,height=500)
window.config(padx=50,pady=50,bg="#B0DBC4")

process = window.after(3000, card_flip)

card_back = PhotoImage(file="card_back.png")
cross_image = PhotoImage(file="wrong.png")
tick_image = PhotoImage(file="right.png")
card_front = PhotoImage(file="card_front.png")

canvas = Canvas(width=900, height=600, bg="#B0DBC4",highlightthickness=0)
canvas_image = canvas.create_image(450,280, anchor='center', image=card_front)
langauge = canvas.create_text(420,150, text="", font=('Ariel', 40, "italic"))
word_in_language = canvas.create_text(420,300, text="", font=('Ariel', 20, "bold"))
canvas.grid(column=0,row=0,columnspan=3)


check_button = Button(image=tick_image,highlightthickness=0, command=known_answer)
check_button.grid(column=0,row=2)

cross_button = Button(image=cross_image,highlightthickness=0,command=random_word)
cross_button.grid(column=2,row=2)


random_word()


window.mainloop()