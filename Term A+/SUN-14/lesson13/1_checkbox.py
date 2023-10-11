import tkinter as tk

window = tk.Tk()
window.title("My first Checkbox")
window.geometry("300x300")


pdk1 = tk.BooleanVar()
pdk1.set(False)
pdk2 = tk.BooleanVar()
pdk2.set(False)
pdk3 = tk.BooleanVar()
pdk3.set(False)

#funtcion
def status():
    if pdk1 == True and pdk2 == True and pdk3==True:
        print("All selected")
    elif pdk1 != False:
        print(f"pendidikan SD dari user adalah {pdk1.get()}")
    elif pdk2 != False:
        print(f"pendidikan SMP dari user adalah {pdk2.get()}")
    elif pdk3 != False:
        print(f"pendidikan SMK dari user adalah {pdk3.get()}")


#widgets
label1 = tk.Label(window, text= "Pendidikan", font=("Arial",20))

checkbox1 = tk.Checkbutton(window, text="SD", variable=pdk1,command=status)
checkbox2 = tk.Checkbutton(window, text="SMP", variable=pdk2,command=status)
checkbox3 = tk.Checkbutton(window, text="SMA/SMK", variable=pdk3,command=status)

#placement
label1.pack(pady=(12,0))
checkbox1.pack(pady=9)
checkbox2.pack(pady=9)
checkbox3.pack(pady=9)

window.mainloop()