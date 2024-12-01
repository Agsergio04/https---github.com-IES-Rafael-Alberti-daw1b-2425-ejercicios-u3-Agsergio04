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

def comprobar_numero(numero: str) -> bool:
    
    
    #Comprovar si es un numero negativo
    if numero.startswith("-"):
        numero = numero[1:]
        
    #Metodo para intercambiar comas por puntos
    if numero.count(",") > 0:  
        numero = numero.replace(",",".")
        
    #Comprovar el numero si tene decimales  
    if numero.count(".") <= 1:
        
        numero = numero.replace(".","")
    
        
    return  numero.isdigit()


def mostrar_resultado(diccionario : dict):
    suma =  0
    limpiar_pantalla()

    print('-' * 32 + "\n" + "\Lista de la compra\n" + '-' * 32 + "\n")
    for objeto,precio in diccionario.items():
        print(f"{objeto} : {precio}")
        suma += float(precio)

    print(f"\nTotal : {suma:.2f}")
    pausa(0,True,True)

    print("\n\n\t Adios ! ! !")


def menu():
    lista_compra = {}
    objeto,precio =None,None 

    while objeto != "salir" or precio != "salir":
        limpiar_pantalla()

        objeto = pedir_usuario("Que producto deseas añadir,escribe 'salir' para salir?")
        precio = pedir_usuario(f"¿Que precio le deseas añadir a {objeto},escribe 'salir' para salir?")

        if comprobar_numero(precio):

            if objeto != "salir" and precio != "salir":
                lista_compra[f"{objeto}"] = precio

            if objeto in lista_compra:
                lista_compra.update({objeto: precio})
        
        if not comprobar_numero(precio) and objeto != "salir" and precio != "salir":
            print("Por favor ingrese un precio valido\n")
            pausa(0,True,True)


    mostrar_resultado(lista_compra)

def main():
   menu()



if __name__ == "__main__":
    main()