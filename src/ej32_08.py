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


def traduccion_palabras_frase(diccionario : dict,frase : str):
    limpiar_pantalla()

    palabras = frase.split() 
    frase_traducida = []

    for palabra in palabras:
        # Cambia la palabra si esta en el diccionario
        frase_traducida.append(diccionario.get(palabra.lower(), palabra))

    frase_resultado = " ".join(frase_traducida)  
    
    mostrar_resultado(frase_resultado)
 

def mostrar_resultado(frase : str):
    print("Aqui esta la frase con la traduccion aplicada:\n")
    print(frase)
    pausa(0,True,True)

def menu():
    diccionario = {}
    palabra,traduccion =None,None 

    while palabra != "salir" or traduccion != "salir":
        limpiar_pantalla()

        palabra = pedir_usuario("¿Que caracteristica deseas añadir,escribe 'salir' para salir?")
        traduccion = pedir_usuario(f"¿Que traduccion le deseas añadir a {palabra},escribe 'salir' para salir?")

        if palabra != "salir" and traduccion != "salir":
            diccionario[f"{palabra}"] = traduccion

        if palabra in diccionario:
            diccionario.update({palabra: traduccion})

    limpiar_pantalla()

    frase = pedir_usuario("Introduce una frase para poder traducir algunas palabras:")

    traduccion_palabras_frase(diccionario,frase)

def main():
   menu()



if __name__ == "__main__":
    main()


    