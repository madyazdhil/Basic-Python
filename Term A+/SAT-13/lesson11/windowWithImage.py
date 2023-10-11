import tkinter

jendela = tkinter.Tk()
jendela.geometry("500x400")
jendela.title("This window has an Image")

#label
label1 = tkinter.Label(jendela, text="Below is a very cute image")

#calling the function to upload an image -- and save the image to a variable called image1
image1 = tkinter.PhotoImage(file="image1.png")
#calling the tkinter funct to display to the window
label2 = tkinter.Label(jendela, image=image1)

image2 = tkinter.PhotoImage(file="image1.png")
#resizing the picturi into spesific pixel size and store into a var called image2_resize
image2_resize = image2.subsample(5,5)

label3 = tkinter.Label(jendela, image=image2_resize)

#placement
label1.pack()
label2.pack()
label3.pack()





jendela.mainloop()