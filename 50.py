from tkinter import *
from tkinter import ttk
import sqlite3

from awesometkinter import *
import awesometkinter as atk

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from PIL import ImageTk, Image
import base64

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf')
    def geraRelatCliente(self):
        self.c = canvas.Canvas('cliente.pdf')

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.fone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont('Helvetica-Bold', 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont('Helvetica-Bold', 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 665, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 595, 'Cidade: ')

        self.c.setFont('Helvetica', 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 665, self.nomeRel)
        self.c.drawString(150, 630, self.foneRel)
        self.c.drawString(150, 595, self.cidadeRel)

        self.c.rect(20, 550, 550, 200, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class Funcs():
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

    def busca_cliente(self):
        self.conecta_bd()
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCLI.insert('', END, values=i)
        self.limpa_tela
        self.desconecta_bd()

    def images_base64(self):
        self.btnovo_base = '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'
        self.btAlterar_base = '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'
        self.btApagar_base = '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'

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    def tela(self):
        self.root.title('CATEC')
        self.root.configure(background='gray20')
        self.root.geometry('900x650')
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=600)

    def frames_da_tela(self):
        self.frame_1 = atk.Frame3d(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = atk.Frame3d(self.root)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = atk.Button3d(self.frame_1, text='Limpar', command=self.limpa_tela)
        self.bt_limpar.place(relx=0.17, rely=0.1, relwidth=0.13, relheight=0.15)
        atk.tooltip(self.bt_limpar, 'Inserir dados no campo')

        self.bt_buscar = atk.Button3d(self.frame_1, text='Buscar', command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.13, relheight=0.15)
        atk.tooltip(self.bt_buscar, 'Digitar no campo o nome em que o cliente deseja pesquisar')

        self.bt_novo = atk.Button3d(self.frame_1, text='Novo', command=self.add_cliente)
        self.bt_novo.place(relx=0.56, rely=0.1, relwidth=0.13, relheight=0.15)
        atk.tooltip(self.bt_novo, 'Inserir dados no campo')

        self.bt_alterar = atk.Button3d(self.frame_1, text='Alterar', command=self.altera_cliente)
        self.bt_alterar.place(relx=0.69, rely=0.1, relwidth=0.13, relheight=0.15)
        atk.tooltip(self.bt_alterar, 'Alterar os dados inseridos no campo')

        self.bt_apagar = atk.Button3d(self.frame_1, text='Apagar', command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.82, rely=0.1, relwidth=0.13, relheight=0.15)
        atk.tooltip(self.bt_apagar, 'Apagar os dados inseridos no campo')

        self.lb_codigo = Label(self.frame_1, text='Código', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text='Nome', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        self.lb_telefone = Label(self.frame_1, text='Telefone', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        self.lb_cidade = Label(self.frame_1, text='Cidade', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
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
        self.scroolLista.place(relx=0.95, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCLI.bind('<Double-1>', self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label='Opções', menu=filemenu)
        menubar.add_cascade(label='Relatórios', menu=filemenu2)

        filemenu.add_command(label='Sair', command=Quit)
        filemenu.add_command(label='Limpa Cliente', command=self.limpa_tela)

        filemenu2.add_command(label='Ficha do cliente', command=self.geraRelatCliente)

Application()