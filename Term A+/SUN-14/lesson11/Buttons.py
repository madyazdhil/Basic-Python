import tkinter

window = tkinter.Tk()
window.title("Label with button")
window.geometry("500x550")

click = 0

#functions
def showText():
    global click
    click += 1
    label2.config(text=f"You have clicked a button for {click} times",font=("Cambria",12))
    button1.config(text="Thank you")



#widgets
#--Label
lable1 = tkinter.Label(window, text="Below, is a button", font=("Cambria",20),background="Salmon")
label2 = tkinter.Label(window)

#--Buttons
button1 = tkinter.Button(window, text="Click me",
                         background="LightSalmon",
                         font=("Arial",12),
                         command=showText)


#placements
lable1.pack(pady=(20,12), ipady=12, ipadx=20)
button1.pack(ipadx=16, ipady=10)
label2.pack()

window.mainloop()