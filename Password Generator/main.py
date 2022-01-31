import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ----------------------------Generate Password---------------------------
def gen_pass():
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    numbers = [str(i) for i in range(0, 10)]
    symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

    let = random.randint(8, 10)
    num = random.randint(2, 4)
    sym = random.randint(2, 4)
    st = ""

    num_let = random.sample(letters, let)
    num_num = random.sample(numbers, num)
    num_sym = random.sample(symbols, sym)

    new_password = num_let + num_num + num_sym
    random.shuffle(new_password)
    new_pass = st.join(new_password)
    password.delete(0, 'end')
    password.insert(0, new_pass)
    pyperclip.copy(new_pass)

# ----------------------------Add Password to file-------------------------------
def save():
    domain_txt = domain.get()
    email_txt = email.get()
    password_txt = password.get()
    new_data = {
        domain_txt: {
            "Email": email_txt,
            "Password": password_txt,
        }}

    if len(domain_txt) == 0 or len(email_txt) == 0 or len(password_txt) == 0:
        messagebox.showinfo(title="Empty Fields", message="Do not leave anything empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm to save", message="Do you want to save the details?")
        if is_ok:
            try:
                with open("data.json", 'r') as save_file:
                    data = json.load(save_file)
            except FileNotFoundError:
                with open("data.json", 'w') as save_file:
                    json.dump(new_data, save_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as save_file:
                    json.dump(data, save_file, indent=4)
            finally:
                domain.delete(0, 'end')
                email.delete(0, 'end')
                password.delete(0, 'end')
                domain.focus()

# ---------------------------------------Search Domain in File-----------------------------
def search():
    domain_txt = domain.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not Found", message="Data File does not exists")
    else:
        if domain_txt in data:
            messagebox.showinfo(title=f"{domain_txt}", message=f"Email :{data[domain_txt]['Email']} \n"
                                                               f"Password :{data[domain_txt]['Password']}")
        else:
            messagebox.showinfo(title="Details not present", message=f"Details for {domain_txt} does not exist")

# -----------------------------------UI Setup---------------------------------------
COLOR = "#FFFFFF"
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=COLOR)

canvas = Canvas(width=200, height=200, bg=COLOR, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
domain = Label(text="Domain", bg=COLOR, pady=5)
domain.grid(row=1)
email = Label(text="Email/Username ", bg=COLOR, pady=5)
email.grid(row=2)
password = Label(text="Password ", bg=COLOR, pady=10)
password.grid(row=3)

# Entries and Buttons
domain = Entry(width=33)
domain.focus()
domain.grid(column=1, row=1)
search_btn = Button(text="Search", bg=COLOR, padx=30, command=search)
search_btn.grid(column=2, row=1)
email = Entry(width=52)
email.grid(column=1, row=2, columnspan=2)
password = Entry(width=33)
password.grid(column=1, row=3)
pass_gen = Button(text="Generate Password", bg=COLOR, command=gen_pass)
pass_gen.grid(column=2, row=3)
add = Button(text="Add", width=44, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
