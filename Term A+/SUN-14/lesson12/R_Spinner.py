import tkinter as tk

window = tk.Tk()
window.geometry("300x240")
window.title("spinner")

#widgets
lb1 = tk.Label(window, text="Pilih Usia sekarang")
lb2 = tk.Label(window, text="Pilih Ukuran Sepatu")
lb3 = tk.Label(window)

sp1 = tk.Spinbox(window, from_=17, to=24, state="readonly")
sp2 = tk.Spinbox(window, values=(39, 42, 44), width=12)

#placement
lb1.pack(pady=12)
sp1.pack()
lb2.pack(pady=12)
sp2.pack()
lb3.pack(pady=12)


window.mainloop()