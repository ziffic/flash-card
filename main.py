from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def new_word():
    canvas.delete(word_learning)
    word_learning = canvas.create_text(400, 263, text="placeholder", font=("Arial", 60, "bold"))


data = pandas.read_csv("data/french_words.csv")
data_dic = data.to_dict(orient="records")
print(data_dic)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_learning = canvas.create_text(400, 263, text="placeholder", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=0)

right_button = PhotoImage(file="images/right.png")
known_button = Button(image=right_button, highlightthickness=0, command=new_word)
known_button.grid(row=1, column=1)

window.mainloop()
