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


def pedir_usuario(cadena: str) -> str:
    return input(f"{cadena}\n>")



def obtener_precio(fruta : str, kilos : int,fruteria : dict):
    precio_total = None

    if fruta in fruteria["fruta"]:
        
        indice_precio = fruteria["fruta"].index(fruta)
        
        precio_total = fruteria["precio"][indice_precio] * kilos

    return precio_total


def mostrar_resultado(fruta_usuario : str,kilos : str,precio : float):
    pausa(0,False,True)

    if precio is not None:
        print(f"El precio de {kilos} kilos de {fruta_usuario} es: {precio:.2f}€")

    else:
        print("La fruta no esta en la frutería.")

    pausa(0,True,True)


def main():
    fruteria ={
        "fruta" : ["platano","manzana","pera","naranja"],
        "precio": [1.35,0.80,0.85,0.70]
    }
    fruta_usuario = ""

    limpiar_pantalla()

    while fruta_usuario.lower() != "salir":
        print("Las frutas disponibles son (platano,manzazna,pera y naranja)")
        fruta_usuario = pedir_usuario("¿Que fruta deseas comprar? (salir para salir): ").lower()
        kilos = pedir_usuario("¿Cuántos kilos deseas comprar? (presiona enter para salir)")

        if fruta_usuario != "salir":
            precio = obtener_precio(fruta_usuario,float(kilos),fruteria)
            
            mostrar_resultado(fruta_usuario,kilos,precio)
        
    limpiar_pantalla()
    



if __name__ == "__main__":
    main()
