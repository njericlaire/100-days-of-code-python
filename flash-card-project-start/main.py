from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word={}
to_learn={}

try:
    data=pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data=pandas.read_csv("./data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")





def next_card():
    global current_word,flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French" ,fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=word_front)
    window.after(3000,func=flash_card)
def flash_card():
    canvas.itemconfig(canvas_image, image=word_back)
    canvas.itemconfig(title_text,text="English" ,fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
def is_known():
    to_learn.remove(current_word)
    data_left=pandas.DataFrame(to_learn)
    data_left.to_csv("./data/word_to_learn.csv")
    next_card()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)


flip_timer=window.after(3000, func=flash_card)

my_image = PhotoImage(file="./images/right.png")
right = Button(image=my_image, highlightthickness=0,command=is_known)
right.grid(row=1,column=1)


my_image1 = PhotoImage(file="./images/wrong.png")
left = Button(image=my_image1, highlightthickness=0,command=next_card)
left.grid(row=1,column=0)

canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
word_front=PhotoImage(file="./images/card_front.png")
word_back=PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(400,263,image=word_front)

title_text=canvas.create_text(400,150,text="French", fill="black", font=("Ariel",40,"italic") )
word_text=canvas.create_text(400,263,text="trouve", fill="black", font=("Ariel",60,"bold") )
canvas.grid(row=0,column=0,columnspan=2)

next_card()

window.mainloop()


