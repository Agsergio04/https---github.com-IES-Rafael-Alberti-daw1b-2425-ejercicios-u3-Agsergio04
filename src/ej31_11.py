import time
import os
import random

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


def menu():
    pass

def generar_vector(min : int,max : int,rango : int) -> tuple:
    """
    Args:
        min (int):
        max (int):
        rango(int):
    
    Returns : 
    
    """
    """
    contador = 0
    lista_creadora = []

    
    while contador < rango:
        numero = random.randint(min,max)

        if numero not in lista_creadora:
            lista_creadora.append(numero)
            contador += 1
    
    vector = tuple(lista_creadora)
    """

    vector = list()
    for _ in range(rango):
        vector.append(random.randint(min,max))

    return tuple(vector)


def mostrar_vector(vector : tuple):
    print(f"\tV = {vector}")


def mostrar_resultado(vector_1 : tuple,vector_2 : tuple,producto_escalar : int ):
    print("Vector 1:",end= "")
    mostrar_vector(vector_1)
    print("Vector 2:",end= "")
    mostrar_vector(vector_2)
    print(f"\tEl producto escalar de los vectores es : {producto_escalar}")


def producto_vectorial(vector1 : tuple,vector2 : tuple) -> tuple:
    vector = list()
    
    for elemento1 in vector1:
        vector.append(producto_numero_vector(elemento1,vector2))

    return tuple(vector)


def producto_numero_vector(numero :int,vector : tuple) -> tuple:
    resultado  = 0
    for elemento2 in vector:
            resultado += numero * elemento2

    return resultado

def producto_escalar(vector_1 : tuple,vector_2 : tuple) -> int:
    """
    
    
    
    """
    resultado = 0

    for valor in range(len(vector_1)):
        resultado += vector_1[valor] * vector_2[valor]

    """
    cont  = 0
    for elemento in vector1:
        producto += elemento * vector2[contador]
        cont += 1
    """

    return resultado


def main():
    #Para producto escalar
    """cantidad = 4
    min = -5
    max = 5

    vector1 = generar_vector(min,max,cantidad)
    vector2 = generar_vector(min,max,cantidad)

    producto = producto_escalar(vector1,vector2)

    mostrar_resultado(vector1,vector2,producto)"""
    #Para producto vectorial
    v1 = (1,2,3)
    v2 = (-1,0,2)

    print(producto_vectorial(v1,v2))




if __name__ == "__main__":
    main()