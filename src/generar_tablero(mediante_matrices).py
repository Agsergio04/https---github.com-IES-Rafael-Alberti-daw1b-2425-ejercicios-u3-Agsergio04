import time
import os
import random

SIMBOLOS = (0,1,2)


def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    if tecla_enter:
        input("\nPresione ENTER para continuar...")
    elif tiempo > 0:
        time.sleep(tiempo)
    
    if limpiar:
        limpiar_pantalla()


def limpiar_pantalla():
    try:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    except Exception as e:
        print(f"Problemas al intentar limpiar la pantalla: {e}")


def generar_tablero(filas : int,columnas :int,valor_depositado : int):
    #Forma Comprimida
    #tablero = [[valor_depositado for _ in range(columnas)] for _ in range(filas)]

    # Forma Tradicional:

    tablero = []  
    for _ in range(filas):  
        fila = [] 

        for _ in range(columnas): 
            fila.append(valor_depositado)  

        tablero.append(fila)

    return tablero

     

def mostrar_tablero(tablero : list):
    barras = '-' * (len(tablero[0]) * 4 + 1)
    print(barras)
    for fila in tablero:
        print('|' + ''.join(f" {celda} |" for celda in fila))
        print(barras)


def pedir_mumero(mensaje : str):
    return int(input(f"{mensaje}\n>"))

def titulo():
    print('-' * 32)
    print("Tablero de Juego")
    print('-' * 32)

def mostrar_menu():
    titulo()
    print("1.- Generar tablero.")
    print("2.- Cambiar simbolo.")
    print("3.- Salir.")

def menu():
    decision = None
    valor_depositado = SIMBOLOS[0]
    while decision != 3:
        try:
            mostrar_menu()

            decision = pedir_mumero("\nPor favor,seleciona una opcion.")
            limpiar_pantalla()

            if decision == 1:
                
                filas = pedir_mumero("De cuantas filas deseas que sea la tabla.")
                if filas < 0:
                    raise ValueError("Por favor ingrese un numero positivo.")
                
                columnas = pedir_mumero("De cuantas columnas deseas que sea la tabla.")
                if columnas < 0:
                    raise ValueError("Por favor ingrese un numero positivo.")
                
                tablero = generar_tablero(filas,columnas,valor_depositado)

                mostrar_tablero(tablero)

                pausa(0,True,True)
            
            elif decision == 2:
                
                valor_depositado = pedir_mumero("Por favor,indica que simbolo quiere que se vea en su lugar.")

                if not valor_depositado:
                    raise ValueError("Introduce un simbolo:")
                
                limpiar_pantalla()
            
            elif decision == 3:
                limpiar_pantalla()

            else:
                raise ValueError("Introduce una opcion valida")
                
        except ValueError as mensaje:
            print(f"**ERROR**\n{mensaje}")
    
    print("\n\n\t\tAdios ! ! ! ")


def main():
    menu()

if __name__ == "__main__":
    main()

