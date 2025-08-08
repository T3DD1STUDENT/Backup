#==========================library=======================#
import tkinter as tk
import time,datetime
from tkinter import ttk
FB=[]
directorti='./HandsomeCafe'
Feedbackpage=tk.Tk()
Feedbackpage.title("Handsome Cafe Feedback Page")
tab=ttk.Notebook(Feedbackpage)
tab.pack
# Feedbackpage.geometry("600x350")
def Startdata():
    try:
        with open(f'{directorti}/log.txt', 'r') as file:
            for fb in file:
                FB.append(fb.strip)
    except FileNotFoundError:
        with open(f'{directorti}/log.txt', 'w') as file:
            for fb in file:
                FB.append(fb.strip)
def Submitdata():
    Nama=Nanswer.get()
    Emali=NEmail.get()
    umpan=NFeedback.get('1.0',tk.END).strip()
    waktu=datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S\n")



Startdata()
Title = tk. LabelFrame(Feedbackpage, text="Feedback Page",relief="solid",font=("pixels", 20,"bold"),fg='Black')
Title.pack(padx=20, pady=20) 
Name = tk.Label(Title, text="Name:",font=("pixels", 15),)
Name.grid(row=3,column=2,sticky='w',pady=10)
Nanswer = tk.Entry(Title,font=("pixels", 15),width=30)
Nanswer.grid(row=3,column=3,padx=10,pady=10)
Email=tk.Label(Title, text="Email:",font=("pixels", 15),)
Email.grid(row=4,column=2,sticky='w',pady=10)
NEmail = tk.Entry(Title,font=("pixels", 15),width=30)
NEmail.grid(row=4,column=3,padx=10,pady=10)
Feetback = tk.Label(Title, text='Feedback:',font=("pixels", 15))
Feetback.grid(row=5,column=2,sticky='nw',pady=10)
NFeedback = tk.Text(Title,font=("pixels", 15),width=30,height=5)
NFeedback.grid(row=5,column=3,padx=10,pady=10,sticky='nsew')
Submit = tk.Button(Title,text='Submit',font=("pixels", 15),fg='black', bg='grey' ,command=Submitdata)
Submit.grid(row=6,column=3,sticky='e',padx=(0,10),pady=(0,10))

Feedbackpage.mainloop()
