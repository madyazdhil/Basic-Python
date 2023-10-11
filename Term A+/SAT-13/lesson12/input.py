import tkinter as tk

#creating window
jendela = tk.Tk()
jendela.geometry("400x500")
jendela.title("Creating Entry")



#functions
def et1():
    entry1.focus()

def et2():
    entry2.focus()

def saveName():
    name = entry1.get()
    lb4.config(text=f"Nama {name} telah disimpan ke database kami")

def getpdd():
    pdd = rdsave.get()
    lb6.config(text=f"Kamu adalah lulusan {pdd}")

rdsave = tk.StringVar()
rdsave.set(" ")

#widget
lb1 = tk.Label(jendela, text="Entry Forms",
               font=("Times New Roman", 23),
               bg="Wheat")
lb2 = tk.Label(jendela, text="Insert your name")
lb3 = tk.Label(jendela, text="Insert your age")
lb4 = tk.Label(jendela)
lb5 = tk.Label(jendela, text="Insert your last education")
lb6 = tk.Label(jendela)

#entry
entry1 = tk.Entry(jendela, width=35)
entry2 = tk.Entry(jendela, width=35)

#spinner
spinner1 = tk.Spinbox(jendela, from_=15, to=21, state="readonly")

#radio button
radio1 = tk.Radiobutton(jendela, text="SD" , variable= rdsave, value="SD",command=getpdd)
radio2 = tk.Radiobutton(jendela, text="SMP" , variable= rdsave, value="SMP",command=getpdd)
radio3 = tk.Radiobutton(jendela, text="SMA / SMK" , variable= rdsave, value="SMA / SMK",command=getpdd)


#button
btn1 = tk.Button(jendela, text="Edit Your name",command=et1)
btn2 = tk.Button(jendela, text="Edit Your age", command=et2)
btn3 = tk.Button(jendela, text="Save Your name", command=saveName)


#placement
lb1.pack(ipadx=15,ipady=20,pady=17)
lb2.pack(pady=(0,12))
entry1.pack()
lb3.pack(pady=12)
spinner1.pack()
lb5.pack(pady=12)
radio1.pack()
radio2.pack()
radio3.pack()
lb6.pack()
btn1.pack(pady=12)
btn2.pack()
btn3.pack(pady=12)
lb4.pack()


#repeating calling the window
jendela.mainloop()