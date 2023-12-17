import tkinter

window = tkinter.Tk()
window.geometry("500x500")
window.title("My button works!")

#functions
def ubahLabel():
    lb2.config(text="Yes, Im changed",background="Salmon")

#widgets
lb1 = tkinter.Label(window, text="This is a label")
lb2 = tkinter.Label(window, text="WIll I changed?")
btn1 = tkinter.Button(window, text="Click me!", command=ubahLabel)

#placements
lb1.pack(pady = 15)
lb2.pack()
btn1.pack(pady=15)

window.mainloop()