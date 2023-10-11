import tkinter as tk
import tkinter.ttk as tk1

windows = tk.Tk()
windows.geometry("300x250")
windows.title("combo box")


lb1 = tk.Label(windows,text="Mobil Indonesia",justify="center")
lb2 = tk.Label(windows,text="Mobil Indonesia")
lb3 = tk.Label(windows,text="Mobil Indonesia")
lb4 = tk.Label(windows,text="Mobil Indonesia")

lb1.grid(row=0,columnspan=2)
lb2.grid(row=1,column=0,padx=5)
lb3.grid(row=1,column=1,padx=5)



windows.mainloop()
