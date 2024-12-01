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
    return input(f"{cadena}\n>").lower().strip()


def mostrar_resultado(diccionario : dict):
    limpiar_pantalla()

    print('-' * 32 + "\n" + "\tFicha del Usuario\n" + '-' * 32 + "\n")
    for clave,valor in diccionario.items():
        print(f"{clave} : {valor}")

    pausa(0,True,True)

    print("\n\n\t Adios ! ! !")


def menu():
    persona = {}
    clave,valor =None,None 

    while clave != "salir" or valor != "salir":
        limpiar_pantalla()

        clave = pedir_usuario("¿Que caracteristica deseas añadir,escribe 'salir' para salir?")
        valor = pedir_usuario(f"¿Que valor le deseas añadir a {clave},escribe 'salir' para salir?")

        if clave != "salir" and valor != "salir":
            persona[f"{clave}"] = valor

        if clave in persona:
            persona.update({clave: valor})


    mostrar_resultado(persona)

def main():
   menu()



if __name__ == "__main__":
    main()


    """
    Diccionario final:
    nombre : ...
    edad: ...

    fin para acabar de añadir y actualizar
    """