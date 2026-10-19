valid_input = False
attempts = 0
max_attempts = 3

while not valid_input and attempts < max_attempts:
    password = input("Ingresa tu contraseña: ")
    if len(password) >= 8:
        print("Contraseña válida")
        valid_input = True
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Contraseña muy corta. Intentos restantes: {remaining}")

if not valid_input:
    print("Máximo de intentos alcanzado")