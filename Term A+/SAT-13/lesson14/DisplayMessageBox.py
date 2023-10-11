import tkinter as tk
import tkinter.messagebox as msgbox

jendela = tk.Tk()
jendela.title("DIsplaying a Message Box")
jendela.geometry("400x500")

#function(s)
def showmsg():
    #msgbox.showinfo("Just an Info" , "You Have Clicked a button")
    #msgbox.showwarning("Be Careful!", "You Clicked a Button")
    #msgbox.showerror("Error Detected!", "You Clicked a Button!!??!")
    #msgbox.askquestion("Confusion Detected!", "Do you Clicked a Button?!")
    msgbox.askyesnocancel("Confusion Detected!", "Do you Clicked a Button?!")

#widgets
lbl1 = tk.Label(jendela, text="Showing a warning", font=("Calimbri", 20))
btn1 = tk.Button(jendela, text="Click me!",background="Salmon", command=showmsg)
#placements
lbl1.pack(pady=20)
btn1.pack()

jendela.mainloop()