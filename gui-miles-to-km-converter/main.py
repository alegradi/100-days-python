import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=125)
window.config(padx=40, pady=20)


def convert_miles_to_km():
    result = "{:.2f}".format(float(input_field.get()) * 1.60934)
    result_label.config(text=result)  # .config to update widget, easy to miss


# miles_label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# equal_to_label
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

# result_label
result_label = tkinter.Label(text="result")
result_label.grid(column=1, row=1)

# km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
# calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)


# Entry point
input_field = tkinter.Entry(width=10)
input_field.grid(column=1, row=0)
print(input_field.get())

window.mainloop()
