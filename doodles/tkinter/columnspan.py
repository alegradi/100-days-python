from tkinter import *

window = Tk()
window.title("Testing column width")

red_label = Label(background="red", width=20, height=10)
red_label.grid(column=0, row=0)

green_label = Label(background="green", width=20, height=10)
green_label.grid(column=1, row=1)

blue_label = Label(background="blue", width=40, height=10)
blue_label.grid(column=0, row=2, columnspan=2)

window.mainloop()
