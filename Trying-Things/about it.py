# we neet to call the module to create a window
# tkinter
import tkinter
import random

f = ["Ayam", "Kambing" , "Sapi" , "domba", "Kucing", "Kuda", "Capybara"]
rd = random.choice(f)
# SAVE THE module to create window inside a variable called "window"

jendela = tkinter.Tk()

# create the size of the window

jendela.geometry("500x400")

# create a title for the window
jendela.title("Creating my first window")
c = 0

def berapakali():
    global c
    rd = random.choice(f)
    c+=1
    label2.config(text=f"ada klik ke {c}")
    button2.config(text= f"{rd}")

def gettext():
    words = entry1.get()
    label3.config(text=words)





# label with different font

label1 = tkinter.Label(jendela, text="Random and get a text",
                       font="Comic",
                       foreground="CornflowerBlue",
                       background="DarkSlateBlue")
label2 = tkinter.Label(jendela)
label3 = tkinter.Label(jendela)
label4 = tkinter.Label(jendela, text= "Enjoy the drinks")
entry1 = tkinter.Entry(jendela, width=35)
button1 = tkinter.Button(jendela, text="Save the Text" , font="Calibri" , bg="Chocolate", command=gettext)
button2 = tkinter.Button(jendela, text="click me" , font="Calibri" , bg="Chocolate",
                         command=berapakali)



# placement

label1.pack(pady=(20,15))
#
#
# label4.pack()

entry1.pack(pady=(0,15))
button1.pack(pady=(0,15))
button2.pack(pady=(0,15))
label2.pack(pady=(0,15))
label3.pack()

# making the window continously appered --> put in he bottom of the code
jendela.mainloop()