import tkinter

window = tkinter.Tk()
window.geometry("650x600")
window.title("Window with label")

#creating label / writings inside the window

#widget
#1. widget is a label - to place a text
label1 = tkinter.Label(window, text="My first label", font=("Arial",20))
label2 = tkinter.Label(window, text="This is my second label", font=("Calibri",15))


#2. image
myImage = tkinter.PhotoImage(file="image.png")
#saving the image to a variable
label3 = tkinter.Label(window, image=myImage)
#putting the image into the label
myImage_resize = myImage.subsample(5,5)
label4 = tkinter.Label(window, image=myImage_resize)


#placement
label1.pack()
label2.pack()
label3.pack()
label4.pack()

window.mainloop()