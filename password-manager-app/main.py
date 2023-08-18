from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entries():
    """
    Use when the "Add" button is pressed.
    """
    # Get data from entry fields
    website_entry_data = website_entry.get()
    username_entry_data = username_entry.get()
    password_entry_data = password_entry.get()

    new_data = {website_entry_data: {
        "email": username_entry_data,
        "password": password_entry_data
    }}

    if len(website_entry_data) == 0 or len(password_entry_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # With error handling, creates if there is no file
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new one
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear the entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    password_lookup = website_entry.get()

    try:
        # Check if password_lookup matches an item in data.json
        with open("data.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Data File Found")
    else:
        # List of dictionary lookup
        found_password_entry = {key: value for (key, value) in json_data.items() if key == password_lookup}
        # print(f"Found entry: {found_password_entry}")  # Debug info

        # Show pop-up if entry found
        if len(found_password_entry) > 0:
            messagebox.showinfo(title=password_lookup, message=f"Email/Username: "
                                                               f"{found_password_entry[password_lookup]['email']} "
                                                               f"\nPassword: "
                                                               f"{found_password_entry[password_lookup]['password']}")
        else:
            messagebox.showinfo(title="Missing Record", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website entry
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Email/Username entry
username_entry = Entry(width=42)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(index=0, string="ferko_ferdinand@gmail.com")

# Password entry
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Generate password button
gen_pass_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
gen_pass_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=41, highlightthickness=0, command=save_entries)
add_button.grid(column=1, row=4, columnspan=2)

# Search button
search_button = Button(text="Search", highlightthickness=0, width=16, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()
