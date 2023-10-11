import tkinter

window = tkinter.Tk()
window.title("Placement pack")
window.geometry("500x450")

#widgets
label1 = tkinter.Label(window, text="Hello World", font=("Calibri", 25))
label2 = tkinter.Label(window, text="This is me", font=("Cambria",20))
label3 = tkinter.Label(window, text="I hope you enjoy it here", font=("Cambria",15))
label4 = tkinter.Label(window, text="Wish to see you later", font=("Cambria",9))

#placements
label1.pack(pady=(12,7))
label2.pack()
label3.pack(pady=(15,20))
label4.pack()

window.mainloop()