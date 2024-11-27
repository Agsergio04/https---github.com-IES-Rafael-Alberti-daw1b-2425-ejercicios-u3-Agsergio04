import time
import os

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


def mostrar_palabras(palabra : str):
    contador = 0
    palabra = palabra[::-1]

    print(" \nLa palabra invertidad se escribe de esta forma:\n")
    while contador < len(palabra):
        print(palabra[contador])
        contador += 1


def mostrar_menu():
    limpiar_pantalla()

    print('-' * 34)
    print("\tPALABRAS INVERTIDAS")
    print('-' * 34 + "\n")


def pedir_usuario(mensaje : str) -> str:
    return input(f"{mensaje}\n>")

def main():
    bandera = True

    while bandera :
        mostrar_menu()
        cadena = pedir_usuario("Introduce una palabra para leearla del reves: (o escribe salir para salir)")

        if not cadena == "salir":

            mostrar_palabras(cadena)

            pausa(0,True,True)

        else:
            bandera = False

    limpiar_pantalla()   


      




if __name__ == "__main__":
    main()