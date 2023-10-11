import tkinter as tk
import tkinter.ttk as tc

window = tk.Tk()
window.title("Combo box")
window.geometry("300x300")

#function
def tampil():
    label2.config(text=f"the user has a {combo1.get()}")

#widgets
label1 = tk.Label(window, text= "Mobil Indonesia", font=("Arial",20))
label2 = tk.Label(window)

combo1 = tc.Combobox(window, width=20,state="readonly")
combo1['values'] = ("Honda","Toyota","BMW","Mercedes Benz")

btn1 = tk.Button(window, text="Tampilkan",command=tampil)

#placement
label1.pack(pady=(20,0))
combo1.pack(pady=10)
btn1.pack()
label2.pack(pady=10)


window.mainloop()