from tkinter import *

root = Tk()

def abrir_legenda():
    label = Label(root, text='Legenda.srt')
    label.pack()

logo = Label(root, text='legendary', font=('Arial', 50))
    # font-size: 50px;
    # font-family: monospace;
    # font-weight: 900;
    # text-shadow: 2px 2px 5px black;
    # color: white;

title = Label(root, text='Resize your subtitles!')
open_subtitle = Button(root, text='Abrir legenda', padx=20, command=abrir_legenda, fg='#F11')
timer_label = Label(root, text='Quanto tempo você quer alterar?')
timer = Entry(root, width=30)   # timer.get para pegar o valor
change_label = Label(root, text='A partir de qual momento?')
since_timer = Entry(root, width=30)
change_subtitle = Button(root, text='Alterar legenda', padx=20)


logo.pack()
title.pack()
open_subtitle.pack()
timer_label.pack()
timer.pack()
timer.insert(0, 'hh:mm:ss')
change_label.pack()
since_timer.pack()
change_subtitle.pack()

root.mainloop()
