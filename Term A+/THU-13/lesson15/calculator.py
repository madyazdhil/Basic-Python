import  tkinter as tk

window = tk.Tk()
window.title("Calculator by me")
window.geometry('250x300')

#functions

#widgets
entry = tk.Entry(window, width = 18, font=("Arial", 18), justify="right", borderwidth=6, state="readonly", background="white")

button_1 = tk.Button(window, text = "1", padx=20, pady=20 )
button_2 = tk.Button(window, text = "2", padx=20, pady=20 )
button_3 = tk.Button(window, text = "3", padx=20, pady=20 )
button_4 = tk.Button(window, text = "4", padx=20, pady=20 )
button_5 = tk.Button(window, text = "5", padx=20, pady=20 )
button_6 = tk.Button(window, text = "6", padx=20, pady=20 )
button_7 = tk.Button(window, text = "7", padx=20, pady=20 )
button_8 = tk.Button(window, text = "8", padx=20, pady=20 )
button_9 = tk.Button(window, text = "9", padx=20, pady=20 )
button_0 = tk.Button(window, text = "0", padx=20, pady=20 )

button_add = tk.Button(window, text = "+", padx=22, pady=20)
button_substraction = tk.Button(window, text = "-", padx=24, pady=20 )
button_multiplication = tk.Button(window, text = "*", padx=24, pady=20 )
button_division = tk.Button(window, text = "/", padx=24, pady=20)
button_equal = tk.Button(window, text = "=", padx=20, pady=20)
button_clear = tk.Button(window,text = "clear", padx=10, pady=20)

#placements
entry.grid(row=0, column=0,columnspan=4)
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_add.grid(row=1,column=3)


window.mainloop()