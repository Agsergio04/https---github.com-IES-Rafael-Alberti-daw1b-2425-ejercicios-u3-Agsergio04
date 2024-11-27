def main():
    lista = []

    for numero in range(1, 11):
        lista.append(numero)

    
    lista = lista[::-1]
    cadena_imprimir = ""

    for valor in lista:
        cadena_imprimir += str(valor) + ", "
    
    cadena_imprimir = cadena_imprimir.strip(", ")
    print(cadena_imprimir)


if __name__ == "__main__":
    main()


"""
Otra forma

for valor in lista:
    res += f"{valor}, "

print(res[:-2])

for in range (len(lista)):
    res += f"{lista[i]},"

"""