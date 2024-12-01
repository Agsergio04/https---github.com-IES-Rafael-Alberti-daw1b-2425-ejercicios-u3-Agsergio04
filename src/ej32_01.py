import time
import os

def pausa(tiempo=0, tecla_enter=False, limpiar=True):
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


def pedir_usuario(cadena: str) -> str:
    return input(f"{cadena}\n>").lower()


def menu(divisa: dict):
    usuario = None

    while usuario != "salir":
        usuario = pedir_usuario("Introduce de qué divisa quieres saber su simbolo(o escribe salir): ")

        if usuario in divisa:
            print(f"El simbolo de {usuario.title()} es {divisa[usuario]}")

        if usuario == "salir":
            limpiar_pantalla()

        else:
            print("**ERROR**\nSimbolo no encontrado.")

def main():
    divisa = {
        'euro': '€', 
        'dollar': '$', 
        'yen': '¥'  
    }
    menu(divisa)

if __name__ == "__main__":
    main()
