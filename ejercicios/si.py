# a = int(input(("Introduce un numero entero: ")))

# b = int(input(("Introduce otro numero entero: ")))

# if a > 0 and b > 0:
#     print ("Ambos numeros son positivos")
# elif a > 0 or b > 0:
#     print ("Solo uno de los numeros es positivo")

# else:
#     print ("Ninguno de los numeros es positivo")
    
nota = int(input(("Introduce una nota: ")))

match nota:
    case nota if 0 <= nota < 5:
        print ("Suspenso")
    case nota if nota >= 5 and nota < 7:
        print ("Aprobado")
    case nota if nota >= 7 and nota < 8.5: 
        print ("Notable")
    case nota if nota >= 8.5 and nota <= 10:
        print ("Sobresaliente")
    case _:
        print("Duro")

