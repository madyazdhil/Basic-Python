import tkinter

window = tkinter.Tk()
window.title("Placement pack")
window.geometry("500x450")

#widgets
label1 = tkinter.Label(window, text="Hello World", font=("Calibri", 25), foreground="RoyalBlue", background="Salmon")
label2 = tkinter.Label(window, text="This is me", font=("Cambria",10), foreground="Salmon")
label3 = tkinter.Label(window, text="I hope you enjoy it here", font=("Cambria",10),foreground="Blue")
label4 = tkinter.Label(window, text="Wish to see you later", font=("Cambria",10),foreground="Plum")

#placements with grid
label1.grid(column=0, row=0)
label2.grid(column=0, row=1)
label3.grid(column=1, row=1)
label4.grid(column=2, row=1)

window.mainloop()