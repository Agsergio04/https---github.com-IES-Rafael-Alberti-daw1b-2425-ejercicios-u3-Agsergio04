import time
import os

def pausa(tiempo=0, tecla_enter=False, limpiar=True):
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

def mostrar_personas(personas: dict):
    limpiar_pantalla()
    print("Datos de todas las personas ingresadas:")
    for nombre, datos in personas.items():
        print(f"\n{nombre} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}.")

def menu():
    personas = {}
    cantidad_personas = pedir_usuario("¿Cuántas personas deseas ingresar?")

    for _ in range(int(cantidad_personas)):
        
        usuario = {}
        
        
        usuario["nombre"] = pedir_usuario("¿Cuál es tu nombre?")
        usuario["edad"] = pedir_usuario("¿Cuántos años tienes?")
        usuario["direccion"] = pedir_usuario("¿Cuál es tu dirección?")
        usuario["telefono"] = pedir_usuario("¿Cuál es tu número de teléfono?")
        
        
        personas[usuario["nombre"]] = usuario
        
        
        pausa(1, False, True)

   
    mostrar_personas(personas)

def main():
    menu()

if __name__ == "__main__":
    main()
