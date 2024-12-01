import time
import os

def pausa(tiempo: int, tecla_enter : bool, limpiar : bool):
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


def pedir_usuario(cadena: str) -> list:
    return input(f"{cadena}\n>").lower().split("/")

def domicilios_clientes(lista_compras : list) -> set:
    domicilio = set()

    #sorted() genera una lista ordenada
    for compra in lista_compras:
        domicilio.add(compra[3])

    return domicilio


def main():
    lista_compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
     ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
     ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

    v = domicilios_clientes(lista_compras)
    numeros = {1,2,3,4,5,6,7,8,9,10}
    pares = {num for num in numeros if num & 2 == 0}

    print(pares)

if __name__ == "__main__":
    main()
