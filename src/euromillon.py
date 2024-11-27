import random
import os
import time



def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    if tecla_enter:
        input("\nPresione ENTER para continuar...")
    elif tiempo > 0:
        time.sleep(tiempo)
    
    if limpiar:
        limpiar_pantalla()


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear' (os.name == "posix").
    """
    # Una forma:
    try:
        # Debe funcionar en todos los sistemas operativos
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    except Exception as e:
        print(f"Problemas al intentar limpiar la pantalla: {e}")


def generar_euromillon(numero : int,estrellas : int,cantidad : int) -> tuple:
    lista_numero1 = []
    lista_numero2 = []
    contador = 0

    while contador < cantidad:
        numero1 = random.randint(1,numero)

        if numero1 not in lista_numero2:
            lista_numero2.append(numero1)
            contador += 1
    
    while contador < cantidad + 2:
        numero2 = random.randint(1,estrellas)

        if numero2 not in lista_numero1:
            lista_numero1.append(numero2)
            contador += 1

    return lista_numero1,lista_numero2


def preguntar_usuario()-> str:
    return int(input(">"))


def mostrar_resultado(numeros : list,estrellas : list):
    cadena_numero = ""
    cadena_estrellas = ""

    numeros.sort()
    estrellas.sort()
    #Para la cadena de numeros
    
    for valor in numeros:
        cadena_numero += f"{valor}-"
    
    cadena_numero = "* " + cadena_numero

    #Para la cadena de estrellas

    for numero in estrellas:
        cadena_estrellas += f"{numero} y "

    cadena_estrellas = "* " + cadena_estrellas
    
    print(cadena_numero[:-1])
    print(cadena_estrellas[:-2])


def mostrar_configuracion_dias():
    titulo()
    print("\t1.- Para modificar el rango de los numeros que salen.")
    print("\t2.- Para modificar el rango de las estrellas que salen.")
    print("\t3.- Para modificar la cantidad de numeros que salen.")
    print("\t4.- Para salir.\n")


def titulo():
    print('-' * 46)
    print("\t\tEUROMILLON")
    print('-' * 46)

def mostrar_menu():
    titulo()
    print("\t1.- Para mostrar los numeros")
    print("\t2.- Configurarcion ")
    print("\t3.- Salir\n")


def mostrar_despedida():
    print("\nAdios ! ! ! ")


def menu_configuracion_dias(numero : int,estrellas : int,cantidad : int):
    configurar = None
    #Esto no hacerlo pq diego me mata a palos

    try:
        while configurar != 4:
            
            mostrar_configuracion_dias()
            configurar = preguntar_usuario()

            pausa(2,False,True)

            if configurar == 1:
                
                print("Indica el cambio:\n")
                numero   = preguntar_usuario()
                limpiar_pantalla()

            if configurar == 2:
                
                print("Indica el cambio:\n") 
                estrellas = preguntar_usuario()
                limpiar_pantalla()

            if configurar == 3:
                
                print("Indica el cambio:\n")
                cantidad = preguntar_usuario()
                limpiar_pantalla()

    except ValueError:
            print("**ERROR**\nIntroduce un valor valido.")

    return numero,estrellas,cantidad


def menu():
    decision = None
    numero = 50
    estrellas = 12
    cantidad = 5
    

    while decision != 3:
        try:
            mostrar_menu()
            decision = preguntar_usuario()
            limpiar_pantalla()

            pausa(1,False,False)

            if decision == 1:
                
                estrellas,numeros  = generar_euromillon(numero,estrellas,cantidad)
                mostrar_resultado(numeros,estrellas)
                pausa(0,True,False)
                limpiar_pantalla()

            if decision == 2:
                limpiar_pantalla()
                #print("Lo sentimos pero esta opcion no esta viable en estos momentos\n")
                numero,estrellas,cantidad = menu_configuracion_dias(numero,estrellas,cantidad)

            
        except ValueError:
            limpiar_pantalla()
            print("**ERROR**\nIntroduce un valor valido.\n")
        except TypeError:
            limpiar_pantalla()
            print("**ERROR**\nIntroduce un valor.\n")

    
    limpiar_pantalla()
    mostrar_despedida()

def main():
    menu()


if __name__ == "__main__":
    main()