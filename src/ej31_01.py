def pedir_asignuatura():
    return input("Introduce la asignatura de la cual vas a guardar la nota: ")

def main():
    asignaturas = []
    try:
        cantidad_notas = int(input("¿Cuantas asignaturas vas a introducir?\n"))

        for _ in range(cantidad_notas):
            asignatura = pedir_asignuatura()
            
            asignaturas.append(asignatura)
    
        for entidad in range(cantidad_notas):
            print(f"{asignaturas[entidad]}")

    except ValueError():
        print("**ERROR**\nIntroduce un valor valido.")
    except TypeError():
        print("**ERROR**\nIntroduce un valor.")


if __name__ == "__main__":
    main()