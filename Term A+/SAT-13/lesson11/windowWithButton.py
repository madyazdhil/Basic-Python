import tkinter
import random

#creating a window
jendela = tkinter.Tk()
jendela.geometry("400x550")
jendela.title("WIndow with Buttons")

#function to act when button 2 is clicked
def showtext():
    movie = ["Frozen 2", "GotG 3", "Cats","Ariel"]
    c = random.choice(movie)
    lb2.config(text= f"You already watch {c}")

#widget = anything inside window
#-- Labels
lb1 = tkinter.Label(jendela, text="Berikut merupakan contoh tombol", bg="SkyBlue" , font=("calibri, 15"))
lb2 = tkinter.Label(jendela)

#--Buttons
button1 = tkinter.Button(jendela, text="Button 1", bg="LavenderBlush")
# buttons with command
button2 = tkinter.Button(jendela,
                         text="Click me!",
                         bg="Salmon",
                         command=showtext
                         )



#placement = .pack()
lb1.pack(ipady=15 , pady=15 , fill=tkinter.X)
button1.pack(pady=15 , side= tkinter.LEFT)
button2.pack(pady=(0,15), side=tkinter.RIGHT)
lb2.pack(side=tkinter.TOP)

jendela.mainloop()
