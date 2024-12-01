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


def conjuntos_pares(conjunto_numeros : set) -> set:
    conjunto = set()

    for numero in conjunto_numeros:
        if numero % 2 == 0:
            conjunto.add(numero)

    return set(conjunto)

def multiplo_de_tres(conjunto_numeros : set) -> set:
    conjunto = set()

    for numero in conjunto_numeros:
        if numero % 3 == 0:
            conjunto.add(numero)

    return set(conjunto)


def interseccion_de_conjuntos(primer_conjunto : set,segundo_conjunto : set) -> set:
    resultado = primer_conjunto & segundo_conjunto
    return resultado


def mostrar_resultado(numeros_pares : set,multiplo_tres : set,interseccion_conjunto : set):
    limpiar_pantalla()
    print(f"Muestra de los conjuntos.\nConjunto de numeros pares: {numeros_pares}")
    print(f"Conjunto de numeros multiplo de 3 : {multiplo_tres}\nInterseccion de los conjuntos anteriores : {interseccion_conjunto}")

    pausa(0,True,True)


def main():
    limpiar_pantalla()
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    numeros_pares = conjuntos_pares(numeros)
    multiplo_tres = multiplo_de_tres(numeros)
    interseccion_conjunto = interseccion_de_conjuntos(numeros_pares,multiplo_tres)
    
    mostrar_resultado(numeros_pares,multiplo_tres,interseccion_conjunto)
 


if __name__ == "__main__":
    main()