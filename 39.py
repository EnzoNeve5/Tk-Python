from tkinter import *

root = Tk()
root.title('Título da nossa janela')
root.geometry('300x200+100+100')
root.config(bg='gray40')
root.resizable(True, True)

frame1 = Frame(root)
frame2 = Frame(root)
label1 = Label(frame1, text='label1')
label2 = Label(frame1, text='label2')

frame1.grid(column=0, row=1, columnspan=1, ipadx=50, ipady=50, padx=1, pady=1)
frame2.grid(column=1, row=1, columnspan=1, ipadx=50, ipady=50, padx=1, pady=1)

root.mainloop()