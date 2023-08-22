from tkinter import *
import pandas
import random


# Constants
BACKGROUND_COLOR = "#B1DDC6"

random_word_pair = {}
words_to_learn = {}


try:
    # Read data from csv
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words_testing.csv")
finally:
    word_dictionary = pandas.DataFrame.to_dict(word_data, orient="records")

# print(word_dictionary)
# print(word_dictionary[4]['French'])


# Random word selection -----------------------------------------------------------------------------------------------
def gen_random_word():
    global random_word_pair, flip_timer
    window.after_cancel(flip_timer)
    if len(word_dictionary) > 0:
        random_word_pair = random.choice(word_dictionary)
        flash_card_canvas.itemconfig(canvas_image, image=card_front_image)
        flash_card_canvas.itemconfig(canvas_word_text, text=random_word_pair['French'], fill="black")
        flash_card_canvas.itemconfig(canvas_lang_text, text="French", fill="black")
        flip_timer = window.after(3000, func=flip_card)
    else:
        print("no more words to learn")


# Flip cards ----------------------------------------------------------------------------------------------------------
def flip_card():
    flash_card_canvas.itemconfig(canvas_image, image=card_back_image)
    flash_card_canvas.itemconfig(canvas_word_text, fill="white", text=random_word_pair['English'])
    flash_card_canvas.itemconfig(canvas_lang_text, fill="white", text="English")


# Remove known word pairs from list -----------------------------------------------------------------------------------
def remove_known_word_pair():
    global random_word_pair, word_dictionary
    if len(word_dictionary) > 0:
        del word_dictionary[word_dictionary.index(random_word_pair)]

        df = pandas.DataFrame.from_dict(word_dictionary)
        df.to_csv("data/words_to_learn.csv", index=False)

        # Validation
        print(pandas.read_csv("data/words_to_learn.csv"))

    else:
        print("no more words to remove")


# GUI -----------------------------------------------------------------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Images
checkmark_image = PhotoImage(file="images/right.png")
xmark_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

# Flash card canvas
flash_card_canvas = Canvas(window, width=800, height=526)
canvas_image = flash_card_canvas.create_image(400, 263, image=card_front_image)
# x & y positions relative to canvas
canvas_lang_text = flash_card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word_text = flash_card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
flash_card_canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(column=0, row=0, columnspan=2)

# X mark button
xmark_button = Button(image=xmark_image, highlightthickness=0, command=gen_random_word)
xmark_button.grid(column=0, row=1)

# Check mark button
checkmark_button = Button(image=checkmark_image, highlightthickness=0, command=remove_known_word_pair)
checkmark_button.grid(column=1, row=1)

gen_random_word()





window.mainloop()
