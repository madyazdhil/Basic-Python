import tkinter

win = tkinter.Tk()
win.geometry("500x500")
win.title("This Window has label")

#widgets

#to create a label
label1 = tkinter.Label(win, text="Hi, this is me; Mr. Ahmad")
label2 = tkinter.Label(win, text="Welcome to Koding Next")
label3 = tkinter.Label(win, text="Enjoy studying with us")

#insert the pictre into a local var
pic1 = tkinter.PhotoImage(file="pic1.gif")
pic2 = tkinter.PhotoImage(file="pic1.gif")
#resize the image
pic_kecil = pic1.subsample(1,1)

#put the picture in a label
label_picture = tkinter.Label(win, image=pic_kecil)
label_picture2 = tkinter.Label(win, image=pic2)

#placement
label2.pack(pady=15)
label1.pack(pady=(0,10))
label3.pack(pady=(0,20))
label_picture.pack()
label_picture2.pack()

win.mainloop()