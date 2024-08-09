from tkinter import *
from entryPlaceHolder import *
from gradienteFrame import *

root = Tk()

gradiente = GradientFrame(root, 'yellow', 'red')
gradiente.pack()
holder = EntPlaceHold(root, 'Digite seu nome')
holder.place(x=10, y=10)

root.mainloop()