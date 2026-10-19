def sumar_todos(*numeros):
# """Suma cualquier cantidad de numeros"""
    total = 0

    for num in numeros:

        total += num

    return total

print (sumar_todos (1, 2, 3))
print (sumar_todos (10, 20, 30, 40))
print (sumar_todos (5) )

# 6
# 100
# 5


def crear_perfil(**datos):
    """Crea un perfil de usuario con datos variables"""
    print("Perfil de usuario:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

crear_perfil(nombre="Ana", edad=25, ciudad="Madrid")
# Perfil de usuario:
#   nombre: Ana
#   edad: 25
#   ciudad: Madrid

crear_perfil(nombre="Carlos", profesion="Ingeniero", pais="España", hobby="Ciclismo")
# Perfil de usuario:
#   nombre: Carlos
#   profesion: Ingeniero
#   pais: España
#   hobby: Ciclismo