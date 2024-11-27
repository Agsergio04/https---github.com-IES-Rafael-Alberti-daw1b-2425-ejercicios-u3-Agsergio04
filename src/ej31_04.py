def pedir_numero():
    return input("Introduce el numero de la primitiva: ")


def main():
    lista_voletos = []
    entrada = None

    print("Introduce los numeros ganadores de la primitiva(escribe salir para salir)")
    try: 
        while entrada != "salir":
            entrada = pedir_numero().lower()

            if entrada.isdigit():
                lista_voletos.append(int(entrada))

    except TypeError():
        print("**ERROR**\nIntroduce un valor.")

    lista_voletos.sort()
    
    print(f"Estos son los numeros ordenados de menor a mayor:\n{lista_voletos}")


if __name__ == "__main__":
    main()