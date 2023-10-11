import tkinter as tk

jendela = tk.Tk()
jendela.title("Check box")
jendela.geometry("300x300")

#functions
def simpanFav():

    text = simpanBox1.get()
    lb2.config(text=f"Ternyata you suka {text}")


simpanBox1 = tk.StringVar()
simpanBox1.set(" ")
simpanBox2 = tk.StringVar()
simpanBox2.set(" ")
simpanBox3 = tk.StringVar()
simpanBox3.set(" ")
simpanBox4 = tk.StringVar()
simpanBox4.set(" ")


#widget
lb1 = tk.Label(jendela, text="Makanan Favorite", font=("Times New Roman", 20),foreground="DarkSlateGrey")
lb2 = tk.Label(jendela, text= " ")
checkbox1 = tk.Checkbutton(jendela,
                           text="Nasi Goreng",
                           variable= simpanBox1,
                           onvalue="Nasi Goreng",
                           offvalue="dont liek Nasi Goreng",
                           command=simpanFav)
checkbox2 = tk.Checkbutton(jendela, text="Mie Ayam", variable= simpanBox2,onvalue="Mie Ayam",offvalue="gasuka ini",command=simpanFav)
checkbox3 = tk.Checkbutton(jendela, text="Sate padang", variable= simpanBox3,onvalue="Sate padang",offvalue="gasuka ini",command=simpanFav)
checkbox4 = tk.Checkbutton(jendela, text="Mie Dok Dok Yogya", variable= simpanBox4,onvalue="Mie Dok Dok Yogya",offvalue="gasuka ini",command=simpanFav)

#placement
lb1.pack(pady=(20,0))
checkbox1.pack(pady=10)
checkbox2.pack(pady=5)
checkbox3.pack(pady=5)
checkbox4.pack(pady=5)
lb2.pack(pady=5)


jendela.mainloop()