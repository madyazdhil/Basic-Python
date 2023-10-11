import tkinter as tk

window = tk.Tk()
window.geometry("300x240")
window.title("Favorite food")

vf1 = tk.StringVar()
vf1.set(" ")
vf2 = tk.StringVar()
vf2.set(" ")
vf3 = tk.StringVar()
vf3.set(" ")

#widgets
lb1 = tk.Label(window, text="Choose your favorite food")

ck1 = tk.Checkbutton(window, text="Nasi Goreng", variable=vf1)
ck2 = tk.Checkbutton(window, text="Nasi Kuning", variable=vf2)
ck3 = tk.Checkbutton(window, text="Nasi Padang", variable=vf3)


#placements
lb1.pack(pady=20)
ck1.pack(pady=(0,12))
ck2.pack(pady=12)
ck3.pack(pady=12)


window.mainloop()