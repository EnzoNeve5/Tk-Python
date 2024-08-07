from tkinter import *
from tkinter import messagebox

root = Tk()

def display():
    messagebox.showinfo('Info', 'Só para você saber')
    messagebox.showwarning('Perigo', 'Melhor ter cuidado')
    messagebox.showerror('Erro', 'Algo deu errado')

    okcancel = messagebox.askokcancel('O que você acha?', 'Devemos ir em frente?')
    print(okcancel)

    yesno = messagebox.askyesno('O que você acha?', 'Por favor decida')
    print(yesno)

    retrycancel = messagebox.askretrycancel('O que você acha?', 'Qual é a sua resposta')
    print(retrycancel)

    answer = messagebox.askquestion('O que você acha?', 'Qual é a sua resposta')
    print(answer)

    answer2 = messagebox.askyesnocancel('O que você acha?', 'Qual é a sua resposta')
    print(answer2)

b1 = Button(root, text='Exibir Diálogos', command=display)
b1.pack()

root.mainloop()