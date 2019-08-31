import json
from tkinter import Tk,simpledialog,messagebox
from difflib import get_close_matches

print('Dictionary')
root = Tk()
root.withdraw()
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #example USA
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=simpledialog.askstring('word',"Did you mean %s instead? Enter Y if yes,or N if no."% get_close_matches(w,data.keys())[0])
        if yn =="Y" or yn =="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =="N" or yn=="n":
            messagebox.showinfo('word',"The word deosn't exist. PLease double check it.")
        else:
            messagebox.showinfo('word',"We didn't understand your entry")
    else:
        messagebox.showinfo('None','The word doesn\'t exist in the dictinory')
    return data[word]

while True:
    word = simpledialog.askstring('word','Enter the word:')

    output = translate(word)

    if type(output) == list:
        output='\nOR \n'.join(output)
        messagebox.showinfo('Meaning of %s'% word, output)
        #for item in output:
         #   messagebox.showinfo('word',item)
    else:
        messagebox.showinfo('Meaning of %s'% word ,output)
