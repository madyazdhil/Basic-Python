import tkinter as tk

window = tk.Tk()
window.geometry("500x600")
window.title("Check Box")

#functions



def pesananMinuman():
    print(f"minuman yang dipesan adalah {psn_minum.get()}")

psn_minum = tk.StringVar()
psn_minum.set(False)

mkn1 = tk.StringVar()
mkn1.set(False)
mkn2 = tk.StringVar()
mkn2.set(False)
mkn3 = tk.StringVar()
mkn3.set(False)

#widgets
lb1 = tk.Label(window, text= " Makanan Favorite Kamu", font=("Arial",21))

ck1 = tk.Checkbutton(window, text="Nasi Kuning",variable=mkn1)
ck2 = tk.Checkbutton(window, text="Nasi Goreng",variable=mkn2)
ck3 = tk.Checkbutton(window, text="Nasi Uduk",variable=mkn3)

lb2 = tk.Label(window, text="Pesanan Minuman", font=("Arial",21))

r1 = tk.Radiobutton(window,text="Soda", value="Soda",variable=psn_minum,command=pesananMinuman)
r2 = tk.Radiobutton(window,text="Susu", value="Susu",variable=psn_minum,command=pesananMinuman)
r3 = tk.Radiobutton(window,text="Water", value="Water",variable=psn_minum,command=pesananMinuman)

#placement
lb1.pack(pady=(20,12))
ck1.pack()
ck2.pack(pady=12)
ck3.pack()

lb2.pack(pady=(20,12))
r1.pack()
r2.pack(pady=12)
r3.pack()

window.mainloop()