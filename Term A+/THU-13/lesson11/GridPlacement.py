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
label1.grid(column=0, row=0)
label2.grid(column=0,row=1)
label3.grid(column=1, row=1)
label4.grid(column=2, row = 2,)

window.mainloop()