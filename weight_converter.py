from tkinter import *

window = Tk()

# define function for conversion
def convert_from_kg():
    grams = float(entry_value.get()) * 1000
    pounds = float(entry_value.get()) * 2.20462
    ounces = float(entry_value.get()) * 35.274

    text1.insert(END, grams)
    text2.insert(END, pounds)
    text3.insert(END, ounces)

# set labels for units
# add text box for conversion answers
label = Label(window, text="Kg")
label.grid(row=0, column=0)

entry_value = StringVar()
entry = Entry(window, textvariable=entry_value)
entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=convert_from_kg)
button.grid(row=0, column=2)

label = Label(window, text="Grams")
label.grid(row=1, column=0)

text1 = Text(window, height=1, width=20)
text1.grid(row=2, column=0)

label = Label(window, text="Pounds")
label.grid(row=1, column=1)

text2 = Text(window, height=1, width=20)
text2.grid(row=2, column=1)

label = Label(window, text="Ounces")
label.grid(row=1, column=2)

text3 = Text(window, height=1, width=20)
text3.grid(row=2, column=2)

window.mainloop()