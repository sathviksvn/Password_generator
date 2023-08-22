import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        password = generate_password(length)
        entry_generated_password.delete(0, tk.END)  # Clear any previous content
        entry_generated_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for password length.")

# Create the GUI
root = tk.Tk()
root.title("Password Generator")
root.config(padx=50, pady=25)

def close_win():
    usname=nameentry.get()
    acc_pass=entry_generated_password.get()
    tk.messagebox.showinfo("Accepted Password", f"Accepted password for {usname} is {acc_pass}")
    root.destroy()

def reset_entry():
    entry_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)



#label_font = font.Font(underline=True)


title_lbl=tk.Label(root,text="Password Generator",fg="#000080",anchor="center",font=("Arial",17))
title_lbl.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

name_ent = tk.Label(root, text="Enter User name:")
name_ent.grid(row=1, column=0, padx=5, pady=5)

nameentry = tk.Entry(root)
nameentry.grid(row=1, column=1, columnspan=2)

label_length = tk.Label(root, text="Enter password length:")
label_length.grid(row=2, column=0, padx=5, pady=5)

entry_length = tk.Entry(root)
entry_length.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click,bg="navy",fg="white")
generate_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

generated = tk.Label(root, text="Generated Password:")
generated.grid(row=3, column=0, padx=5, pady=5)

entry_generated_password = tk.Entry(root)
entry_generated_password.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

accept_button = tk.Button(root, text="Accept", command=close_win,fg="navy")
accept_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_entry,fg="navy")

reset_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)


root.mainloop()
