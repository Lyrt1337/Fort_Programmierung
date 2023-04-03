import pandas as pd
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Vehicle Registration")
root.geometry("600x600")

def button_apply():
    pass





def check(*args):
    if var1.get() == "Car":
        label6.config(text="Number of Doors:")
        label7.config(text="Number of Seats:")
        label8.config(text="Warranty:")

    if var1.get() == "Motorbike":
        label6.config(text="Number of Mirrors:")
        label7.config(text="Bodykit:")
        label8.config(text="Exhaust:")

    if var1.get() == "Truck":
        label6.config(text="Hanger Length:")
        label7.config(text="Load Capacity:")
        label8.config(text="Special Permit")

    if var1.get() == "unspecified":
        label6.config(text="")
        label7.config(text="")
        label8.config(text="")


# Dropdown
options = ["Car", "Motorbike", "Truck", "unspecified"]
var1 = StringVar()
var1.set(options[3])
var1.trace('w', check)
old_var = "unspecified"

drop = OptionMenu(root, var1, *options)
drop.grid(row=0, column=0)


# Color
color_label = Label(root, text="Color")
color_label.grid(row=1, column=0, columnspan=3)
e_color = Entry(root, width=20, borderwidth=3)
e_color.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

# Brand
brand_label = Label(root, text="Brand")
brand_label.grid(row=2, column=0, columnspan=3)
e_brand = Entry(root, width=20, borderwidth=3)
e_brand.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

# Construction Year
construct_label = Label(root, text="Construction Year")
construct_label.grid(row=3, column=0, columnspan=3)
e_construct = Entry(root, width=20, borderwidth=3)
e_construct.grid(row=3, column=3, columnspan=2, padx=10, pady=10)

# Tyres
tyres_label = Label(root, text="Number of Tyres")
tyres_label.grid(row=4, column=0, columnspan=3)
e_tyres = Entry(root, width=20, borderwidth=3)
e_tyres.grid(row=4, column=3, columnspan=2, padx=10, pady=10)

# Power
power_label = Label(root, text="Power (PS)")
power_label.grid(row=5, column=0, columnspan=3)
e_power = Entry(root, width=20, borderwidth=3)
e_power.grid(row=5, column=3, columnspan=2, padx=10, pady=10)

# mirrors
label6 = Label(root, text="")
label6.grid(row=6, column=0, columnspan=3)
e_6 = Entry(root, width=20, borderwidth=3)
e_6.grid(row=6, column=3, columnspan=2, padx=10, pady=10)

# bodykit
label7 = Label(root, text="")
label7.grid(row=7, column=0, columnspan=3)
e_7 = Entry(root, width=20, borderwidth=3)
e_7.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

# exhaust
label8 = Label(root, text="")
label8.grid(row=8, column=0, columnspan=3)
e_8 = Entry(root, width=20, borderwidth=3)
e_8.grid(row=8, column=3, columnspan=2, padx=10, pady=10)

# Button

# apply = Button(root, text="apply",  command=EntryField.apply())
# apply.grid(row=8, column=3)
# print(objdata)
root.mainloop()
