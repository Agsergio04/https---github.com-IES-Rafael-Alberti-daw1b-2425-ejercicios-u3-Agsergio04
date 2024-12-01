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
    return input(f"{cadena}\n>").lower().split("/")


def encontrar_clave_diccionario(diccionario : dict, valor: int):
    resultado = None

    for clave, key in diccionario.items():
        if key == valor:
            resultado = clave

    return resultado 


def comprobar_longitud(dia : int, mes : int, anio : int) -> bool:
    return 0 < len(str(dia)) <= 2 and 0 < len(str(mes)) <= 2 and len(str(anio)) == 4


def comprobar_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))


def dias_en_mes(mes: int, anio: int) -> int:
    dia = 31
    if mes == 2:
        if comprobar_bisiesto(anio):
            dia = 29  
        else:
            dia = 28
    elif mes in [4, 6, 9, 11]:
        dia = 30

    else:
        return dia
    


def comprobar_fecha(dia : int, mes : int, anio : int) -> bool:
    condicion = True

    if not comprobar_longitud(dia, mes, anio):
        condicion = False

    if mes < 1 or mes > 12:
        condicion = False
        
    if dia < 1 or dia > dias_en_mes(mes, anio):
        condicion = False
    return condicion 


def mostrar_resultado(fecha : dict, meses : dict):
    clave = encontrar_clave_diccionario(meses, fecha["mes"])
    if clave:
        print(f"{fecha['dia']} del {clave} de {fecha['anio']}")
    else:
        print("Mes inválido.")


def main():
    fecha = {
        "dia" : 0,
        "mes" : 0,
        "anio"  : 0
    }

    meses = {
        "enero" : 1,
        "febrero" : 2,
        "marzo" : 3,
        "abril" : 4,
        "mayo" : 5,
        "junio" : 6,
        "julio" : 7,
        "agosto" : 8,
        "septiembre" : 9,
        "octubre" : 10,
        "noviembre" : 11,
        "diciembre" : 12
    }
    limpiar_pantalla()
    entrada = [1]
    
    while entrada[0] != "salir":
        entrada = pedir_usuario("Introduce una fecha separada por '/' o escribe 'salir' para salir")

        if len(entrada) == 3:
            try:
                dia, mes, anio = map(int, entrada)
                fecha["dia"], fecha["mes"], fecha["anio"] = dia, mes, anio

                if comprobar_fecha(dia, mes, anio):
                    mostrar_resultado(fecha, meses)
                else:
                    print("La fecha introducida no es valida")

            except ValueError:
                print("Por favor ingrese una fecha valida en el formato día/mes/año.")
                
            except TypeError:
                print("La fecha introducida no es valida.")

        elif entrada[0] == "salir":
            limpiar_pantalla()
            print("\n\tADIOS ! ! !")

        else: 
            print("Por favor ingrese la fecha en el formato correcto.")
        
        pausa(0, True, True) 

    


if __name__ == "__main__":
    main()
