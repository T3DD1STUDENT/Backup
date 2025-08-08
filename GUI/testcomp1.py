import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Entry")

'''def greet():
    name = entry.get()
    print("Hello,", name)

label = ttk.Label(root, text="Enter your name:")
label.pack()

entry = ttk.Entry(root)
entry.pack()

label2 = ttk.Label(root, text="Enter your creditcard information:")
label2.pack()

entry2 = ttk.Entry(root)    
entry2.pack()

button = ttk.Button(root, text="next", command=greet)
button.pack()

root.mainloop()'''

def create_biodata(root):
    #Create label and entries for name, age, and address
    name_label = tk.Label(root, text="Skibedi toilets")
    name_label.grid(row=0, column=0)

