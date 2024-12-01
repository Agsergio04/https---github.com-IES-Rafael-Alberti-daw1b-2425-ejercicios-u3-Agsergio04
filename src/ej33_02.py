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
    return input(f"{cadena}\n>").lower().capitalize()


def set_alumno_primaria() -> set:
    conjunto = set()
    bandera = True

    while bandera:
        limpiar_pantalla()
        entrada =  pedir_usuario("Introduce el nombre de pila del alumno de primaria,escribe 'x' para salir")

        if entrada == 'x':
            bandera = False

        conjunto.add(entrada)

    return conjunto


def set_alumno_secundaria() -> set:
    conjunto = set()
    bandera = True

    while bandera:
        limpiar_pantalla()
        entrada =  pedir_usuario("Introduce el nombre de pila del alumno de secundaria,escribe 'x' para salir")

        if entrada == 'x':
            bandera = False
            
        conjunto.add(entrada)

    return conjunto


def mostrar_resultado(primaria : set,secundaria : set):
    limpiar_pantalla()

    print(f"Nombres de alumnos de primaria:\n{primaria}\nNombres de alumnos de secundaria:\n{secundaria}")
    print(f"Nombres que se repiten entre los alumnos de primaria y secundaria {primaria | secundaria}")
    print(f"Nombres de primaria no se repiten en secundaria {primaria - secundaria}")
    print(f"Nombres de primaria que  estan  incluidos en secundaria {primaria & secundaria}")

    pausa(0,True,True)


def main():
   primaria = set_alumno_primaria()
   secundaria = set_alumno_secundaria()

   mostrar_resultado(primaria,secundaria)

if __name__ == "__main__":
    main()