import tkinter as tk

def tampilkanPop():
    windowExtra.deiconify()

def ShootWindow():
    windowExtra.withdraw()    #just for a moment and able to open again

def KillWindow():
    windowExtra.destroy()       #kill the window for good


#MAIN WINDOW
window = tk.Tk()
window.geometry("600x300")
window.title("Main")

#WIDGETS
lb1 = tk.Label(window, text= "This is the first and the main window", font=("Arial",21))
btn1 = tk.Button(window, text="Show a pop up Window", command=tampilkanPop)

#PLACEMENT
lb1.pack(pady=21)
btn1.pack()


#window 2
windowExtra = tk.Toplevel(window)
windowExtra.geometry("650x350")
windowExtra.title("Extra")

#widgets
lb2 = tk.Label(windowExtra, text= "This is the Second and the Extra window", font=("Arial",21))
btn2 = tk.Button(windowExtra, text="Click me to close me", command=ShootWindow)
btn3 = tk.Button(windowExtra, text="Click me to close me adn never able to- again",command=KillWindow)


#placement
lb2.pack(pady=16)
btn2.pack()
btn3.pack()

windowExtra.withdraw()
window.mainloop()