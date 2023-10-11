import tkinter

window = tkinter.Tk()
window.geometry("228x286")
window.title("Calculator")

#functions
expression = ""

def insert_number(num):
    global expression
    expression = expression + str(num)
    input_text.set(expression)

def clearAll():
    global expression
    expression =""
    input_text.set("")

def FinalResult():
    global expression
    equation = str(eval(expression))
    input_text.set(equation)



#widgets

input_text = tkinter.StringVar()
ent1= tkinter.Entry(window, width=35, borderwidth=10, textvariable=input_text)

btn_1 = tkinter.Button(window, text="1", pady=20, padx=21,command=lambda :insert_number(1))
btn_2 = tkinter.Button(window, text="2", pady=20, padx=20,command=lambda :insert_number(2))
btn_3 = tkinter.Button(window, text="3", pady=20, padx=20,command=lambda :insert_number(3))
btn_4 = tkinter.Button(window, text="4", pady=20, padx=21,command=lambda :insert_number(4))
btn_5 = tkinter.Button(window, text="5", pady=20, padx=20,command=lambda :insert_number(5))
btn_6 = tkinter.Button(window, text="6", pady=20, padx=20,command=lambda :insert_number(6))
btn_7 = tkinter.Button(window, text="7", pady=20, padx=21,command=lambda :insert_number(7))
btn_8 = tkinter.Button(window, text="8", pady=20, padx=20,command=lambda :insert_number(8))
btn_9 = tkinter.Button(window, text="9", pady=20, padx=20,command=lambda :insert_number(9))
btn_0 = tkinter.Button(window, text="0", pady=20, padx=20,command=lambda :insert_number(0))

btn_additon = tkinter.Button(window, text="+", pady=20, padx=18,command=lambda :insert_number("+"))
btn_substraction = tkinter.Button(window, text="-", pady=20, padx=20,command=lambda :insert_number("-"))
btn_multipication = tkinter.Button(window, text="x", pady=20, padx=20,command=lambda :insert_number("*"))
btn_division = tkinter.Button(window, text=":", pady=20, padx=20,command=lambda :insert_number("/"))

btn_result = tkinter.Button(window, text="=", pady=20, padx=20,command=FinalResult)
btn_clear = tkinter.Button(window, text="CE", pady=20, padx=18, command=clearAll)


#placements

ent1.grid(row=0,column=0,columnspan=5)

btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_additon.grid(row=1, column=3)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_substraction.grid(row=2,column=3)

btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)
btn_multipication.grid(row=3,column=3)

btn_clear.grid(row=4,column=0)
btn_0.grid(row=4,column=1)
btn_result.grid(row=4,column=2)
btn_division.grid(row=4,column=3)

window.mainloop()