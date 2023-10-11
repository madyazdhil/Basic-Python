import tkinter as tk
import tkinter.ttk as tk1
import tkinter.messagebox as mg
import googletrans
import textblob

window = tk.Tk()
window.title("Translator By me")
window.geometry("900x400")

#function

def translateIt():

    #getting the ID from the original language (e.g : id, en , etc)
    try:
        # Get Languages From Dictionary Keys
        # Get the From Langauage Key
        for key, value in languages.items():
            if (value == Ori_lang.get()):
                from_language_key = key

        # Get the To Language Key
        for key, value in languages.items():
            if (value == trans_lang.get()):
                to_language_key = key

        # Turn Original Text into a TextBlob
        words = textblob.TextBlob(Ori_trans.get("1.0", "end-1c"))

        # Translate Text
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        # Output translated text to screen
        trans_result.insert(1.0, words)

    except:
        print("something is wrong")

def clear():
    Ori_trans.delete("1.0", "end-1c")
    trans_result.delete("1.0", "end-1c")


#widgets
title = tk.Label(window, text= "Translator by Me" ,font=("Cooper",21), foreground="Salmon")

languages = googletrans.LANGUAGES
language_list = list(languages.values())


#Original text
Ori_lang = tk1.Combobox(window, width=40, state="readonly", values=language_list) #combo box
Ori_trans = tk.Text(window, width=32, height=10) # text area

#translated text
trans_lang = tk1.Combobox(window, width=40, state="readonly",values=language_list)
trans_result = tk.Text(window, width=32, height=10)

#action buttons
transBtn = tk.Button(window,text="Translate" , font=("Times New Roman",17),background="Salmon", command=translateIt)
DeleteBtn = tk.Button(window,text="Clear" , font=("Times New Roman",17),background="Red", command=clear)


#placement
title.grid(row=0,column= 1,pady= (20,0))

#original tetxs
Ori_lang.grid(row=1, column=0, padx=(90,0),pady=20)
Ori_trans.grid(row=2,column=0, padx=(90,0))
transBtn.grid(row=3, column=0, padx=(90,0), ipadx=76,pady=20)

trans_lang.grid(    row=1, column=2)
trans_result.grid(  row=2, column=2)
DeleteBtn.grid(     row=3, column=2, ipadx=94)

window.mainloop()