import tkinter as tk
import tkinter.messagebox as mg

window = tk.Tk()
window.geometry("400x200")
window.title("Message Box")

#functions
def comingSoon():
    mg.showwarning(
        "Not Available yet", "This operation is coming in later update"
    )
def about():
    mg.showinfo(
        "Developer List","Here are the Developer for this virus app:\n1.Roger\n2.Dio\n3.Ahmad"
    )
def version():
    mg.showwarning("Update needed","Your current version is 3.45.44.88.21.33\n\nUpdate Immediately")

#widgets
lb1 = tk.Label(window, text="Welcome to a mystery Gift\n CLick a button to see a suprise")

btn = tk.Button(window, text="Try me!")

#menubar

menubar = tk.Menu(window)
#menubar.add_command(label="File")
#menubar.add_command(label="Help")
#menubar.add_command(label="About")

fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="New", command=comingSoon)
fileMenu.add_separator()#to seperate each menu
fileMenu.add_command(label="Print", command=comingSoon)
menubar.add_cascade(label="File",menu=fileMenu)

helpMenu = tk.Menu(menubar)
helpMenu.add_command(label="Get Help", command=comingSoon)
helpMenu.add_command(label="Shortcut", command=comingSoon)
menubar.add_cascade(label="Help",menu=helpMenu)

aboutMenu = tk.Menu(menubar)
aboutMenu.add_command(label="Develepers",command=about)
aboutMenu.add_command(label="Version",command=version)
menubar.add_cascade(label="About", menu=aboutMenu)

#placements
lb1.pack(pady=19)
btn.pack()

window.config(menu=menubar)
window.mainloop()