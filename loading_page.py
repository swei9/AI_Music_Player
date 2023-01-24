from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk,Image
import customtkinter
import os
import sys

root = Tk()

height = 430
width = 530
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1)
root.config(background='grey')

exit_btn = Button(root, text='X', command=lambda: exit_window(), bg='grey', bd=0, activebackground='grey')
exit_btn.place(x=512, y=0)


welcome_label = Label(root, text='BEATSCAPE', font=("Helvetica", 30, 'bold'), bg='grey', fg='white')
welcome_label.place(x=150, y=10)

loading_label = Label(root, text='Please Wait, System Processing', font=("Times", 25,), bg='grey')
loading_label.place(x=60, y=180)

progress_label = Label(root, text='Progress: ', font=("Times", 12, 'bold'), bg='grey')
progress_label.place(x=210, y=380)

progress_bar = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress_bar.place(x=15, y=350)

def exit_window():
    sys.exit(root.destroy())


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Progress: ' +(str(10*i) + '%')
        progress_label.config(text=txt)
        progress_label.after(500, load)
        progress_bar['value'] = 10*i
        i += 1

load()

root.after(5100,lambda:root.destroy())

root.mainloop()