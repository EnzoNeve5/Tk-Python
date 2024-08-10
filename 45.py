from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Título da nossa janela')
root.geometry('600x500+100+100')
root.config(bg='gray40')
root.resizable(True, True)
root.minsize(width=500, height=400)
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

label1 = Label(frame1, text='Código', font=('verdana', 11, 'bold'), bg='gray70')
label1.place(relx=0.05, rely=0.3, relwidth=0.15, relheight=0.1)

entry1 = Entry(frame1, font=('verdana', 11, 'bold'))
entry1.place(relx=0.25, rely=0.3, relwidth=0.15, relheight=0.1)

label2 = Label(frame1, text='Nome', font=('verdana', 11, 'bold'), bg='gray70')
label2.place(relx=0.05, rely=0.5, relwidth=0.15, relheight=0.1)

entry2 = Entry(frame1, font=('verdana', 11, 'bold'))
entry2.place(relx=0.25, rely=0.5, relwidth=0.6, relheight=0.1)

label3 = Label(frame1, text='Telefone', font=('verdana', 11, 'bold'), bg='gray70')
label3.place(relx=0.05, rely=0.7, relwidth=0.15, relheight=0.1)

entry3 = Entry(frame1, font=('verdana', 11, 'bold'))
entry3.place(relx=0.25, rely=0.7, relwidth=0.35, relheight=0.1)

frame2 = Frame(root)
frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

lista = ttk.Treeview(frame2, height=5, columns=('col0', 'col1', 'col2'))
lista.heading('#0', text='Código')
lista.heading('#1', text='Nome')
lista.heading('#2', text='Telefone')

lista.column('#0', width=70)
lista.column('#1', width=250)
lista.column('#2', width=150)

lista.place(relx=0.02, rely=0.1, relwidth=0.9, relheight=0.8)
barra = ttk.Scrollbar(frame2, orient='vertical')
barra.place(relx=0.92, rely=0.1, relheight=0.8)

root.mainloop()