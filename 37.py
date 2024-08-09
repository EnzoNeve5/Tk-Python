from tkinter import *

root = Tk()
root.title('Título da nossa janela')
root.geometry('300x200+100+100')
root.config(bg='gray40')
root.resizable(True, True)

frame1 = Frame(root)
frame1.pack()

root.mainloop()