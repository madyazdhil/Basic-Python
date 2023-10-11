import tkinter as tk

jendela = tk.Tk()
jendela.title("Multiple Windows")
jendela.geometry("300x200")

label1 = tk.Label(jendela, text="This is the main window")
label1.pack()

#adding a new window and make it connected to main window
jendelaTambah = tk.Toplevel(jendela)
jendelaTambah.title("COmplementary window")
jendelaTambah.geometry("200x200")

label2 = tk.Label(jendelaTambah, text="Another copy of the original")
label2.pack()

jendela.mainloop()