from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode='w',filetype=[('text files','.txt')])
    if new_file is None:
        return
    text = str(entry.get(0,tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r',filetype= [('text files','*.txt')])
    if file is not None:
        content = file.read()

    entry.insert(tk.INSERT,content)

def clearFile():
    entry.delete(1.0,tk.END)




'''ui of application'''
canvas= tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="#eace17")
top= tk.Frame(canvas)
top.pack(padx=10,pady=5,anchor='nw')

button1=tk.Button(canvas,text="open", bg="#eace17", command=openFile)
button1.pack(in_=top,side="left")

button2=tk.Button(canvas,text="save", bg="#eace17", command=saveFile)
button2.pack(in_=top,side="left")

button3=tk.Button(canvas,text="clear", bg="#eace17", command=clearFile)
button3.pack(in_=top,side="left")

button4=tk.Button(canvas,text="exit", bg="#eace17", command=exit)
button4.pack(in_=top,side="left")

entry=tk.Text(canvas,wrap=tk.WORD, bg="#f4f2a4", font=("serif",13))
entry.pack(padx=10,pady=15, expand="true", fill="both")


canvas.mainloop()