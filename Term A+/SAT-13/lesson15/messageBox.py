import tkinter as tk
import tkinter.messagebox as mg

window = tk.Tk()
window.geometry("500x600")
window.title("Check Box")

def show():
    #mg.showerror("Error Found", "You have click the wrong button for this job\nDo it again later")
    #mg.showinfo("FYI", "This button is useless")
    asking = mg.askyesno("Are You Human", "Are you Human that can breathe")
    if asking==True:
        print("this user is a human")
    else:
        print("this user is a robot")

btn = tk.Button(window, text="warning", command=show).pack(ipadx=20,ipady=21)

window.mainloop()