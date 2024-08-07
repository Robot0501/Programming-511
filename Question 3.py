# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:23:57 2024

@author: SuhaylTager
"""

import tkinter as tk
from tkinter import ttk

# Declare the tkinter window's variable
window = tk.Tk() 

window.title("Inventory Management System")

# initialise all variables from
# the entry box's input
name_var = ''
descrip_var = ''
quant_var = ''
price_var = ''

# Set the size of the tkinter window
window.geometry("500x500")

# Create the label for the Name entry box
label1 = ttk.Label(window, text="Name:")
label1.grid(column=1,row=2)

# Create the entry box to obtain use input
entrybox1 = ttk.Entry(window, textvariable=name_var)
entrybox1.grid(column=2,row=2)

# Create the label for the Description entry box
label2 = ttk.Label(window, text="Description:")
label2.grid(column=1,row=3)

# Create the entry box to obtain use input
entrybox1 = ttk.Entry(window, textvariable=descrip_var)
entrybox1.grid(column=2,row=3)

# Create the label for the Quantity entry box
label3 = ttk.Label(window, text="Quantity:")
label3.grid(column=1,row=4)

# Create the entry box to obtain use input
entrybox1 = ttk.Entry(window, textvariable=quant_var)
entrybox1.grid(column=2,row=4)

# Create the label for the Price entry box
label4 = ttk.Label(window, text="Price:")
label4.grid(column=1,row=5)

# Create the entry box to obtain use input
entrybox1 = ttk.Entry(window, textvariable=price_var)
entrybox1.grid(column=2,row=5)


button1 = ttk.Button(window, text="Add Product")
button1.grid(column=1,row=6)

button1 = ttk.Button(window, text="Update Product")
button1.grid(column=2,row=6)

button1 = ttk.Button(window, text="Delete Product")
button1.grid(column=3,row=6)

window.mainloop()