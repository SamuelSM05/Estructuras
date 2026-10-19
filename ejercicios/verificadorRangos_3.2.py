nombre = input("Introduce el nombre de usuario: ").strip()
cp = input("Introduce el codigo postal: ").strip()

if not nombre:
    print("El nombre de usuario esta vacio")
if not cp.isdigit():
    print("El codigo postal no es un digito")
if nombre and cp.isdigit():
    print(f"Registro Valido. '{nombre}' | CP: {cp}")