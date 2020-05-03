from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.config(bg='#000')
ventana.geometry('350x450')

i = 0

#Pantalla Principal (falta resolver el alto porque esta muy angosta)

e_texto = Entry(ventana, font=('Bitwise 15'), bg='#000000', fg='#00ff00', justify='right')
e_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
e_texto.config()

#Funciones

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def robot():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0
    

#BOTONES DE NUMEROS
boton1 = Button(ventana, text = '1', command = lambda:click_boton(1), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton2 = Button(ventana, text = '2', command = lambda:click_boton(2), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton3 = Button(ventana, text = '3', command = lambda:click_boton(3), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton4 = Button(ventana, text = '4', command = lambda:click_boton(4), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton5 = Button(ventana, text = '5', command = lambda:click_boton(5), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton6 = Button(ventana, text = '6', command = lambda:click_boton(6), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton7 = Button(ventana, text = '7', command = lambda:click_boton(7), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton8 = Button(ventana, text = '8', command = lambda:click_boton(8), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton9 = Button(ventana, text = '9', command = lambda:click_boton(9), font=('Bitwise 25'), bg='black', fg='white', width = 3)
boton0 = Button(ventana, text = '0', command = lambda:click_boton(0), font=('Bitwise 25'), bg='black', fg='white', width = 3)

#Botones Simbolos

boton_borrar = Button(ventana, text = 'DEL', command = lambda:borrar(), font=('Console 15'), bg='black', fg='white')
boton_parent1 = Button(ventana, text = '(', command = lambda:click_boton('('), font=('Console 20'), width=3, bg='black', fg='white')
boton_parent2 = Button(ventana, text = ')', command = lambda:click_boton(')'), font=('Console 20'), width=3, bg='black', fg='white')
boton_punto = Button(ventana, text='.', command=lambda: click_boton('.'), font=('Console 20'), bg='black', fg='white', width = 3)

boton_div = Button(ventana, text = '/', command = lambda:click_boton('/'), font=('Console 20'), bg='black', fg='white', width = 3)
boton_mul = Button(ventana, text = '*', command = lambda:click_boton('*'), font=('Console 20'), bg='black', fg='white', width = 3)
boton_suma = Button(ventana, text ='+', command = lambda:click_boton('+'), font=('Console 20'), bg='black', fg='white', width = 3)
boton_resta = Button(ventana, text='-', command = lambda:click_boton('-'), font=('Console 20'), bg='black', fg='white', width = 3)
boton_igual = Button(ventana, text='=', command=lambda: robot(), font=('Console 20'), width=8, bg='black', fg='white')

#Botones en Pantalla

boton_borrar.grid(row=1, column = 0, padx=5, pady=5)
boton_parent1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parent2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mul.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_punto.grid(row=5, column=1, padx=5, pady=5)
boton_igual.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

ventana.mainloop()