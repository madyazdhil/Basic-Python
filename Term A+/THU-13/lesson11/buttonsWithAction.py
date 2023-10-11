import tkinter as tk

window = tk.Tk()
window.title("Have buttons")
window.geometry("400x400")

#fuctions
def showText():
    lb2.config(text="Thanks for clicking me!!!", background="Yellow")


#widget
lb1 = tk.Label(window, text="Who are you", font=("Times New Roman",21), background="Salmon")
lb2 = tk.Label(window)

btn1 = tk.Button(window, text="Click me")
btn2 = tk.Button(window, text="Choose me", background="LightPink",
                 command=showText)

#placement
lb1.pack(pady=15)
btn1.pack()
btn2.pack(pady=6)
lb2.pack()

window.mainloop()