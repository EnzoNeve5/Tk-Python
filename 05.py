from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root  = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
    def tela(self):
        self.root.title('CATEC')
        self.root.configure(background= '#1e3743')
        self.root.geometry('700x550')
        self.root.resizable(True, True)
        self.root.maxsize(width= 800, height= 600)
        self.root.minsize(width= 500, height= 500)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        self.frame_2 = Frame(self.root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bd= 4, bg= '#167db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.17, rely= 0.1, relwidth= 0.13, relheight= 0.15)
        self.bt_buscar = Button(self.frame_1, text= 'Buscar', bd= 4, bg= '#167db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.13, relheight= 0.15)
        self.bt_buscar = Button(self.frame_1, text= 'Novo', bd= 4, bg= '#167db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.6, rely= 0.1, relwidth= 0.13, relheight= 0.15)
        self.bt_buscar = Button(self.frame_1, text= 'Alterar', bd= 4, bg= '#167db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.73, rely= 0.1, relwidth= 0.13, relheight= 0.15)
        self.bt_buscar = Button(self.frame_1, text= 'Apagar', bd= 4, bg= '#167db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.86, rely= 0.1, relwidth= 0.13, relheight= 0.15)

        self.lb_codigo = Label(self.frame_1, text= 'Código', bg= '#dfe3ee', fg= '#167db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#167db2')
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        self.lb_nome = Label(self.frame_1, text= 'Nome', bg= '#dfe3ee', fg= '#167db2')
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#167db2')
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8)

        self.lb_nome = Label(self.frame_1, text= 'Telefone', bg= '#dfe3ee', fg= '#167db2')
        self.lb_nome.place(relx= 0.05, rely= 0.6)

        self.nome_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#167db2')
        self.nome_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        self.lb_nome = Label(self.frame_1, text= 'Cidade', bg= '#dfe3ee', fg= '#167db2')
        self.lb_nome.place(relx= 0.5, rely= 0.6)

        self.nome_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#167db2')
        self.nome_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)


Application()