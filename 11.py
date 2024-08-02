from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs:
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
        print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectando ao banco de dados')

    def montaTabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone CHAR(20),
                cidade CHAR(40)
            );                
        """)
        self.conn.commit()
        print('Banco de dados criado')
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()        
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCLI.insert("", END, values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCLI.selection()

        for n in self.listaCLI.selection():
            col1, col2, col3, col4 = self.listaCLI.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """, (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title('CATEC')
        self.root.configure(background='#1e3743')
        self.root.geometry('700x550')
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=500, height=500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=4, bg='#167db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.17, rely=0.1, relwidth=0.13, relheight=0.15)
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=4, bg='#167db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.13, relheight=0.15)
        self.bt_novo = Button(self.frame_1, text='Novo', bd=4, bg='#167db2', fg='white', font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.13, relheight=0.15)
        self.bt_alternar = Button(self.frame_1, text='Alterar', bd=4, bg='#167db2', fg='white', font=('verdana', 8, 'bold'), command=self.altera_cliente)
        self.bt_alternar.place(relx=0.73, rely=0.1, relwidth=0.13, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=4, bg='#167db2', fg='white', font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.86, rely=0.1, relwidth=0.13, relheight=0.15)

        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#167db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#167db2')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#167db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#167db2')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#167db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#167db2')
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#167db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#167db2')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listaCLI = ttk.Treeview(self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCLI.heading('#0', text='')
        self.listaCLI.heading('#1', text='Codigo')
        self.listaCLI.heading('#2', text='Nome')
        self.listaCLI.heading('#3', text='Telefone')
        self.listaCLI.heading('#4', text='Cidade')

        self.listaCLI.column('#0', width=1)
        self.listaCLI.column('#1', width=50)
        self.listaCLI.column('#2', width=200)
        self.listaCLI.column('#3', width=125)
        self.listaCLI.column('#4', width=125)

        self.listaCLI.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCLI.bind('<Double-1>', self.OnDoubleClick)


Application()