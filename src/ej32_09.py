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
    return float(input(f"{cadena}\n>"))


def titulo():
    print('-' * 38)
    print("\t GESTION DE FACTURAS")
    print('-' * 38 + "\n")

def mostrar_menu():
    limpiar_pantalla()
    titulo()
    print("1.- Añadir una nueva factura.")
    print("2.- Pagar factura existente.")
    print("3.- Total a pagar.")
    print("4.- Total pagado.")
    print("5.- Salir.")


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
    
 

def mostrar_resultado(frase : str):
    print("Aqui esta la frase con la traduccion aplicada:\n")
    print(frase)
    pausa(0,True,True)

def menu():
    facturas_empresa = {
        "pagado" : 0,
        "facturas" : {},
        "monto_pagar" : 0
    }
        
    
    decision = None

    while decision != 5.0:
        try:
            mostrar_menu()

            decision = pedir_usuario("")

            limpiar_pantalla()
            if decision == 1.0:
                id_factura = pedir_usuario("escribe la id de la factua a agregar: ")
                monto = pedir_usuario("¿De cuanto va a ser la factua a agregar?")

                facturas_empresa["facturas"][id_factura] = monto

            elif decision == 2.0:
                id_factura = pedir_usuario("Escribe la ID de la factura a pagar:")

                if id_factura in facturas_empresa["facturas"]:
                    monto_factura = facturas_empresa["facturas"][id_factura]

                    print(f"La factura {id_factura} tiene un monto pendiente de {monto_factura:.2f}\n")

                    monto_a_pagar = pedir_usuario("¿Cuánto deseas pagar de esta factura?")

                    if monto_a_pagar >= monto_factura:
                        
                        facturas_empresa["pagado"] += monto_factura
                        facturas_empresa["facturas"].pop(id_factura)

                        print(f"\nFactura {id_factura} pagada completamente\n")

                    else:
                        
                        facturas_empresa["pagado"] += monto_a_pagar
                        facturas_empresa["facturas"][id_factura] -= monto_a_pagar

                        print(f"\nSe pagaron {monto_a_pagar:.2f} de la factura {id_factura}")
                        print(f"Quedan {facturas_empresa['facturas'][id_factura]:.2f} por pagar\n")
                else:
                    print(f"No se encontró una factura con la ID {id_factura}")

                pausa(0, True, True)
            
            elif decision == 3.0:
                suma_facturas = sum(facturas_empresa["facturas"].values())
                facturas_empresa.update({"monto_pagar": suma_facturas})

                print(f"El dinero necesario para pagar todas las faturas es {facturas_empresa["monto_pagar"]}")
                pausa(0,True,True)

                """
                Sobrepisando el valor:
                
                suma_facturas = sum(facturas_empresa["facturas"].values())
                facturas_empresa["monto_pagar"] = suma_facturas
                
                """

            elif decision == 4.0:
                print(f"El total pagado de las facturas es {facturas_empresa['pagado']}")
                pausa(0,True,True)

            elif decision == 5.0:
                limpiar_pantalla()

            else:
                raise ValueError("Introduce una opcion valida")

        
        except ValueError as mensaje:
            print(f"**ERROR**\n{mensaje}.")
            
            

    

def main():
   menu()



if __name__ == "__main__":
    main()


    