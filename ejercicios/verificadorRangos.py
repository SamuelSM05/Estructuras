temp = float(input(("Introduce una temperatura: ")))

if 18 <= temp <= 27:
    print("Temperatura optima")
elif temp < 18:
    print("Cuidado que refresca")
elif temp > 27:
    print("Se nota el calufo ya")
