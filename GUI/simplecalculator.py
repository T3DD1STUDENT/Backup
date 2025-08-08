import tkinter as tk

root = tk.Tk()
root.title("Tedculator")
# root.geometry("300x350")
form_frame = tk.LabelFrame(root, text="Form Feedback")
form_frame.pack(padx=20, pady=20)
email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(form_frame,width=30)
email_entry.grid(row=1, column=1, sticky="ew",padx=(0,10))


root.mainloop()