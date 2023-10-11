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


# label with different font

label1 = tkinter.Label(jendela, text="Entry Methods",
                       font="Comic",
                       foreground="CornflowerBlue",
                       background="DarkSlateBlue")

label2 = tkinter.Label(jendela, text="Insert Name")
label3 = tkinter.Label(jendela, text="Insert Age")

entry1 = tkinter.Entry(jendela, width=35)
entry2 = tkinter.Entry(jendela, width=35)

button1 = tkinter.Button(jendela, text="Edit name" , font="Calibri" , bg="Chocolate" )
button2 = tkinter.Button(jendela, text="Edit Age" , font="Calibri" , bg="Chocolate")

label4 = tkinter.Label(jendela, text= "--------------------------------------")

label5 = tkinter.Label(jendela, text= "Makanan Favorite", font=("Times New Roman",20) ,bg="Salmon" )
label6 = tkinter.Label(jendela, text= "Pilih salah satu makanan favorite mu")

spinbox1 = tkinter.Spinbox(jendela, from_=0, to= 100, state="readonly")
spinbox2 = tkinter.Spinbox(jendela, from_=0, to= 100, state="disabled")



# placement

label1.pack(pady=(20,15))
#
#
#
label2.pack(pady=(0,15))
spinbox1.pack(pady=(0,15))

label3.pack(pady=(0,15))
spinbox2.pack(pady=(0,15))

# button1.pack(pady=(0,15))
# button2.pack(pady=(0,15))

# label4.pack(pady=(15,30))

# label5.pack( ipady=10, fill=tkinter.X)
# label6.pack(pady=15)



# making the window continously appered --> put in he bottom of the code
jendela.mainloop()