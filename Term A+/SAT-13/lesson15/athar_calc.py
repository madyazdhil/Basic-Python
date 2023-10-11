import tkinter
import tkinter.messagebox as mg

jendela = tkinter.Tk()
jendela.title("My Calculator")
jendela.geometry("250x300")

expression = ""

#functions
def insertingNumber(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)

def clearAll():
    global expression
    expression=""
    input_text.set("")

def Calculate():
    try:
        global expression
        result = eval(expression)
        input_text.set(result)
    except:
        mg.showerror("Missing Instruction","Please add another number or operation")


input_text = tkinter.StringVar()
#Widgets
entry = tkinter.Entry(jendela,
                      width=18,
                      borderwidth=5,
                      font=("Arial",18),
                      state="readonly",
                      justify="right",
                      textvariable=input_text)

button1 = tkinter.Button(jendela, text="1", pady=20, padx=20,command=lambda : insertingNumber(1))
button2 = tkinter.Button(jendela, text="2", pady=20, padx=20,command=lambda : insertingNumber(2))
button3 = tkinter.Button(jendela, text="3", pady=20, padx=20,command=lambda : insertingNumber(3))
button4 = tkinter.Button(jendela, text="4", pady=20, padx=20,command=lambda : insertingNumber(4))
button5 = tkinter.Button(jendela, text="5", pady=20, padx=20,command=lambda : insertingNumber(5))
button6 = tkinter.Button(jendela, text="6", pady=20, padx=20,command=lambda : insertingNumber(6))
button7 = tkinter.Button(jendela, text="7", pady=20, padx=20,command=lambda : insertingNumber(7))
button8 = tkinter.Button(jendela, text="8", pady=20, padx=20,command=lambda : insertingNumber(8))
button9 = tkinter.Button(jendela, text="9", pady=20, padx=20,command=lambda : insertingNumber(9))
button0 = tkinter.Button(jendela, text="0", pady=20, padx=20,command=lambda : insertingNumber(0))


addition = tkinter.Button(jendela, text="+", pady=20, padx=19.5,command=lambda : insertingNumber("+"))
substract = tkinter.Button(jendela, text="-", pady=20, padx=20.5,command=lambda : insertingNumber("-"))
multi = tkinter.Button(jendela, text="x", pady=20, padx=20,command=lambda : insertingNumber("*"))
div = tkinter.Button(jendela, text="/", pady=20, padx=20,command=lambda : insertingNumber("/"))

result = tkinter.Button(jendela, text="=", pady=20, padx=20 ,command=Calculate)
clear = tkinter.Button(jendela, text="CE", pady=20, padx=19,command=clearAll)


#placements
#row1
entry.grid(row=0, column=0,columnspan=4)

#row2
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
addition.grid(row=1, column=3)

#row3
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
substract.grid(row=2, column=3)

#row4
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multi.grid(row=3, column=3)

#row5
clear.grid(row=4, column=0)
button0.grid(row=4, column=1)
result.grid(row=4,column=2)
div.grid(row=4, column=3)

jendela.mainloop()