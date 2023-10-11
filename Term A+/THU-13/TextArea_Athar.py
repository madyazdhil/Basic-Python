import tkinter as tk


windows = tk.Tk()
windows.geometry("300x250")
windows.title("combo box")


lb1 = tk.Label(windows,text="Mobil Indonesia")
tA = tk.Text(windows, height=3, width=25)

lb1.pack(pady=12)
tA.pack(pady=12)



windows.mainloop()