from PersonajeTeletubby import PersonajeTeletubby

tinky_winky = PersonajeTeletubby("Tinky Winky", "morado", "triangulo", "bolso")
po = PersonajeTeletubby("Po", "rojo", "circulo", "patinete")

tinky_winky.saludar()
po.saludar()

tinky_winky.jugar()
po.jugar()

print("\nEstado despues de jugar:")
tinky_winky.ver_estado()
po.ver_estado()

tinky_winky.comer_tubby_papilla()

print("\nEstado final:")
tinky_winky.ver_estado()
po.ver_estado()

print(po)
