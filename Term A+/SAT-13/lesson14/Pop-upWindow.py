import tkinter as tk

#first and main window
jendela = tk.Tk()
jendela.title("Main Action")
jendela.geometry("300x200")

#functions
def showpopup():
    jendelaTambah.deiconify()

#widgets / window 1
label1 = tk.Label(jendela, text="This is the main Action window")
btn1 = tk.Button(jendela, text="Click me to show another window", command=showpopup)
#placement / window 1
label1.pack()
btn1.pack()



#Second window
jendelaTambah = tk.Toplevel(jendela)
jendelaTambah.title("COmplementary window")
jendelaTambah.geometry("350x350")

#functions
def closepopup():
    jendelaTambah.withdraw()

def destroypopup():
    jendelaTambah.destroy()

#widgets for second window
label2 = tk.Label(jendelaTambah, text="Another copy of the original")
btn2 = tk.Button(jendelaTambah, text="Click me to close", command=closepopup)
btn3 = tk.Button(jendelaTambah, text="Click me to close and never able to open again", command=destroypopup)


#placement of second window
label2.pack()
btn2.pack()
btn3.pack()

jendelaTambah.withdraw()
jendela.mainloop()