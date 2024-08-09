from tkinter import *

root = Tk()
root.title('Título da nossa janela')
root.geometry('300x200+100+100')
root.config(bg='gray40')
root.resizable(True, True)
root.attributes('-alpha', 0.7)

frame1 = Frame(root)
frame2 = Frame(root)
label1 = Label(frame1, text='label1')
label2 = Label(frame1, text='label2')

frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)
frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

root.mainloop()