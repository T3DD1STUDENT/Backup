import tkinter as tk
root = tk.Tk()
root.title("Raffaels Porn")

root.geometry("600x350")
text1=tk.Label(root, text="PORN",relief="solid",font=("pixels", 20,"bold"),fg='Orange',bg='black')
text2=tk.Label(root, text="HUB",relief="solid",font=("pixels", 20,"bold"),fg='black',bg='Orange')
text3=tk.Label(root, text="ACC=Raffael J G",font=("pixels", 12,"bold"),fg='black')
text1.grid(row=1,column=5)
text2.grid(row=1,column=6)
text3.grid(row=2,column=5,columnspan=2)

root.mainloop() 