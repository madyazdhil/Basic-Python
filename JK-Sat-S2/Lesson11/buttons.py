import tkinter

win = tkinter.Tk()
win.geometry("500x500")
win.title("This Window has label")

#widgets

#labels
#to create a label
label1 = tkinter.Label(win, text="Hi, this is me; Mr. Ahmad")
label2 = tkinter.Label(win, text="Welcome to Koding Next",foreground="Black",background="DarkSalmon")
label3 = tkinter.Label(win, text="Enjoy studying with us")

#insert the pictre into a local var
pic1 = tkinter.PhotoImage(file="pic1.gif")
pic2 = tkinter.PhotoImage(file="pic1.gif")
#resize the image
pic_kecil = pic1.subsample(1,1)

#put the picture in a label
label_picture = tkinter.Label(win, image=pic_kecil)

#buttons
btn1 = tkinter.Button(win, text="Click me")
btn2 = tkinter.Button(win, text="Look What happened",background="DarkSlateBlue",foreground="Beige")


#placement
label2.pack(ipady = 20,ipadx=15)
label1.pack()
label3.pack()

btn1.pack(ipadx=25 , ipady=10, pady = 15)
btn2.pack(ipadx=25 , ipady=10, pady = 15)

label_picture.pack()



win.mainloop()