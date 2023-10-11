import tkinter

jendela = tkinter.Tk()
jendela.geometry("300x400")
jendela.title("Radio Buttons!!")

#functions
def printgender():
    g = gender.get()
    print(f"The choosen gender is {g}")
    lbl2.config( text=f"The choosen gender is {g}", font=("Calimbri",15))

#widgets
lbl1 = tkinter.Label(jendela, text="Choose your Gender", font=("Calimbri",21), foreground="Blue")
lbl2 = tkinter.Label(jendela)

gender = tkinter.StringVar()
gender.set(" ")
radio1 = tkinter.Radiobutton(jendela, text= "Male", value="Male" , variable=gender , command=printgender)
radio2 = tkinter.Radiobutton(jendela, text= "Female" ,value="Female", variable=gender, command=printgender)

#placements
lbl1.pack(pady=(20,5))
radio1.pack()
radio2.pack()
lbl2.pack(pady=15)

jendela.mainloop()