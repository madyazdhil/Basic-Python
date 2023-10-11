#we neet to call the module to create a window
# tkinter
import tkinter


#SAVE THE module to create window inside a variable called "window"
#window = tkinter.Tk()
jendela = tkinter.Tk()

#create the size of the window
#window.geometry("400x300")
jendela.geometry("500x400")


#create a title for the window
jendela.title("Creating my first window")

#creating a label
# label1 = tkinter.Label(window, text="This is a label")
# label2 = tkinter.Label(window, text="My name is Ahmad")
# label3 = tkinter.Label(window, text="My age is 21")

#label with different font
label4 = tkinter.Label(jendela, text="Enjoy this pic", font="Calibri")
#label with different text coloure ( using foreground )
label5 = tkinter.Label(jendela, text="This is my favorite", font="Comic" , foreground="CornflowerBlue")
#label with different text coloure ( using background )
label6 = tkinter.Label(jendela, text="This is my favorite", font="Comic" , foreground="CornflowerBlue" , background="DarkSlateBlue" )

#placement
# label1.pack()
# label2.pack()
# label3.pack()
label4.pack()
label5.pack()
label6.pack()








#making the window continously appered --> put in he bottom of the code
jendela.mainloop()