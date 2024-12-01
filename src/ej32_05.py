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
    return input(f"{cadena}\n>").lower().split(" ")


def comprobar_conjunto(lista : list) -> bool:
    return str(lista[1]).isdigit()


def crear_diccionario()-> dict:
    diccionario_asignaturas = {}

    entrada = [0]

    limpiar_pantalla()
    while entrada[0]!= "salir":
        
        entrada = pedir_usuario("Introduce la asignatura que quieras añadir junto con su nota separadas con un espacio")

        if not entrada[0] == "salir":
            if comprobar_conjunto(entrada):
                diccionario_asignaturas[entrada[0]] = entrada[1]
            else:
                print("Introduce el conjunto Asignaturas Creditos correctamente\n")
                pausa(0,True,True)

        limpiar_pantalla()
       
    return diccionario_asignaturas


def mostrar_asignaruta(diccionario : dict):
    suma = 0
    
    for asignatura in diccionario:
        credito = diccionario[f"{asignatura}"]
        
        print(f"La {asignatura} tiene {credito} ")
        suma += int(credito)

    print(f"\nLos creditos totales que posee es {suma}")
    pausa(0,True,True)


def main():
    diccionario = crear_diccionario()

    mostrar_asignaruta(diccionario)

if __name__ == "__main__":
    main()