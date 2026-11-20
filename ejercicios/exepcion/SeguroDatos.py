import argparse


class FicheroVacioError(Exception):
    """Indica que el fichero no contiene números enteros procesables."""


def sumar_enteros(ruta: str) -> int:
    total = 0
    numeros_validos = 0

    with open(ruta, "r", encoding="utf-8") as fichero:
        for numero_linea, linea in enumerate(fichero, start=1):
            try:
                numero = int(linea.strip())
            except ValueError:
                print(
                    f"Advertencia: la línea {numero_linea} no contiene "
                    "un número entero válido; se omite."
                )
                continue

            total += numero
            numeros_validos += 1

    if numeros_validos == 0:
        raise FicheroVacioError(
            "El fichero está vacío o no contiene números enteros válidos."
        )

    return total


def main(ruta: str | None = None) -> None:
    try:
        if ruta is None:
            try:
                ruta = input("Introduce el nombre del fichero: ")
            except KeyboardInterrupt:
                print("\nEjecución cancelada. ¡Hasta luego!")
                return

        try:
            total = sumar_enteros(ruta)
        except FileNotFoundError:
            print(f"Error: no se encontró el fichero '{ruta}'.")
        except PermissionError as error:
            print(f"Error: no hay permiso para leer el fichero '{ruta}': {error}")
        except OSError as error:
            print(f"Error de entrada/salida al leer '{ruta}': {error}")
        except FicheroVacioError as error:
            print(f"Sin datos procesables: {error}")
        else:
            print(f"Suma total: {total}")
    finally:
        print("Proceso de lectura finalizado")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Suma los números enteros de un fichero de texto."
    )
    parser.add_argument(
        "fichero",
        nargs="?",
        help="ruta del fichero (si se omite, se solicitará por teclado)",
    )
    argumentos = parser.parse_args()
    main(argumentos.fichero)