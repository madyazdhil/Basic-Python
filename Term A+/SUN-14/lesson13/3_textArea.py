import tkinter as tc

window = tc.Tk()
window.title("Text area")
window.geometry("300x300")

#fuctions
def tampil():
    text = textArea1.get("1.0","end-1c")
    lb2.config(text=text)

#widgets
lb1 = tc.Label(window, text="Reason you were with us")
lb2 = tc.Label(window)

textArea1 = tc.Text(window, width=20, height=8,wrap="word")

btn = tc.Button(window, text="Save",command=tampil)


#placement

lb1.pack(pady=(20,10))
textArea1.pack()
btn.pack(pady=10)
lb2.pack()


window.mainloop()