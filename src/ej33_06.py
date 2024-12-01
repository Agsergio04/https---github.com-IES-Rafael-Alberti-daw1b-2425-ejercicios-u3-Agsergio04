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


def mostrar_resultado(vocales : set,consonantes : set,letras_comunes : set):
    limpiar_pantalla()
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")
    print(f"Letras comunes entre vocales y consonantes: {letras_comunes}")

    pausa(0,True,True)


def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')

    consonantes = alfabeto - vocales
    letras_comunes = vocales & consonantes

    mostrar_resultado(vocales,consonantes,letras_comunes)
    

if __name__ == "__main__":
    main()
    ""
