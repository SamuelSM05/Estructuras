code = int(input("Introduce el codigo de estado: "))

match code:
    case 200 | 201:
        print("EXITOOOOOOO")
    case code if 400 <= code >= 404:
        print(" Error de cliente")
    case 500 | 503:
        print ("Error de servidor")
    case _ :
        print("Codigo de estado no reconocido")