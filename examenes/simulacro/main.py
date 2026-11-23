from personaje import Personaje
from hombre import Hombre
from elfo import Elfo

def cargar_personajes(ruta_fichero: "Personajes.txt"):
    
    elfoLista = []
    hombreLista = []
    archivo = None

    try:
        # 1. Intentamos abrir y leer el fichero
        archivo = open(ruta_fichero, "r", encoding="utf-8")
        contenido = archivo.read()
        print("Contenido del fichero leído con éxito:")
        print(contenido)

        for num_linea, linea in enumerate(contenido.splitlines(), start=1):
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue  

            datos = [campo.strip() for campo in linea_limpia.split(",")]

            if len(datos) != 5:
                print(f"[AVISO] Línea {num_linea} ignorada: formato incorrecto.")
                continue
            
            try:
                nombre = datos[0]
                nivel = int(datos[1])
                altura = float(datos[2])
                atributo_especifico = datos[3]
                naturaleza = datos[4].lower()
                
                if naturaleza == "inmortal":
                    elfoLista.append(Elfo(nombre,nivel,altura,atributo_especifico))
                    
                elif naturaleza == "mortal":
                    hombreLista.append(Hombre(nombre,nivel,altura,atributo_especifico))
                    
                else:
                    print(f'En la linea {num_linea} no se conoce la naturaleza {naturaleza}')
                    
            except ValueError as error:
                print(f"[ERROR DE DATOS] Línea {num_linea} corrupta ({error}).")
                    
    except FileNotFoundError:
        print("Error: El archivo 'Personajes.txt' no fue encontrado.")
    except ValueError as error:
        print(f'Error de valor: {error}')
    except OSError as error:
        print(f"Error de entrada/salida: {error}")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

    finally:
        
        if archivo is not None and not archivo.closed:
            archivo.close()
            print("🔒 Acción de limpieza: El fichero se ha cerrado correctamente.")
        else:
            print("🔒 Acción de limpieza: El flujo finalizó sin necesidad de cerrar ficheros abiertos.")

    return elfoLista, hombreLista
            
if __name__ == "__main__":
    elfoLista, hombreLista = cargar_personajes(
     "/workspaces/Estructuras/examenes/simulacro/Personajes.txt"
     )
    
    print("Lista de Elfos por orden de inserción:")
    for elfo in elfoLista:
        print(elfo)

    print("Lista de hombres por orden de inserción:")
    for hombre in hombreLista:
        print(hombre)


        
        
        