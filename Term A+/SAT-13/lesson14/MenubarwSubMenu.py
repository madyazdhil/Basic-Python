import tkinter as tk
import tkinter.messagebox as msgbox

jendela = tk.Tk()
jendela.title("My Apps")
jendela.geometry("400x300")

#functions
def comingsoon():
    msgbox.showinfo("On Progress", "More Info coming Soon")

def version():
    msgbox.showinfo("Version", "Current app version is Beta 13.5")

def credit():
    msgbox.showinfo("Credits","Made by Mr. Ahmad - Koding Next Samarinda")

#menubar
#save the menu to the window
menubar = tk.Menu(jendela)

#saving the sub menu to menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Avanza", command=comingsoon)
filemenu.add_separator()
filemenu.add_command(label="Xenia", command=comingsoon)
filemenu.add_separator()
filemenu.add_command(label="Wuling", command=comingsoon)
menubar.add_cascade(label="Car Brand" ,menu=filemenu)


carType = tk.Menu(menubar, tearoff=0)
carType.add_command(label="SUV", command=comingsoon)
carType.add_separator()
carType.add_command(label="MVP", command=comingsoon)
carType.add_separator()
carType.add_command(label="Sedan", command=comingsoon)
menubar.add_cascade(label="Car Type", menu=carType)

help = tk.Menu(menubar, tearoff=0)
help.add_command(label="Version", command=version)
help.add_separator()
help.add_command(label="Credit", command=credit)
menubar.add_cascade(label="Help", menu=help)



jendela.config(menu=menubar)
jendela.mainloop()
