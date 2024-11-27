def particion_abecedario_espacios(cadena : str) -> list:
    return cadena.split(" ")


def multiplo_tres_lista(lista : list) -> list:
    return lista[::3]


def muestra(lista : list):
    cadena = "->"
    for elemento in lista:
        cadena += elemento + " " 
    print(cadena)

def quitar_palabras(lista1 : list,lista2 : list):

    for elemento in lista1:
        if elemento in lista2:
            lista1.remove(elemento)

    return lista1

    

def main():
    cadena = "a b c d e f g h i j k m n ñ o p q r s t u v w x y z"
    abecedario = particion_abecedario_espacios(cadena)

    lista_quitar = multiplo_tres_lista(abecedario)

    lista_resultado = quitar_palabras(abecedario,lista_quitar)

    print("Aqui tienes la lista del abecedario  sin las palabras que son multiplos de 3:")
    muestra(lista_resultado)

if __name__ == "__main__":
    main()