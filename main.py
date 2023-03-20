from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 260, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

language_label = Label(text="Spanish", font=("Arial", 40, "italic"), background="#ffffff")
language_label.place(relx=0.5, rely=0.25, anchor='center')

word_label = Label(text="Spanish", font=("Arial", 60, "bold"), background="#ffffff")
word_label.place(relx=0.5, rely=0.45, anchor='center')

wrong_button = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_button, highlightthickness=0)
button1.grid(column=0, row=1)

right_button = PhotoImage(file="images/right.png")
button2 = Button(image=right_button, highlightthickness=0)
button2.grid(column=1, row=1)

window.mainloop()
