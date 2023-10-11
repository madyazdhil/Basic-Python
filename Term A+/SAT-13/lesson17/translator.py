import tkinter as tk
import tkinter.ttk as tk1
import googletrans
import textblob


window = tk.Tk()
window.geometry("900x400")
window.title("Translator by Mr. Ahmad")

#functions
def translate():
    try:
        # ngambil key dari bahasa asal
        for key, value in languages.items():
            if (value == ori_combo.get()):
                from_language_key = key
        #ngambil key/ id dari bahasa tujuan
        for key, value in languages.items():
            if(value == target_combo.get()):
                target_language_key = key

        #mengubah text area menjadi blob atau paket
        words = textblob.TextBlob(ori_tA.get("1.0", "end-1c"))
        #men-translate blob/paket
        words = words.translate(from_lang=from_language_key, to=target_language_key)
        #masukin kedalam target text area
        target_tA.insert(1.0, words)

    except:
        print("Something is wrong")

def delete():
    ori_tA.delete("1.0","end-1c")
    target_tA.delete("1.0","end-1c")

#widgets
lb1 = tk.Label(window, text="My Translator", font=("Cooper",21),foreground="Salmon")

languages = googletrans.LANGUAGES
language_list = list(languages.values())

ori_combo = tk1.Combobox(window, width=50, state="readonly", values=language_list)
ori_tA = tk.Text(window, height=10, width=40)

target_combo = tk1.Combobox(window, width=50, state="readonly",values=language_list)
target_tA = tk.Text(window, height=10, width=40)

translateBtn = tk.Button(window, text="Translate", font=("Britannic",17),background="DarkSlateBlue",foreground="White",command=translate)
deleteBtn = tk.Button(window, text="Delete", font=("Britannic",17), background="DarkRed",foreground="White",command=delete)

#placements
lb1.grid(row=0, column=1,pady=20)

ori_combo.grid(row=1, column=0, padx=27)
ori_tA.grid(row=2, column=0, pady=15)
translateBtn.grid(row=3, column=0, ipadx=104)

target_combo.grid(row=1,column=2)
target_tA.grid(row=2,column=2)
deleteBtn.grid(row=3,column=2,ipadx=120)

window.mainloop()