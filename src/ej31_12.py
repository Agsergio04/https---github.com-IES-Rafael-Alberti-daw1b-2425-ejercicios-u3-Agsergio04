def producto_escalar(vector_1 : tuple,vector_2 : tuple) -> int:
    resultado = 0

    for valor in range(len(vector_1)):
        resultado += vector_1[valor] * vector_2[valor]

    return resultado


def producto(matriz1: tuple[tuple],matriz2 : tuple[tuple]) -> tuple[tuple]:
    #columnas_m1 = len(matriz1[0]) if len(matriz1) > 0 else 0
    # Version simplificada(tradicional)      
    
    #Dimensiones matriz 1
    filas_m1 = len(matriz1)

    if len(matriz1) > 0:
        columnas_m1 = len(matriz1[0])
    else:
        columnas_m1 = 0

    #Dimensiones matriz 2
    filas_m2 = len(matriz2)

    if len(matriz2) > 0:
        columnas_m2 = len(matriz2[0])
    else:
        columnas_m2 = 0

    if columnas_m1 != filas_m2:
        return None

    producto = list()

    for vector1 in matriz1:
        elemento = list()
        
        for col in range(columnas_m2):
            vector2 = list()
            
            for fila in range(filas_m2):
                vector2.append(matriz2[fila][col])
            elemento.append(producto_escalar(vector1,vector2))

        producto.append(elemento)

    return producto

def main():
    matriz_a = (
        (1,2,3),
        (4,5,6)
    )

    matriz_b = (
        (-1,1),
        (0,2),
        (2,3)
    )

    print(producto(matriz_a,matriz_b))


if __name__ == "__main__":
    main()

    """
    Crear una funcion que sea crear_crear matriz

    Args:
     filas:
     columnas:
     minimo:
     maximo:

    Returns.
        tuple
    """

"""
#
v3 = []

for i in range(len(matrizb[0])-1):
    fila = []
    for x in range(len(matriz_b[0])):
        resultado = 0
        for j in range(len(matriz_b)):
            resultado += matriz_a[i][j] * matriz_b[j][x]
        fila.append(resultado)
    v3.append(tuple(fila))

    return tuple(v3)

Como lo ha hecho diego:

matriz_producto = producto(matriz1,matriz2)

if matriz_produto is none


"""