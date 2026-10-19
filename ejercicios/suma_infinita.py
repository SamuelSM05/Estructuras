suma = 0

while True:
    declaracion = input("Numero a sumar (escribie Salir para no sumar mas):")
    
    if declaracion == "salir":
        print("Saliendo.....")
        break

    suma += int(declaracion)
    
    print(f"La suma es: {suma} ")