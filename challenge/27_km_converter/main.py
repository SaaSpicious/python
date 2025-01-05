from tkinter import *


def miles_to_km(miles):
    return int(miles * 1.6)


def button_clicked():
    miles = int(input.get())
    output_text.config(text=miles_to_km(miles))


window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

# Labeling
mile_text = Label(text="equals to ",font=("Arial",16,"bold"))
mile_text.grid(column=0, row=2)

input = Entry(width=20)
input.grid(column=1, row=1)

mile_text_2 = Label(text="km",font=("Arial",16,"bold"))
mile_text_2.grid(column=2, row=1)

output_text = Label(text="0",font=("Arial",16,"bold"))
output_text.grid(column=1, row=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()