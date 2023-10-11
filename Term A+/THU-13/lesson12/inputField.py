import tkinter as tk

window = tk.Tk()
window.geometry("300x400")
window.title("Student Entry")

#functions
def getText():
    name = ipt1.get()
    age = ipt2.get()
    lb3.config(text=f"data of = {name} and age {age}\n Has been saved",
               font=("Times New Roman",10))


#widgets
lb1 = tk.Label(window,
               text="Insert your name",
               font=("Times New Roman",15)
               )
lb2 = tk.Label(window,
               text="Insert your Age",
               font=("Times New Roman",15)
               )
lb3 = tk.Label(window)

ipt1 = tk.Entry(window, width=35)
ipt2 = tk.Entry(window, width=35)

btn1 = tk.Button(window,text="Save", background="Lavender")

#placement
lb1.pack(pady=10)
ipt1.pack()
lb2.pack(pady=10)
ipt2.pack()
btn1.pack(pady=10, ipady=8, ipadx=16)
lb3.pack()

window.mainloop()