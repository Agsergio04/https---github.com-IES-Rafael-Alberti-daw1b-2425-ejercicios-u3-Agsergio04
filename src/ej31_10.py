import time
import os

def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    if tecla_enter:
        input("\nPresione ENTER para continuar...")
    elif tiempo > 0:
        time.sleep(tiempo)
    
    if limpiar:
        limpiar_pantalla()



def titulo():
    print('-' * 32)
    print("ORDENAR CONJUNTOS")
    print('-' * 32)



def limpiar_pantalla():
    try:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    except Exception as e:
        print(f"Problemas al intentar limpiar la pantalla: {e}")


def menu():
    lista = [50, 75, 46, 22, 80, 65, 8]
    
    mostrar_resultado(lista)


def mayor_menor(lista : list) -> tuple:
    lista.sort()

    numero_mayor,numero_menor = lista[-1],lista[0]

    return numero_menor,numero_mayor

def mostrar_resultado_mayor_menor(lista : list):
    menor,mayor = mayor_menor(lista)

    print(f"El numero mas pequeño de los valores dados es {menor}")
    print(f"El numero mas grande de los valores dados es {mayor}")


def mostrar_resultado(lista : list):
    pausa(0,False,True)

    titulo()
    print(f"Dada la lista:\n{lista}\n\nTenemos que: \n")
    mostrar_resultado_mayor_menor(lista)

    pausa(0,True,True)


def main():
    menu()


if __name__ == "__main__":
    main()