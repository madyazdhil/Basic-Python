import tkinter
import tkinter.messagebox as msgbox

jendela = tkinter.Tk()
jendela.title("My Calculator")
jendela.geometry("250x300")

expression = ""

#functions
#1. adding numbers into an entry
def insert_number(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)

def clearBt():
    global expression
    #deletes whatever inside the variable
    expression= ""
    #deletes the text appeared in the entry box
    input_text.set("")

def resultCal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
    except:
        msgbox.showerror("Empty Field", "Please Insert the number first!")



input_text = tkinter.StringVar()
#Widgets
entry = tkinter.Entry(jendela,
                      width=18,
                      borderwidth=5,
                      font=("Arial",18),
                      state="readonly",
                      justify="right",
                      textvariable=input_text)

button1 = tkinter.Button(jendela, text="1", pady=20, padx=20, command= lambda : insert_number(1))
button2 = tkinter.Button(jendela, text="2", pady=20, padx=20, command= lambda : insert_number(2))
button3 = tkinter.Button(jendela, text="3", pady=20, padx=20, command= lambda : insert_number(3))
button4 = tkinter.Button(jendela, text="4", pady=20, padx=20, command= lambda : insert_number(4))
button5 = tkinter.Button(jendela, text="5", pady=20, padx=20, command= lambda : insert_number(5))
button6 = tkinter.Button(jendela, text="6", pady=20, padx=20, command= lambda : insert_number(6))
button7 = tkinter.Button(jendela, text="7", pady=20, padx=20, command= lambda : insert_number(7))
button8 = tkinter.Button(jendela, text="8", pady=20, padx=20, command= lambda : insert_number(8))
button9 = tkinter.Button(jendela, text="9", pady=20, padx=20, command= lambda : insert_number(9))
button0 = tkinter.Button(jendela, text="0", pady=20, padx=20, command= lambda : insert_number(0))


addition = tkinter.Button(jendela, text="+", pady=20, padx=19.5,command= lambda : insert_number("+"))
substract = tkinter.Button(jendela, text="-", pady=20, padx=20.5,command= lambda : insert_number("-"))
multi = tkinter.Button(jendela, text="x", pady=20, padx=20,command= lambda : insert_number("*"))
div = tkinter.Button(jendela, text="/", pady=20, padx=20,command= lambda : insert_number("/"))

result = tkinter.Button(jendela, text="=", pady=20, padx=20 ,command=resultCal)
clear = tkinter.Button(jendela, text="CE", pady=20, padx=19, command=clearBt)


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