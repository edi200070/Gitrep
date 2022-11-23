import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image


def activate_organizer():
    with open(r"output.txt", "w") as a:
        os.chdir(entry_text.get()) 
        for count, f in enumerate(os.listdir()):
            f_name, f_ext = os.path.splitext(f)
            a.write(f_name + os.linesep)

#Code from the Rename funktion
def Rename():
    os.chdir(entry_text.get()) 
    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = entry_text2.get() + str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)

#Code drom the convert funktion   
def convert():
    print(dropdownValue1 , dropdownValue2)
    ToConvertFile = entry_text.get(),entry_text2.get()
    print(ToConvertFile)
    im1 = Image.open(entry_text.get() + "\\" + str(os.path.splitext(entry_text2.get())[0] + dropdownValue1))
    im1.save(entry_text.get()+ "\\"  + str(os.path.splitext(entry_text2.get())[0] + dropdownValue2))

#click dropdown menu
def callback1(value):
    global dropdownValue1 
    dropdownValue1 = value

#click dropdown menu 2
def callback2(value):
    global dropdownValue2 
    dropdownValue2 = value

answer = ""
# root window
root = tk.Tk()
root.geometry('300x175')
root.resizable(False, False)
root.title('folder_organizer')

#Code from first button
button1 = ttk.Button(
    root,
    text='Get all Filenames',
    command=activate_organizer
)
button1.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
button1.place(x=15, y=125)

#Code from second button
button2 = ttk.Button(
    root,
    text='Rename Files',
    command=Rename
)

button2.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
button2.place(x=200, y=125)

#Code from first Textfeld (Dateiordnen)
entry_text = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_text) 
new_Text = r""
entry_text.set(new_Text)
entry.place(x=110, y=0, height=18, width=185)

#Code from "folder pathname :"
Labelka = tk.Label(root, text="folder pathname :")
Labelka.place(x = 0, y = 0)

#Code from second Textfield ("new filename :")
entry_text2 = tk.StringVar()
entry2 = tk.Entry(root,textvariable=entry_text2) 
new_Text2 = ""
entry_text2.set(new_Text2)
entry2.place(x=110, y=20, height=18, width=185)

#Code from "filename :"
Labelka = tk.Label(root, text="filename :")
Labelka.place(x = 0, y = 20)

#menu
options = [
    ".png",
    ".jpg"
]

#datatype of menu text
clicked = StringVar()
clicked2 = StringVar()

#initial menu text
clicked.set( "datatype" )
clicked2.set( "datatype" )
  
#Creates Dropdown menu
drop = OptionMenu( root , clicked , *options, command=callback1 )
drop.pack()
drop.place( x = 10, y = 60)
dropdownValue1 = "" 

#Creates Dropdown  menu 2
drop2 = OptionMenu( root , clicked2 , *options, command=callback2 )
drop2.pack()
drop2.place( x = 200, y = 60)
dropdownValue2 = "" 

#Code from "from"
Labelka = tk.Label(root, text="from")
Labelka.place(x = 10, y = 40)

#Code from "to"
Labelka = tk.Label(root, text="to")
Labelka.place(x = 200, y = 40)

#Code from convert button
button3 = ttk.Button(
    root,
    text='Convert',
    command=convert
)

button3.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

button3.place(x=118, y=125)

root.mainloop()