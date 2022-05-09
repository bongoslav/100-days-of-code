from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adding padding to all elements


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# Configure a value for a key
my_label["text"] = "New text"
my_label.config(text="New text")
my_label.config(pady=100)  # Adding padding to a single element

# Button
def button_clicked():
    my_label["text"] = entry.get()


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Button2")
button2.grid(column=2, row=0)


# Entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.get()  # Returns the input the user gives
entry.grid(column=3, row=3)


window.mainloop()