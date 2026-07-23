from tkinter import Tk,Button,Entry,Label,messagebox,Canvas,PhotoImage,END
from PIL import Image, ImageTk
from random import choice, shuffle, randint
from cryptography.fernet import Fernet
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import os

#-----------functions------------------------
def load_key():
     if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
     else:
       with open("secret.key", "rb") as key_file:
        return key_file.read()

fernet = Fernet(load_key())

def add():
    web=webEntry.get().strip()
    username=usernameEntry.get().strip()
    password=passwordEntry.get().strip()
    
    if not web or not username or not password :
        messagebox.showerror(title="⚠️Oops", message="Please make sure you haven't left any fields empty.")
    else:
         infos = messagebox.askokcancel(title="website", message=f"These are the details entered: \nUsername: {username} "
                                                      f"\nPassword: {password} \nDo you wnt to save ?")
         if infos:
            encrypted_password = fernet.encrypt(password.encode()).decode()
            with open("passwordManager.txt", "a") as data_file:
                data_file.write(f"-> website: {web} |-> Email: {username} |-> Password(encrypted): {encrypted_password}\n")
            webEntry.delete(0, END)
            usernameEntry.delete(0,END)
            passwordEntry.delete(0, END)
            messagebox.showinfo(title="success!",message="data added successfully >⩊<!")
def generate_password():
    letters = list(ascii_uppercase)+list(ascii_lowercase)
    symbols = list(punctuation)
    numbers = list(digits)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password = password_letters + password_symbols + password_numbers
    shuffle(password)
    
    generatedPassword = "".join(password)

    if  password:
        passwordEntry.delete(0,END)
        passwordEntry.insert(0, generatedPassword)

#------------------------UI---------------------------------
root = Tk()
root.geometry('600x390')
root.resizable(False,False)
root.config(bg="black")
root.title("Password Manager")

#logo
logo = Image.open("logo.png")
logo = logo.resize((200, 200), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
logo_label = Label(root, image=logo,bg="black")
logo_label.grid(row=0,column=1)

#labels
web_label = Label(root,text="🌐Website   :",bg="black",fg="white",font=("sans",18,))
web_label.grid(row=1, column=0)
username_label = Label(root,text="👤Username:",bg="black",fg="white",font=("sans",18))
username_label.grid(row=2, column=0)
password_label=Label(root,text="🔐Password:",bg="black",fg="white",font=("sans",18))
password_label.grid(row=3,column=0)
#entry
webEntry = Entry(root, width=35,bg="white",font=(15))
webEntry.grid(row=1, column=1)
usernameEntry = Entry(root, width=35,bg="white",font=(15))
usernameEntry.grid(row=2, column=1)
passwordEntry = Entry(root, width=34,bg="white",font=(15))
passwordEntry.grid(row=3,column=1)

#buttons
generate_password_button = Button(text="Generate Password",command=generate_password,bg="white",fg="black")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=add,bg="green",fg="white")
add_button.grid(row=4, column=1)

passwordEntry.bind("<Return>", lambda event:add)
root.mainloop()