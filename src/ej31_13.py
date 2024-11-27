import time
import os
import math

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


def pedir_usuario(cadena : str) -> str:
    return input(f"{cadena}\n>").strip().split(",")


def calcular_media(lista : list) -> float:
    suma = 0
    divisor = len(lista)
    for numero in lista:
        suma += int(numero)

    return suma // divisor


def calcular_desviacion_tipica(lista : list) -> float:
    return math.sqrt(calcular_media(lista))


def comprobar_lista(lista : list) -> list:
    lista_comprobada = []

    for elemento in lista:
        lista_comprobada.append(int(elemento))

    return lista


def mostrar_resultado(media,desviacion_tipica):
    pausa(0,False,True)

    print(f"La media de los valores dados es: {media}\n")
    print(f"La desviacion tipica de los valores dados es: {desviacion_tipica:.2f}\n")

    pausa(0,True,True)



def menu():
    entrada = None

    while entrada is not list():
        try:
            entrada = pedir_usuario("Introduce una cadena de numeros separados por comas:")

            lista_comprobada = comprobar_lista(entrada)

            media,desviacion_tipica = calcular_media(lista_comprobada),calcular_desviacion_tipica(lista_comprobada)

            mostrar_resultado(media,desviacion_tipica)
        except ValueError:
            pausa(0,False,True)
            print("**ERROR**\nHas introducido un valor invalido.\nPor favor vuelva a escribir la cadena.\n")

    

def main():
    menu()


if __name__ == "__main__":
    main()