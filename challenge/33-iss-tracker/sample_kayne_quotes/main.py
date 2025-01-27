import requests
from tkinter import *


def get_quote():
    request_url = "https://api.kanye.rest/"
    api_response = requests.get(request_url)
    if api_response.status_code == 200:
        canvas.itemconfig(quote_text,text=str(api_response.json()["quote"]))
    else:
        raise Exception(f"An error occurred receiving data. Status code: {api_response.status_code}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()