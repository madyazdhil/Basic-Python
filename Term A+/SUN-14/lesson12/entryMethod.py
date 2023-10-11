import tkinter

jendela = tkinter.Tk()
jendela.geometry("400x500")
jendela.title("Entry Method")

#function
def focus1():
    input1.focus()

def focus2():
    input2.focus()

def erase1():
    input1.delete(0, tkinter.END)

def erase2():
    input2.delete(0, tkinter.END)


#widgets
input1 = tkinter.Entry(jendela, width=30)
input2 = tkinter.Entry(jendela, width=30)

btn1 = tkinter.Button(jendela, text="Focus Input 1", command=focus1)
btn2 = tkinter.Button(jendela, text="Focus Input 2", command=focus2)
btn3 = tkinter.Button(jendela, text="Erase input 1", command=erase1)
btn4 = tkinter.Button(jendela, text="Erase input 2", command=erase2)

#placement
input1.pack(pady=(20,5))
input2.pack(pady=5)
btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)




jendela.mainloop()