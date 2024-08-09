from tkinter import *

root = Tk()
root.title('Título da nossa janela')
root.geometry('500x400+100+100')
root.config(bg='gray40')
root.resizable(True, True)
root.attributes('-alpha', 0.7)

frame1 = Frame(root)
frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

botao1 = Button(frame1, text='Novo', bg='gray35', fg='white', font=('verdana', 12, 'bold'))
botao1.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.15)

botao2 = Button(frame1, text='Alterar', bg='gray35', fg='white', font=('verdana', 12, 'bold'))
botao2.place(relx=0.21, rely=0.05, relwidth=0.15, relheight=0.15)

botao3 = Button(frame1, text='Apagar', bg='gray35', fg='white', font=('verdana', 12, 'bold'))
botao3.place(relx=0.37, rely=0.05, relwidth=0.15, relheight=0.15)

botao4 = Button(frame1, text='Buscar', bg='gray35', fg='white', font=('verdana', 12, 'bold'))
botao4.place(relx=0.53, rely=0.05, relwidth=0.15, relheight=0.15)

frame2 = Frame(root)
frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

root.mainloop()