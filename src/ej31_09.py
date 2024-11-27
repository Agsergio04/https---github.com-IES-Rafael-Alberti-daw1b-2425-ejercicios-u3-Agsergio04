import os


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


def comprobar_vocales(cadena : str) -> int:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    contador = 0

    for elemento in cadena:

        if elemento in vocales:
            contador += 1
    
    return contador

def pedir_usuario(cadena : str) -> str:
    return input(f"{cadena}\n>").strip()


def despedida():
    limpiar_pantalla()
    print("\n\n\tAdios ! ! !")



def menu():
    condicion = None

    while condicion != "salir":
        try:
            condicion = pedir_usuario("Introduce una cadena (si quieres parar escribe salir)")


            if condicion != "salir":

                contador = comprobar_vocales(condicion)

                print(f"De la frase {condicion}\nHan aparecido esta cantidad de vocales {contador}")
                
        except ValueError:
            print("**ERROR**\nIntroduce un numero.")

def main():
    menu()
    despedida()


if __name__ == "__main__":
    main()