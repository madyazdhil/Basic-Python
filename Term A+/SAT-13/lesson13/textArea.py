import tkinter as tk

jendela = tk.Tk()
jendela.title("Check box")
jendela.geometry("300x400")

#function
def munculkan_teks():
    text = textArea2.get("1.0", "end-1c")
    lb2.config(text=text)
#widget
lb1 = tk.Label(jendela, text="Text area", font=("Times New Roman", 20),foreground="DarkSlateGrey")
lb2 = tk.Label(jendela)
textArea = tk.Text(jendela, width=20, height=5, wrap="word")
textArea2 = tk.Text(jendela, width=20, height=5, wrap="word")
btn = tk.Button(jendela, text="Click me", command=munculkan_teks )

#placement
lb1.pack(pady=(20,0))
textArea.pack(pady=10)
textArea2.pack(pady=10)
btn.pack(pady=10)
lb2.pack()

jendela.mainloop()