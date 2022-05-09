import csv
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = {}

# ---------------------------- CHECK IF THERE ARE WORDS TO LEARN ------------------------------- #
try:
    to_learn = pd.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    # create words_to_learn.csv if it's the first time running the program
    french_words_data = pd.read_csv("./data/french_words.csv")
    french_words_data.to_csv("./data/words_to_learn.csv", index=False)
    to_learn = french_words_data.to_dict(orient="records")


# ---------------------------- GENERATE RANDOM FRENCH WORDS ------------------------------- #
def next_card(button_id):
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(3000, func=flip_card)
    # Check if check button was clicked and update the words to learn file
    if button_id == 1:
        to_learn.remove(current_card)
        data = pd.DataFrame(to_learn)
        data.to_csv("./data/words_to_learn.csv")

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_card)


# ---------------------------- UI SETUP ------------------------------- #
# Flash cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
language_text = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Tick and cross images
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=lambda: next_card(1))
right_button.grid(column=1, row=1)
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=lambda: next_card(2))
wrong_button.grid(column=0, row=1)

# Card flipper
flip_timer = window.after(3000, func=flip_card)
next_card(2)

window.mainloop()
