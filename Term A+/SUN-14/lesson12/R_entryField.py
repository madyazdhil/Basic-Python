import tkinter as tk

window = tk.Tk()
window.geometry("300x250")
window.title("Student data")

#functions
def saveData():
    name = input1.get()
    age = input2.get()
    lb3.config(text= f"Data of {name} age of {age} already been saved!")

#widgets
lb1 = tk.Label(window, text="Student's name")
lb2 = tk.Label(window, text="Student's age")
lb3 = tk.Label(window)

input1 = tk.Entry(window, width=35)
input2 = tk.Entry(window, width=35)

btn1 = tk.Button(window, text="Save data", command=saveData)

#placements
lb1.pack(pady=15)
input1.pack()
lb2.pack(pady=15)
input2.pack()
btn1.pack(pady=10)
lb3.pack()


window.mainloop()