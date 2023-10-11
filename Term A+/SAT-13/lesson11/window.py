import tkinter

window = tkinter.Tk()
window.geometry("300x400")
window.title("My first Window")

#widgets
#adding a label
label1 = tkinter.Label(window, text="My first label")
label2 = tkinter.Label(window, text="My second label",background="DarkOrchid",foreground="White")

#adding a button
btn1 = tkinter.Button(window, text="Click me",background="MidnightBlue",foreground="White")


#placement
label1.pack(pady=20)
label2.pack(pady=(5,10),ipadx=8,ipady=16)
btn1.pack()

# label1.grid(row=0, column=0, padx=15)
# label2.grid(row=0, column=1, padx=15)



window.mainloop()