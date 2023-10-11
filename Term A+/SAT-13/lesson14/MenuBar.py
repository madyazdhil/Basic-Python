import tkinter as tk


jendela = tk.Tk()
jendela.title("Window with Menu Bar")
jendela.geometry("400x500")

#window configuration
menubar=tk.Menu(jendela)

menubar.add_command(label="Menu 1")
menubar.add_command(label="Menu 2")
menubar.add_command(label="Menu 3")


jendela.config(menu=menubar)
jendela.mainloop()