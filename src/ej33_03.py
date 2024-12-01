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


def conjunto_potencia(conjunto_original : set) -> list:
    potencia = [set()]

    for elemento in conjunto_original:
        nuevos_subconjuntos = []

        for subconjunto in potencia:

            nuevos_subconjuntos.append(subconjunto | {elemento})

        potencia.extend(nuevos_subconjuntos)

    return potencia

def main():
    conjunto = {6,1,4}

    subconjuntos = conjunto_potencia(conjunto)

    print(subconjuntos)


if __name__ == "__main__":
    main()