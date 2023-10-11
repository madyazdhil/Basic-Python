import tkinter

window = tkinter.Tk()
window.title("Label with button")
window.geometry("500x550")

#functios
def showText():
    lable2.config(text="Im the suprise", background="LightBlue", font=("Arial",20))


#widgets
#--Label
lable1 = tkinter.Label(window, text="Below, is a button with a suprise", font=("Cambria",20),background="Salmon")
lable2 = tkinter.Label(window, text="")

#--Buttons
button1 = tkinter.Button(window, text="Suprise after click", background="LightSalmon", font=("Arial",12),
command=showText)


#placements
lable1.pack(pady=(20,12), ipady=12, ipadx=20)
button1.pack(ipadx=16, ipady=10)
lable2.pack(pady=15)


window.mainloop()