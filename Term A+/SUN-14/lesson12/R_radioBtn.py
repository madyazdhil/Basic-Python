import tkinter as tk

window = tk.Tk()
window.geometry("300x240")
window.title("Pendidikan")

pendidikan = tk.StringVar()
pendidikan.set(" ")

#function


#widgets
lb1 = tk.Label(window, text=" Pilih pendidikan terakhir anda")
rd1 = tk.Radiobutton(window, text="SD" , value="SD", variable=pendidikan)
rd2 = tk.Radiobutton(window, text="SMP" , value="SMP", variable=pendidikan)
rd3 = tk.Radiobutton(window, text="SMA" , value="SMA", variable=pendidikan)

#placement
lb1.pack(pady=12)
rd1.pack()
rd2.pack(pady=12)
rd3.pack()

window.mainloop()