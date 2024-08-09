from tkinter import *

root = Tk()
root.title('Título da nossa janela')
root.geometry('300x200+100+100')
root.config(bg='gray40')
root.resizable(True, True)

frame1 = Frame(root)
frame1.pack(side=TOP, ipadx=210, ipady=80, padx=10, pady=10)
frame2 = Frame(root)
frame2.pack(side=BOTTOM, ipadx=210, ipady=80, padx=10, pady=10)
label1 = Label(frame1, text='label1')
label1.pack()
label2 = Label(frame1, text='label2')
label2.pack()

root.mainloop()