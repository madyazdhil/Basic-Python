import tkinter as tk
import tkinter.ttk

jendela = tk.Tk()
jendela.title("Combo Box")
jendela.geometry("300x300")

#functions

#widgets
lb1 = tk.Label(jendela, text="Merek Mobil", font= ("Poppins, 15"), background="LightBlue")
carList = tk.ttk.Combobox(jendela, width = 30 , state="readonly")
carList['values'] = ("Honda", "Mazda", "BMW", "Mercedes", "Toyota")
carList.current(3)


#placements
lb1.pack(pady=(20,0), ipadx= 10, ipady=16)
carList.pack(pady=(10,0))




jendela.mainloop()