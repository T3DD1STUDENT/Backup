#==========================library=======================#
import tkinter as tk
import time,datetime
from tkinter import ttk,messagebox

#==========================variable=======================#
FB=[]
fb=''
directorti='./HandsomeCafe'
#==========================function=======================#
def buatTab(mainFrame, titleTab):
    frame=ttk.Frame(mainFrame)
    mainFrame.add(frame, text=titleTab)
    return frame
def Startdata():
    try:
        with open(f'{directorti}/log.txt', 'r') as file:
            # for fb in file:
            #     FB.append(fb.strip)
            FB=file.readlines()
            return FB
    except FileNotFoundError:
        with open(f'{directorti}/log.txt', 'w') as file:
            file.write(f'Feedback\n')
def clear():
    Nanswer.delete(0,tk.END)
    NEmail.delete(0,tk.END)
    NFeedback.delete('1.0',tk.END)

def Submitdata():
    Nama=Nanswer.get()
    if Nama == '':
        Nama='Anonymous'
    Emali=NEmail.get()
    if Emali == '':
        Emali='Anonymous'
    umpan=NFeedback.get('1.0',tk.END).strip()
    if not umpan:
        messagebox.showerror("Error","Feedback tidak boleh kosong")
        return
    waktu=datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S\n")
    with open(f'{directorti}/log.txt','a') as file:
        file.write(f'{waktu}nama: {Nama}\nemail: {Emali}\nfeedback: {umpan}\n')
        file.write(f"{'='*100}\n")
    messagebox.showinfo("Success","Feedback berhasil dikirim")
    clear()
#==========================main=======================#
Feedbackpage=tk.Tk()
Feedbackpage.title("Handsome Cafe Feedback Page")
tab=ttk.Notebook(Feedbackpage)
tab.pack(expand=True, fill="both")
tab1=buatTab(tab, "MainPage")
tab2=buatTab(tab, "Display Feedback")

#==========================Submain tab1=======================#
FB=Startdata()
Title = tk. LabelFrame(tab1, text="Feedback Page",relief="solid",font=("pixels", 20,"bold"),fg='Black')
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

#============================Submain tab2=======================#

Title2 = tk. LabelFrame(tab2, text="View Feedback")
Title2.pack(padx=20, pady=20)

Name = tk.Listbox(Title2,width=50)
Name.pack()
for i in FB:
    Name.insert(tk.END,i)



Feedbackpage.mainloop()
