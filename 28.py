from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bar')
root.geometry('500x600')

def step():
    progress1.start(10)
def step2():
    progress2['value'] += 10
def step3():
    for x in range (10):
        progress3['value'] += 10
        root.update_idletasks()
        time.sleep(1)
def stop():
    progress1.stop()
def stop2():
    progress2.stop()
def stop3():
    progress3.stop()

progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress1.pack(pady=20)

progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress2.pack(pady=20)

progress3 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress3.pack(pady=20)

botao = Button(root, text='Progresso', command=step)
botao.pack(pady=20)

botao2 = Button(root, text='Progresso2', command=step2)
botao2.pack(pady=20)

botao3 = Button(root, text='Progresso3', command=step3)
botao3.pack(pady=20)

botao3 = Button(root, text='Parar', command=stop)
botao3.pack(pady=20)

botao4 = Button(root, text='Parar2', command=stop2)
botao4.pack(pady=20)

botao5 = Button(root, text='Parar3', command=stop3)
botao5.pack(pady=20)

root.mainloop()