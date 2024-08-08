from modulos import *
from validEntry import Validadores
from frameGrad import GradientFrame
from reports import Relatorios
from funcionalidades import Funcs
from placeHolder import EntPlaceHold

import brazilcep

root = tix.Tk()

class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    def cepCorreios(self):
        try:
            self.cidade_entry.delete(0, END)
            self.endereco_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            zipcode = self.cep_entry.get()
            dadosCep = brazilcep.get_address_from_cep(zipcode)
            print(dadosCep)
            self.cidade_entry.insert(END, dadosCep['city'])
            self.endereco_entry.insert(END, dadosCep['street'])
            self.bairro_entry.insert(END, dadosCep['district'])
        except:
            messagebox.showinfo('CATEC', 'CEP não encontrado')
        
    def tela(self):
        self.root.title('CATEC')
        self.root.configure(background='#1e3743')
        self.root.geometry('800x600')
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=800, height=600)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = GradientFrame(self.abas)
        self.aba3 = GradientFrame(self.abas, 'blue', 'white')

        self.aba1.configure(background='#dfe3ee')
        self.aba2.configure(background='#dfe3ee')
        self.aba3.configure(background='#dfe3ee')

        self.abas.add(self.aba1, text='Aba 1')
        self.abas.add(self.aba2, text='Aba 2')
        self.abas.add(self.aba3, text='Aba 3')

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas_bt = Canvas(self.aba1, bd=0, bg='#1e3743', highlightbackground='gray', highlightthickness=3)
        self.canvas_bt.place(relx=0.16, rely=0.08, relwidth=0.2775, relheight=0.19)

        self.bt_limpar = Button(self.aba1, text='Limpar', bd=4, bg='#167db2', fg='white', activebackground='#108ecb', activeforeground='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.17, rely=0.1, relwidth=0.13, relheight=0.15)

        texto_balao_limpar = 'Apague os dados inseridos no campo'
        self.balao_limpar = tix.Balloon(self.aba1)
        self.balao_limpar.bind_widget(self.bt_limpar, balloonmsg=texto_balao_limpar)

        self.bt_buscar = Button(self.aba1, text='Buscar', bd=4, bg='#167db2', fg='white', activebackground='#108ecb', activeforeground='white', font=('verdana', 8, 'bold'), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.13, relheight=0.15)

        texto_balao_buscar = 'Digite no campo o nome em que o cliente deseja pesquisar'
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg=texto_balao_buscar)
        
        self.btnovo = PhotoImage(data=base64.b64decode(self.btnovo_base))
        self.btnovo = self.btnovo.subsample(2, 2)
        self.bt_novo = Button(self.aba1, bd=0, image=self.btnovo, command=self.add_cliente)
        self.bt_novo.place(relx=0.61, rely=0.12, width=80, height=29)

        self.btAlterar = PhotoImage(data=base64.b64decode(self.btAlterar_base))
        self.btAlterar = self.btAlterar.subsample(2, 2)       
        self.bt_alterar = Button(self.aba1, bd=0, image=self.btAlterar, command=self.altera_cliente)
        self.bt_alterar.place(relx=0.74, rely=0.12, width=80, height=29)

        self.btApagar = PhotoImage(data=base64.b64decode(self.btApagar_base))
        self.btApagar = self.btApagar.subsample(2, 2)
        self.bt_apagar = Button(self.aba1, bd=0, image=self.btApagar, command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.87, rely=0.12, width=80, height=29)

        self.lb_codigo = Label(self.aba1, text='Código', bg='#dfe3ee', fg='#167db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2', validate='key', validatecommand=self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.aba1, text='Nome', bg='#dfe3ee', fg='#167db2')
        self.lb_nome.place(relx=0.05, rely=0.4)

        self.nome_entry = EntPlaceHold(self.aba1, 'Digite o nome do cliente - campo obrigatório')
        self.nome_entry.place(relx=0.05, rely=0.5, relwidth=0.8)

        self.lb_telefone = Label(self.aba1, text='Telefone', bg='#dfe3ee', fg='#167db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2')
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        self.lb_cidade = Label(self.aba1, text='Cidade', bg='#dfe3ee', fg='#167db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        self.lb_endereco = Label(self.aba1, text='Endereço', bg='#dfe3ee', fg='#167db2')
        self.lb_endereco.place(relx=0.05, rely=0.8)

        self.endereco_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2')
        self.endereco_entry.place(relx=0.05, rely=0.9, relwidth=0.4)

        self.lb_bairro = Label(self.aba1, text='Bairro', bg='#dfe3ee', fg='#167db2')
        self.lb_bairro.place(relx=0.5, rely=0.8)

        self.bairro_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2')
        self.bairro_entry.place(relx=0.5, rely=0.9, relwidth=0.4)

        self.bt_cep = Button(self.aba1, text='CEP', bd=4, bg='#167db2', fg='white', activebackground='#108ecb', activeforeground='white', font=('verdana', 8, 'bold'), command=self.cepCorreios)
        self.bt_cep.place(relx=0.275, rely=0.3, relwidth=0.10, relheight=0.10)

        self.cep_entry = Entry(self.aba1, bg='#dfe3ee', fg='#167db2')
        self.cep_entry.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.10)

        self.Tipvar = StringVar(self.aba2)
        self.TipV = ('Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)', )
        self.Tipvar.set('Solteiro(a)')
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)
        
        self.bt_novajanela = Button(self.aba2, text='Nova Janela', bd=4, bg='#167db2', fg='white', activebackground='#108ecb', activeforeground='white', font=('verdana', 8, 'bold'), command=self.janela2)
        self.bt_novajanela.place(relx=0.3, rely=0.1, relwidth=0.13, relheight=0.15)

        texto_balao_novajanela = 'Abra uma nova janela'
        self.balao_novajanela = tix.Balloon(self.aba2)
        self.balao_novajanela.bind_widget(self.bt_novajanela, balloonmsg=texto_balao_novajanela)

        self.bt_calendario = Button(self.aba2, text='Data', command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx=0.5, rely=0.2)

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

    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title('Janela 2')
        self.root2.configure(background='lightblue')
        self.root2.geometry('400x200')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), '%P')

Application()