import tkinter

jendela = tkinter.Tk()
jendela.geometry("400x300")
jendela.title("Input Field")

#functions
def savename():
    name = input1.get()
    age = input2.get()
    label3.config( text=f"Your name is {name} and your age is {age}", font=("Calimbri",10))

#widgets
label1 = tkinter.Label(jendela, text="Input your name", font=("Calimbri",15))
label2 = tkinter.Label(jendela, text="Input your age", font=("Calimbri",15))
label3 = tkinter.Label(jendela)

input1 = tkinter.Entry(jendela,width=35)
input2 = tkinter.Entry(jendela,width=35)

btn1 = tkinter.Button(jendela, text="Save", command=savename)

#placement
label1.pack(pady=(20,10))
input1.pack()
label2.pack(pady=(20,10))
input2.pack()
btn1.pack()
label3.pack()

jendela.mainloop()