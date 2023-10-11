import tkinter

jendela = tkinter.Tk()
jendela.geometry("300x400")
jendela.title("Radio Buttons!!")

#widgets
lbl1 = tkinter.Label(jendela, text="Choose your Gender", font=("Calimbri",21), foreground="Blue")

gender = tkinter.StringVar()
gender.set(" ")
radio1 = tkinter.Radiobutton(jendela, text= "Male", value="male" , variable=gender)
radio2 = tkinter.Radiobutton(jendela, text= "Female" ,value="Female", variable=gender)

#placements
lbl1.pack(pady=(20,5))
radio1.pack()
radio2.pack()

jendela.mainloop()