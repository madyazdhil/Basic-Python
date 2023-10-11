import tkinter as tk

window = tk.Tk()
window.title("Creating a menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As")
fileMenu.add_command(label="Close Project")
menubar.add_cascade(label="File", menu=fileMenu)


menubar.add_command(label="Edit")


menubar.add_command(label="About")



window.config(menu=menubar)
window.mainloop()