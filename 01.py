from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root  = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title('CATEC')
        self.root.configure(background= '#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 800, height= 600)
        self.root.minsize(width= 600, height= 400)

Application()