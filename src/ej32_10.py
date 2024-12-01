import time
import os

def pausa(tiempo: int, tecla_enter: bool, limpiar: bool):
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


def pedir_usuario(cadena: str) -> str:
    return input(f"{cadena}\n>").strip()


def titulo():
    print('-' * 38)
    print("\t GESTION DE CLIENTES")
    print('-' * 38 + "\n")


def mostrar_menu():
    limpiar_pantalla()
    titulo()
    print("1.- Añadir Cliente.")
    print("2.- Eliminar Cliente.")
    print("3.- Mostrar Cliente.")
    print("4.- Lista de todos los clientes.")
    print("5.- Lista de todos los clientes preferentes.")
    print("6.- Terminar.")


def comprobar_referente(nombre: str) -> bool:
    decision = pedir_usuario(f"¿{nombre} es preferente? (1 para si / 0 para no)")

    if decision == "1":
        condicion =  True
    else:
        condicion = False
    
    return condicion 


def añadir_datos(dni: str, diccionario: dict):
    nombre = pedir_usuario("Escribe el nombre del Cliente: ")
    direccion = pedir_usuario(f"Escribe la direccion de {nombre}")
    telefono = pedir_usuario(f"Escribe el telefono de {nombre}")
    correo = pedir_usuario(f"Escribe el correo de {nombre}")
    preferente = comprobar_referente(nombre)

    caracteristicas = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }

    diccionario[dni] = caracteristicas


def mostrar_cliente(dni: str, base_datos: dict):
    if dni in base_datos:

        cliente = base_datos[dni]

        print(f"Cliente: {dni}")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print(f"No se encontro un cliente con el DNI {dni}.")


def menu():
    base_datos = {}

    decision = None

    while decision != 6:
        try:
            mostrar_menu()

            decision = int(pedir_usuario("Seleccione una opcion"))

            limpiar_pantalla()

            if decision == 1:
                dni = pedir_usuario("Por favor, escribe el DNI del cliente que deseas añadir: ")

                añadir_datos(dni, base_datos)

                pausa(0, True, True)

            elif decision == 2:
                dni = pedir_usuario("Por favor, escribe el DNI del cliente que deseas eliminar: ")

                if dni in base_datos:
                    base_datos.pop(dni)

                    print(f"El cliente con DNI {dni} ha sido borrado exitosamente.")

                else:
                    print(f"No se encuentra el cliente con el DNI {dni} en la base de datos.")

                pausa(0, True, True)

            elif decision == 3:
                dni = pedir_usuario("Por favor, escribe el DNI del cliente que deseas ver: ")
                
                mostrar_cliente(dni, base_datos)
                
                pausa(0, True, True)

            elif decision == 4:
                print("Lista de todos los clientes:")

                for dni, cliente in base_datos.items():
                    print(f"DNI: {dni}, Caracteristicas: {cliente['caracteristicas']}")
                
                pausa(0, True, True)

            elif decision == 5:
                print("Lista de clientes preferentes:")

                for dni, cliente in base_datos.items():

                    if cliente["preferente"]:
                        print(f"DNI: {dni}, Caracteristicas: {cliente['caracteristicas']}")

                pausa(0, True, True)

            elif decision == 6:
                limpiar_pantalla()

            else:
                raise ValueError("Introduce una opción valida")

        except ValueError as mensaje:
            print(f"**ERROR**\n{mensaje}.")


def main():
    menu()


if __name__ == "__main__":
    main()
    