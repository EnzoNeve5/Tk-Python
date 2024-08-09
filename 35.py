from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry

root = Tk()
root.title('Países da América do Norte e Central')
root.geometry('500x400')
root.config(bg='#f25252')

countries = [
        'Antígua e Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canadá',
        'Costa Rica', 'Cuba', 'Dominica', 'República Dominicana', 'El Salvador',
        'Granada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'México',
        'Nicarágua', 'São Cristóvão e Névis', 'Panamá', 'Santa Lúcia', 
        'São Vincente e Granadinas', 'Trindade e Tobago', 'Estados Unidos da América'
        ]

frame = Frame(root, bg='#f25252')
frame.pack(expand=True)

Label(frame, bg='#f25252', font=('Times', 20), text='Países da América do Norte e Central').pack()

entry = AutocompleteEntry(frame, width=30, font=('Times', 18), completevalues=countries)

entry.pack()

root.mainloop()