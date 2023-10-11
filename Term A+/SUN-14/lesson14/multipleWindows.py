import tkinter as tk


window = tk.Tk()
window.geometry("600x200")
window.title("Main")

lb1 = tk.Label(window, text= "This is the first and the main window", font=("Arial",21))

lb1.pack(pady=21)

windowExtra = tk.Toplevel(window)
windowExtra.geometry("650x250")
windowExtra.title("Extra")

lb2 = tk.Label(windowExtra, text= "This is the Second and the Extra window", font=("Arial",21))
lb2.pack(pady=16)


window.mainloop()