import tkinter as tk
import requests

window = tk.Tk()
window.title("Link Shortner (my version)")
window.geometry("400x250")

#functions
def shortenLink():
    API_KEY = 'c258a81323e9cbf4d4dd950cc3e057d4306aa'
    BASE_URL = 'https://cutt.ly/api/api.php'
    link = etr1.get()
    name = etr2.get()
    payload = {'key': API_KEY, 'short':link, 'name': name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        lb4.config(text=f"Your shortened link is {short_link}")

        print(f"Title = {title}")
        print(f"link = {short_link}")
    except:
        status = data['url']['status']
        print(f" You have an error. Status of error is {status}")

#widgets
lb1 = tk.Label(window, text=" Link Shortner")
lb2 = tk.Label(window, text="Insert full link")
lb3 = tk.Label(window, text="what do you want to short it into")
lb4 = tk.Label(window)

etr1 = tk.Entry(window, width=45)
etr2 = tk.Entry(window, width=45)

btn1 = tk.Button(window,text="Generate Link", command=shortenLink)

#placements
lb1.pack(pady=20)
lb2.pack(pady=(0,12))
etr1.pack()
lb3.pack(pady=12)
etr2.pack()
btn1.pack(pady=12)

window.mainloop()