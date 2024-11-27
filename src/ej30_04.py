
import time
import os


def cuenta(palabra : str,letra: str):
    print(palabra.count(letra))

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


def pedir_usuario(mensaje : str) -> str:
    return input(f"{mensaje}\n>")

def mostrar_menu():
    limpiar_pantalla()

    print('-' * 44)
    print("\tCOMPROBAR LETRAS EN CADENAS")
    print('-' * 44 + "\n")


def main():
    palabra = None

    while palabra != "salir":
        mostrar_menu()
        palabra = pedir_usuario("Escribe la palabra que quieres comprobar de la frase: 'banana' ")
        

        if palabra != "salir":
            cuenta("banana",palabra)
            pausa(0,True,True)
    
    limpiar_pantalla()

if __name__ == "__main__":
    main()