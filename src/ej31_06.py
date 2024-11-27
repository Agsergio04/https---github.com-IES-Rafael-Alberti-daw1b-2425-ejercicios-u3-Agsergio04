def pedir_nota():
    return float(input("Introduce la nota de la asignatura: "))


def pedir_asignuatura():
    return input("Introduce la asignatura de la cual vas a guardar la nota: ")

def main():
    asignaturas = []
    notas = []
    try:
        cantidad_notas = int(input("¿Cuantas asignaturas vas a introducir?\n"))

        for _ in range(cantidad_notas):
            asignatura = pedir_asignuatura()
            nota = pedir_nota()
            if nota < 0:
                raise ValueError("**ERROR**\nIntroduce una nota valida.")
            
            if nota < 5:
                asignaturas.append(asignatura)
                notas.append(nota)
            
        print(f"Tienes que recuperar {len(asignatura)} asignaturas las cuales son: ")
        for entidad in range(len(notas)):
            print(f"En {asignaturas[entidad]} has sacado {notas[entidad]:.2f}")

    except ValueError:
        print("**ERROR**\nIntroduce un valor valido.")


if __name__ == "__main__":
    main()