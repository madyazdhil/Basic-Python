import tkinter as tk

#saving the window config to a variable
jendela = tk.Tk()
jendela.title("Review Lesson")
jendela.geometry("400x400")

#functions
def ambil_kata():
    label2.config(text="You have choosen me")

#widgets = anything iside the window
label1 = tk.Label(jendela,
                  text="Review",
                  font=("Arial",20) )
label2 = tk.Label(jendela,text="")

button1 = tk.Button(jendela,
                    text="Click Me!",
                    background="CornflowerBlue",
                    command=ambil_kata)

#placement = the hirarcy of the placement
label1.pack(pady=(15,0))
button1.pack(ipady=5, ipadx=10, pady=10)
label2.pack()


jendela.mainloop()
