import requests
import tkinter as tk
import pyperclip

window = tk.Tk()
window.geometry("400x300")
window.title("Link SHortener")

#functions
def shorten_link():
    API_KEY = '50ff34b9497a8111838783f91b8fb254130e3'
    BASE_URL = 'https://cutt.ly/api/api.php'

    link_input = EntInst.get()
    name_input = EntName.get()

    #variable to store the parameters
    payload = {'key': API_KEY,'short':link_input, 'name': name_input }
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        #create a vara to store the title of the website
        title = data['url']['title']
        #create a var to shortening the links
        short_link = data['url']['shortLink']
        #create a var to tell us the status
        status = data['url']['status']
        print()
        print(f"Title of the website is      : {title}")
        print(f"The shortened link is        : {short_link}")
        print(f"Status of shortening the link: {status}")

        labelResult.config(text=short_link)
        pyperclip.copy(short_link)

    except:
        status=data['url']['status']
        print(f"status error is {status}")
        if status == 1:
            print("the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened")
        elif status == 2:
            print("the entered link is not a link")
        elif status == 3:
            print("	the preferred link name is already taken")
        elif status == 4:
            print("Invalid API key")
        elif status == 5:
            print("the link has not passed the validation. Includes invalid characters")
        elif status == 6:
            print("	The link provided is from a blocked domain")



#widgets
title = tk.Label(window, text= "Shorting your long link", font=("Times New Roman",20))
LbInst = tk.Label(window, text="Insert yout link")
EntInst = tk.Entry(window, width=50)
LbName = tk.Label(window, text="Insert yout link")
EntName = tk.Entry(window, width=50)

btn = tk.Button(window, text="Submit",command=shorten_link)

labelResult = tk.Label(window)


#placements:
title.pack(pady=20)
LbInst.pack()
EntInst.pack(pady=12)
LbName.pack()
EntName.pack(pady=12)
btn.pack()
labelResult.pack(pady=24)

window.mainloop()