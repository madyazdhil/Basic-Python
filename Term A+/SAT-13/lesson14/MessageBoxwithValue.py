import tkinter as tk
import tkinter.messagebox as msgbox

jendela = tk.Tk()
jendela.title("DIsplaying a Message Box with Option")
jendela.geometry("400x500")

#function(s)
def showmsg():
    result = msgbox.askyesno("Confirmation", "Are you sure wants to exit?")
    if result == True:
        print("The user wants to exit")
    elif result == False:
        print("the user doesn't wanted to exit")

#widgets
lbl1 = tk.Label(jendela, text="Who are you", font=("Calimbri", 20))
btn1 = tk.Button(jendela, text="No Thanks!",background="Salmon", command=showmsg)
#placements
lbl1.pack(pady=20)
btn1.pack()

jendela.mainloop()