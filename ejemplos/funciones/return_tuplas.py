def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo de una lista"""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo  # Devuelve una tupla

# Desempaquetado de valores
suma, prom, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val}")
# Salida: Suma: 150, Promedio: 30.0, Máximo: 50