from tkinter import *
from tkinter import messagebox
from random import  randint, shuffle , choice
import pyperclip


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letter= [choice(letters) for _ in range(randint(8,10))]
    password_number= [choice(numbers) for _ in range(randint(2,4))]
    password_symbol= [choice(symbols) for _ in range (randint(2,4))]

    password_list= password_letter+password_number+password_symbol

    password= "".join(password_list)

    shuffle(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)








def save():
    website= web_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    is_ok=messagebox.askokcancel(title=website, message=f" its your mail id {email}\n want "
                                                     f"to save password {password}\n")

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="OOps", message=" Do not leave blank the fields")
    else:



        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)





window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)
label_web=Label(text="website")
label_web.grid(column=0, row=1)
web_entry=Entry(width=35)
web_entry.grid(column=1,row=1, columnspan=2)
web_entry.focus()
label_email=Label(text="Email/Username")
label_email.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "uvyneetprep@gmail.com")
button_genrate_pd=Button(text="Generate Password", command=generate_password)
button_genrate_pd.grid(column=3,row=2)
label_password=Label(text="Password")
label_password.grid(column=0, row=3)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)
add_button=Button(text="add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
