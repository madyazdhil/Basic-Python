import tkinter as tk

window = tk.Tk()
window.title("Have buttons")
window.geometry("400x400")

#widget
lb1 = tk.Label(window, text="Who are you", font=("Times New Roman",21), background="Salmon")

btn1 = tk.Button(window, text="Click me")
btn2 = tk.Button(window, text="Choose me", background="LightPink")

#placement
lb1.pack(pady=15)
btn1.pack()
btn2.pack()

window.mainloop()