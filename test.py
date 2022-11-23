import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image

def Inch_Convert_To_Cm():
    Input_Text = entry1.get()
    cm_distance = float(Input_Text)
    inch_distance = cm_distance*2.54
    answer = inch_distance
    new_text = ""
    entry_text.set(new_text)
    new_Output_Text = inch_distance
    output_text.set(new_Output_Text)

def Cm_Convert_To_Inch():
    Input_Text = entry1.get()
    cm_distance = float(Input_Text)
    inch_distance = cm_distance/2.54
    answer = inch_distance
    new_text = ""
    entry_text.set(new_text)
    new_Output_Text = inch_distance
    output_text.set(new_Output_Text)

answer = ""
# root window
root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('measure_converter')

#button
button1 = ttk.Button(
    root,
    text='Cm to Inch',
    command=Cm_Convert_To_Inch
)
button1.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
button1.place(x=50, y=200)

button2 = ttk.Button(
    root,
    text='Inch to cm',
    command=Inch_Convert_To_Cm
)
button2.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
button2.place(x=350, y=200)

entry_text = tk.StringVar()
entry1 = tk.Entry(root,textvariable=entry_text) 
new_Text = ""
entry_text.set(new_Text)
entry1.place(x= 210, y=200, width=125)

output_text = tk.StringVar()
Output_Text = Label(root, textvariable=output_text, font= ('Aerial 17 bold italic')).pack(pady= 30)
new_Output_Text = ""
output_text.set(new_Output_Text)

Labelka = tk.Label(root, text="input field :")
Labelka.place(x = 130, y = 200)

root.mainloop()