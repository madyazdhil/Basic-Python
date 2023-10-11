import tkinter as tk

main_window = tk.Tk()
main_window.geometry("600x870")
main_window.title("Restaurant France")


#functions


#widgets
welcome = tk.Label(main_window, text= "Welcome to Restaurant France" ,font=("Gill Sans",25))
nameL=tk.Label(main_window, text="Costumer's name: ")
nameI=tk.Entry(main_window, width=24, justify="center")
tableL=tk.Label(main_window, text="Table Number")

#placements
welcome.pack(pady=25)
nameL.pack(pady=15)
nameI.pack()


main_window.mainloop()