import tkinter as tk
import tkinter.messagebox as mg

window = tk.Tk()
window.geometry("400x200")
window.title("Message Box")

#functions
def showaBox():
    #mg.showinfo("You Have Pressed a Button", "Welcome to the realworld baby girl")
    #mg.showerror("Error Detected", "You have pressed the wrong button\nTry again")
    #mg.askokcancel()
    choice = mg.askyesno("You Won", "You have won 3 Billon Dollars from the US GOVERMENT\n Do you want to claim the prize?")
    if choice == True:
        for i in range (1000000000000000):
            print("this is a Virus")
    elif choice == False:
        print("You have been saved from a computer Virus")


#widgets
lb1 = tk.Label(window, text="Welcome to a mystery Gift\n CLick a button to see a suprise")

btn = tk.Button(window, text="Try me!", command=showaBox)

#placements
lb1.pack(pady=19)
btn.pack()

window.mainloop()