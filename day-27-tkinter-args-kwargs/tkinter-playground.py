from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adding padding to all elements


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # place the component my_label in the window; place(x, y), pack or grid(col, row) can be used

# Configure a value for a key
my_label["text"] = "New text"
my_label.config(text="New text")
my_label.config(pady=100)  # Adding padding to a single element


# Button
def button_clicked():
    my_label["text"] = entry.get()


button = Button(text="Click Me", command=button_clicked)
button.place(x=50, y=100)


# Entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.get()  # Returns the input the user gives
entry.pack()


# Text
text = Text(height=5, width=30)
text.focus()  # Puts the cursor in the textbox.
text.insert(END, "Example of multi-line text.")
text.get("1.0", END)  # gets current value in textbox at line 1, character 0


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    #  Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()