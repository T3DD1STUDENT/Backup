#=========================library=========================#
import tkinter as tk

def count():
    ok=equition.get()
#=========================main=========================#
root = tk.Tk()
root.title('Tedculator')
root.geometry('400x500')
equition=tk.StringVar()
entry=tk.Entry(root,textvariable=equition)
entry.grid(row=0,column=0,columnspan=5)
plus=tk.Button(root,text='+',bg='lightblue',command=lambda:equition.set(equition.get()+'+'))#Tambah
plus.grid(row=1,column=0)
min=tk.Button(root,text='-',bg='lightblue',command=lambda:equition.set(equition.get()+'-'))
min.grid(row=1,column=1)
x=tk.Button(root,text='x',bg='lightblue',command=lambda:equition.set(equition.get()+'*'))
x.grid(row=1,column=2)
bagi=tk.Button(root,text=':',bg='lightblue',command=lambda:equition.set(equition.get()+'/'))
bagi.grid(row=1,column=3)
answer=tk.Button(root,text='=',bg='lightblue',command=lambda:equition.set(eval(equition.get())))
answer.grid(row=1,column=4)
clear=tk.Button(root,text='clear',bg='lightblue',command=lambda:equition.set(''))
clear.grid(row=2,column=0)
root.mainloop()
#display
#fungsi