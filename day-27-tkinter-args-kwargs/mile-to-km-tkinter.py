from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

equal = Label(text=0)
equal.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)


def button_clicked():
    miles = float(entry.get())
    km = miles * 1.609
    equal.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()