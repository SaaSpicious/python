from tkinter import *
from tkinter import messagebox
import random
import source

PASSWORD_FILE = "passwords.txt"
MOST_USED_USERNAME = "Dennis.Klein87@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_easy=[]

    nr_letters = random.randint(8,12)
    nr_symbols = random.randint(4,6)
    nr_numbers = random.randint(4,6)

    for n in range(1,nr_letters+1):
        password_easy.append(random.choice(source.letters))

    for n in range(1,nr_symbols+1):
        password_easy.append(random.choice(source.symbols))

    for n in range(1,nr_numbers+1):
        password_easy.append(random.choice(source.numbers))

    password_easy_string=""
    for character in password_easy:
        password_easy_string+=character

    password_hard=password_easy
    random.shuffle(password_hard)

    password_hard_string=""
    for character in password_hard:
        password_hard_string+=character

    password_input.delete(0, END)
    password_input.insert(index=0, string=password_hard_string)
    return True

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Whooopsie doodle...", message="Ooops, you might've missed a few entries...")
    else:
        if ask_confirmation(website,username,password):
            write_to_file(website,username,password)


def ask_confirmation(website,username,password):
    return messagebox.askokcancel(title=website,message=f"These are the details you've entered:"
                                                 f"\nWebsite: {website}\nUsername: {username}\nPassword:{password}"
                                                 f"\nIs it okay to save?")


def write_to_file(website,username,password):
    file = open("passwords.txt","a")
    file.write(f"{website} | {username} | {password}\n")
    file.close()
    cleangui()


def cleangui():
    username_input.delete(0, END)
    username_input.insert(index=0, string=MOST_USED_USERNAME)
    website_input.delete(0,END)
    password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=1, row=1)

website_input = Entry(width=60)
website_input.grid(column=1, row=2, columnspan=2)
website_text = Label(text="Website:",font=("Arial",12,"bold"))
website_text.grid(column=0, row=2)

username_input = Entry(width=60)
username_input.grid(column=1, row=3, columnspan=2)
username_text = Label(text="Email/Username:",font=("Arial",12,"bold"))
username_text.grid(column=0, row=3)

password_input = Entry(width=40)
password_input.grid(column=1, row=4)
password_text = Label(text="Password:",font=("Arial",12,"bold"))
password_text.grid(column=0, row=4)
password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(column=2, row=4)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1, row=5, columnspan=2)

website_input.focus()
username_input.insert(index=0,string=MOST_USED_USERNAME)



window.mainloop()