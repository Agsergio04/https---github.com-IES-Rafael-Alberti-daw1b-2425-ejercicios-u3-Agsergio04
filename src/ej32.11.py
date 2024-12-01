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


def convertir_directorio_a_diccionario(directorio: str) -> dict:
    lineas = directorio.split('\n')  
    encabezados = lineas[0].split(';') 

    clientes = {}

    for linea in lineas[1:]:
        datos = linea.split(';')  
        nif = datos[0]  

        cliente_info = {}  

        
        for i in range(1, len(encabezados)):

            clave = encabezados[i]  

            if clave == "descuento":
                valor = float(datos[i])

            else:
                valor = datos[i]

            cliente_info[clave] = valor
        
      
        clientes[nif] = cliente_info

    return clientes

def mostrar_resultado(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    
    pausa(0,True,True)


def main():
    limpiar_pantalla()

    cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    clientes_diccionario = convertir_directorio_a_diccionario(cadena)

    print("Este es la informacion de cada persona: ")
    mostrar_resultado(clientes_diccionario)

    

if __name__ == "__main__":
    main()

