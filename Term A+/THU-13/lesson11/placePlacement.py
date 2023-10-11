import tkinter

window = tkinter.Tk()
window.title("There's a Label")
window.geometry("500x600")

#Widgets
label1 = tkinter.Label(window, text="My first label",
                       font=("Arial",20))
label2 = tkinter.Label(window, text="I'm excited to learn", font=("Calimbri",12),
                       foreground="DarkGreen")
label3 = tkinter.Label(window, text="What is it", font=("Calimbri",12),
                       background="Ivory")

img = tkinter.PhotoImage(file="image.png")
img_1 = img.subsample(5,5)
label4 = tkinter.Label(window, image=img_1)

#Placements
label1.place(x=165, y=50)
label2.place(x= 185, y= 100, width=200, height=70)
label3.place()
label4.place()

window.mainloop()