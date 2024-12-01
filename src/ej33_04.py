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


def mostrar_resultado(frutas_comunes : set,frutas_solo_en_frutas1 : set,frutas_solo_en_frutas2 : set):
    limpiar_pantalla()

    print(f"Frutas comunes {frutas_comunes}")
    print(f"Frutas que solo estan en el conjunto de frutas primero {frutas_solo_en_frutas1}")
    print(f"Frutas que solo estan en el conjunto de frutas segundo {frutas_solo_en_frutas2}")
    

    pausa(0,True,True)


def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    frutas1_set = set(frutas1)
    frutas2_set = set(frutas2)

    frutas_comunes = frutas1_set & frutas2_set
    frutas_solo_en_frutas1 = frutas1_set - frutas2_set
    frutas_solo_en_frutas2 = frutas2_set - frutas1_set


    mostrar_resultado(frutas_comunes,frutas_solo_en_frutas1,frutas_solo_en_frutas2)

    



if __name__ == "__main__":
    main()