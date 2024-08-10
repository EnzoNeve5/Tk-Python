from tkinter import *
import tkcalendar

root = Tk()
root.title('49')

def funcao1(event):
    print('Ativa função ao clicar na data')
    print(calendario.get_date())

def funcao2():
    print('Ativa função ao clicar no botao X')
    print(calendario.get_date())

calendario = tkcalendar.Calendar(root, locale='pt_br')
calendario.pack()

calendario.bind('<<CalendarSelected>>', funcao1)

botao1 = Button(root, text='X', command=funcao2)
botao1.pack()

root.mainloop()