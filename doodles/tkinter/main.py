import tkinter


def button_clicked():
    print("I got clicked")


def update_label():
    # my_label.config(text="I got clicked")
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # add padding

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "bold"))
# my_label.pack()  # Place it on the screen and centre it
# my_label["text"] = "New text"
my_label.grid(row=0, column=0)
my_label.config(text="new new text")


# Button
button = tkinter.Button(text="Click me", command=update_label)
# button.pack()
button.grid(row=1, column=1)

# New Button
new_button = tkinter.Button(text="Shiny new button")
new_button.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(row=2, column=3)
print(input.get())




# Must be the last line of code for tkinter to work correctly
window.mainloop()
