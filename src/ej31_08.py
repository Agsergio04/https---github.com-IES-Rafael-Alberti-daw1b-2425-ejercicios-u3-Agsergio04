import os
import time



def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    if tecla_enter:
        input("\nPresione ENTER para continuar...")
    elif tiempo > 0:
        time.sleep(tiempo)
    
    if limpiar:
        limpiar_pantalla()


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear' (os.name == "posix").
    """
    try:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    except Exception as e:
        print(f"Problemas al intentar limpiar la pantalla: {e}")

def pedir_usuario(cadena : str) -> str:
    return input(">").strip()


def calcular_mitad(lista :list) -> int:
    return len(lista)//2


def comprobar_palidromo(lista : list) -> bool:
    return lista == lista[::-1]


def ejercicio():
    print('-' *40)
    print("\t PALINDROMO")
    print('-' *40)


def mostrar_menu():
    ejercicio()
    print("1.- Comprobar palindromo.")
    print("2.- Salir.\n")


def mensaje_error():
    print("Por favor,Introduce una opcion valida")


def despedida():
    limpiar_pantalla()
    print("\n\n\tAdios ! ! !")


def resultado_positivo(cadena : str):
    print(f"La palabra {cadena} es palindroma.")


def resultado_negativo(cadena : str):
    print(f"La palabra {cadena} no es palindroma.")


def menu():
    condicion = 3

    while condicion != '2':
        try:
            mostrar_menu()
            condicion = pedir_usuario("Introduce una opcion:\n")
            limpiar_pantalla()

            if condicion == '1':
                condicion = pedir_usuario("Introduce la cadena a comprobar:\n")
                if comprobar_palidromo(condicion):
                    resultado_positivo(condicion)
                    pausa(0,True,True)

                else: 
                    resultado_negativo(condicion)
                    pausa(0,True,True)
                
            else:
                mensaje_error()
        
        except ValueError:
            print(f"**ERROR**\nIntroduce un valor valido.")

    despedida()
        

def main():
    menu() 


if __name__ == "__main__":
    main()