import tkinter as tk
import tkinter.ttk as tk1

windows = tk.Tk()
windows.geometry("300x250")
windows.title("combo box")


lb1 = tk.Label(windows,text="Mobil Indonesia")
cbx = tk1.Combobox(windows, width= 23)
cbx["values"] = ("Wuling","Honda","BMW","Mercedes","Toyota")

lb1.pack(pady=12)
cbx.pack(pady=12)



windows.mainloop()