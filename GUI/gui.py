import tkinter as tk
import time
def x():
    print('Thank you for using this program')
    text2=tk.Label(root, text='Error',fg='red',bg='black')
    text2.pack()
    time.sleep(1)
    text2.destroy
def y():
    print('abslima DASAR')
    text2.pack_forget()
root = tk.Tk()
root.title("Teds Shop Help Center")
root.geometry("600x350")

text1=tk.Label(root, text="Welcome to the Teds Shop Help Center",relief="solid",font=("pixels", 20,"bold"),fg='Orange',bg='black')
text2=tk.Label(root, text="Powered by Tedcode")
text3=tk.Label(root, text="www.tedshop.com")
text2.pack() 
text1.pack() 
text3.pack()
tombol=tk.Button(root, text="add", command=y,fg='red',bg='black',font=("Roboto", 15,"bold"))
tombol.pack()
tombol2=tk.Button(root, text="delete", command=x,fg='red',bg='black',font=("Roboto", 15,"bold"))
tombol2.pack()
root.mainloop() 