import tkinter

jendela = tkinter.Tk()
jendela.geometry("300x400")
jendela.title("Spinner Input!!")

#functions


#widgets
lbl1 = tkinter.Label(jendela, text="Input your Grade", font=("",15))
lbl2 = tkinter.Label(jendela, text="Input your Age", font=("",15))
lbl3 = tkinter.Label(jendela, text="Input your Teacher", font=("",15))

spinner1 = tkinter.Spinbox(jendela, from_=1, to=12, width=15)
spinner2 = tkinter.Spinbox(jendela, values=(10,12,13,15,17), width=15 , state="readonly")
spinner3 = tkinter.Spinbox(jendela, values=("mr. Ahmad", "Mr.Eko"), width=15)


#placement
lbl1.pack(pady=(20,6))
spinner1.pack(pady=6)
lbl2.pack(pady=6)
spinner2.pack(pady=6)
lbl3.pack(pady=6)
spinner3.pack(pady=6)

jendela.mainloop()