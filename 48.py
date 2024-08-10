from tkinter import *
from tkinter import ttk
from awesometkinter import *
import awesometkinter as atk

root = Tk()

class Janela():
    def __init__(self):
        self.root = root
        self.root.title('Título da nossa janela')
        self.root.geometry('600x500+100+100')
        self.root.config(bg='gray20')
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)
        self.root.attributes('-alpha', 0.7)

        self.frame_superior()
        self.frame_inferior()

        self.root.mainloop()

    def frame_superior(self):
        frame1 = atk.Frame3d(self.root)
        frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        botao1 = atk.Button3d(frame1, text='Novo')
        botao1.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.16)
        atk.tooltip(botao1, 'Inserir dados no campo')

        botao2 = atk.Button3d(frame1, text='Alterar')
        botao2.place(relx=0.21, rely=0.05, relwidth=0.15, relheight=0.16)
        atk.tooltip(botao2, 'Alterar os dados inseridos no campo')

        botao3 = atk.Button3d(frame1, text='Apagar')
        botao3.place(relx=0.37, rely=0.05, relwidth=0.15, relheight=0.16)
        atk.tooltip(botao3, 'Apagar os dados inseridos no campo')

        botao4 = atk.Button3d(frame1, text='Buscar')
        botao4.place(relx=0.53, rely=0.05, relwidth=0.15, relheight=0.16)
        atk.tooltip(botao4, 'Digitar no campo o nome em que o cliente deseja pesquisar')

        bar = atk.RadialProgressbar3d(frame1, fg='cyan', bg=atk.DEFAULT_COLOR, size=120)
        bar.place(relx=0.75, rely=0.05)
        bar.start()

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

    def frame_inferior(self):
        frame2 = atk.Frame3d(self.root)
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

Janela()