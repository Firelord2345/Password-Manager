from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # pass_length=int(input("whats the length of the password?"))
    letter_length=random.randint(8,10)
    sys=random.randint(2,4)
    num=random.randint(2,14)

    password=[]
    pass1=""
    password_letters=[random.choice(letters) for _ in range(letter_length)]
    password_symbols=[random.choice(symbols) for _ in range(sys) ]
    password_numbers=[random.choice(numbers) for _ in range(num) ]
    password=password_letters+password_symbols+password_numbers
    random.shuffle(password)
    pass1="".join(password)
    password_entry.insert(0,pass1)
    pyperclip.copy(pass1)
# ---------------------------- Find the website ------------------------------- #
def find():
    website=web_entry.get()
    email= email_entry.get()
    password=password_entry.get()
    try:
    # Try to open and load the data.json file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # If the file is not found, handle the exception
         messagebox.showwarning(message="No data file found")
    else:
        # Check if the website exists in the loaded data
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Website Found", message=f"Email: {email}\nPassword: {password}")
        else:
            # If the website is not found in the data
            messagebox.showinfo(title="Website Not Found", message="No details for the website exist.")

    
    
            
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    enweb=web_entry.get()
    enmai=email_entry.get()
    enpass=password_entry.get()
    new_data={
        enweb:{
            "email":enmai,
            "password":enpass
        }
    }
    
    if len(enweb)!=0 and len(enmai)!=0:
     is_ok=messagebox.askokcancel(title="website",message=f"{enweb}\n{enmai}\n{enpass}")
     if is_ok:
    #   with open("data.txt","a") as file:
    #    file.write(f"{enweb}|{enmai}|{enpass}\n") 
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
        
            web_entry.delete(0,END)
            password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="OOps",message="Please Fill")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button

# Create the main window
window = Tk()

# Set padding for the entire window
window.config(padx=20, pady=20)

# Create a canvas to display an image
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, columnspan=2)  # Span the image across two columns

# Add a label and entry for 'Website'
web = Label(text="Website")
web.grid(column=0, row=1)
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()
search=Button(text="Search",command=find)
search.grid(column=3, row=1)

# Add a label and entry for 'Email/Username'
email = Label(text="Email/Username")
email.grid(column=0, row=2)
email_entry = Entry(width=21)
email_entry.insert(0,"joel@.com")
email_entry.grid(column=1, row=2)

# Add a label and entry for 'Password'
password = Label(text="Password")
password.grid(column=0, row=3 )
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Add 'Generate Password' button next to the password entry
generate = Button(text="Generate Password",command=passgen)
generate.grid(column=3, row=3)

# Add 'Add' button, spanning two columns
add = Button(text="Add", width=36,command=save)
add.grid(column=1, row=4, columnspan=2)

# Run the application
window.mainloop()
