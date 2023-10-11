import tkinter as tk
import tkinter.ttk as pj

window = tk.Tk()
window.geometry("300x240")
window.title("Car List")

#functions
def showCar():
    a= cbx.get()
    lb2.config(text=f"this user has a {a}")


#widgets
lb1 = tk.Label(window, text="Mobil Indonesia", font=("Arial",20))
lb2 = tk.Label(window)

cbx = pj.Combobox(window, width=21, state="readonly")
cbx["values"] = ["Toyota","BMW","Honda","Wuling","Ford"]
btn = pj.Button(window, text="Show", command=showCar)

#placements
lb1.pack(pady=19)
cbx.pack(pady=19)
btn.pack(pady=19)
lb2.pack(pady=19)

window.mainloop()
