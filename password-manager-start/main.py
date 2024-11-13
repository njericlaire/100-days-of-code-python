from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def find_password():
    web_value=web_entry.get()
    try:

        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found" )
    else:
        if web_value in data:
            messagebox.showinfo(title=web_value,message=f"Your password is {data[web_value]["password"]}\n Your email is {data[web_value]["email"]}")
        else:
            messagebox.showinfo(title="Error", message="No details of the website were found")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    pass_word = ""
    for char in password_list:
      pass_word += char

    pass_entry.insert(0,pass_word)
    pyperclip.copy(pass_word)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_value=web_entry.get()
    name_value=name_entry.get()
    pass_value=pass_entry.get()

    new_data={website_value:{
        "email":name_value,
        "password":pass_value,
    }}

    if len(website_value)==0 or len(name_value)==0 or len(pass_value)==0:
        messagebox.showwarning(title="Warning",message="Please fill in all the fields")
    else:
        is_ok=messagebox.askokcancel(title=website_value,message=f"These are the details entered: \nEmail: {name_value} \nWebsite: {website_value} \nPassword:{pass_value}\nIs it okay to save? ")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                data = {}

                # Update the data dictionary with new_data
            data.update(new_data)

            # Write the updated data back to the file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            web_entry.delete(0,'end')

            pass_entry.delete(0,'end')




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, )

generate = Button(text="Generate Password",width=14,command=generate_password )
generate.grid(row=3,column=2)

search = Button(text="Search",width=14,command=find_password )
search.grid(row=1,column=2)

add = Button(text="Add", width=36,command=save_password)
add.grid(row=4,column=1,columnspan=2)

website= Label(text="Website",)
website.grid(row=1,column=0)

name= Label(text="Email/Username",)
name.grid(row=2,column=0)

web_entry = Entry(width=18)
web_entry.focus()
web_entry.grid(row=1,column=1,)

name_entry = Entry(width=35)
name_entry.insert(0,"clairemwas20@gmail.com")
name_entry.grid(row=2,column=1,columnspan=2)

pass_entry = Entry(width=18)
pass_entry.grid(row=3,column=1,)

password= Label(text="Password",)
password.grid(row=3,column=0)

canvas=Canvas(width=200, height=224,  )
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

window.mainloop()