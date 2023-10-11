# we neet to call the module to create a window
# tkinter
import tkinter
import random

f = ["Ayam", "Kambing" , "Sapi" , "domba", "Kucing", "Kuda", "Capybara"]
rd = random.choice(f)
# SAVE THE module to create window inside a variable called "window"

jendela = tkinter.Tk()

# create the size of the window

jendela.geometry("500x700")

# create a title for the window
jendela.title("Form update")

def focus1():
    entry1.focus()

def focus2():
    entry2.focus()


# label with different font

label1 = tkinter.Label(jendela, text="Entry Methods",
                       font="Comic",
                       foreground="CornflowerBlue",
                       background="DarkSlateBlue")

label2 = tkinter.Label(jendela, text="Insert Name")
label3 = tkinter.Label(jendela, text="Insert Age")

entry1 = tkinter.Entry(jendela, width=35)
entry2 = tkinter.Entry(jendela, width=35)

button1 = tkinter.Button(jendela, text="Edit name" , font="Calibri" , bg="Chocolate", command=focus1)
button2 = tkinter.Button(jendela, text="Edit Age" , font="Calibri" , bg="Chocolate", command=focus2)

label4 = tkinter.Label(jendela, text= "--------------------------------------")

label5 = tkinter.Label(jendela, text= "Makanan Favorite", font=("Times New Roman",20) ,bg="Salmon" )
label6 = tkinter.Label(jendela, text= "Pilih salah satu makanan favorite mu")
rdo = tkinter.Radiobutton

def getValu():
    makan = x.get()
    minum = y.get()
    if makan == " " and minum == " ":
        label7.config(text=f"\nKamu pesan dulu ya")
    elif makan == " ":
        label7.config(text=f"\nKamu pesan {minum} dan belum pesan makanan")
    elif minum == " ":
        label7.config(text=f"\nKamu pesan {makan} dan belum pesan minuman")
    else:
        label7.config(text=f"\nKamu pesan {makan} dan {minum}")

x = tkinter.StringVar()
x.set(" ")

y = tkinter.StringVar()
y.set(" ")

radio1 = rdo(jendela, text="Pizza",variable=x,value="Pizza",command=getValu)
radio2 = rdo(jendela, text="Spagetti",variable=x,value="Spagetti",command=getValu)
radio3 = rdo(jendela, text="Ayam Bakar Madu",variable=x,value="Ayam Bakar Madu",command=getValu)
label7 = tkinter.Label(jendela)





# placement

label1.pack(pady=(20,15))
#
#
#
label2.pack(pady=(0,15))
entry1.pack(pady=(0,15))

label3.pack(pady=(0,15))
entry2.pack(pady=(0,15))

button1.pack(pady=(0,15))
button2.pack(pady=(0,15))

label4.pack(pady=(15,30))

label5.pack( ipady=10, fill=tkinter.X)
label6.pack(pady=15)

radio1.pack()
radio2.pack()
radio3.pack()


minum = ["Cola", "fanta" , "sprite"]

label8 = tkinter.Label(jendela, text= "\nChoose the drink\n--------------------------------------").pack()

for index in range(len(minum)):
    radio4 = tkinter.Radiobutton(jendela, text=minum[index], value=minum[index], variable=y, command=getValu)
    radio4.pack()




label7.pack()



# making the window continously appered --> put in he bottom of the code
jendela.mainloop()