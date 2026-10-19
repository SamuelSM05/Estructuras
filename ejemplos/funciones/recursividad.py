def factorial(n):
    # Case base
    if n <= 1:
        return 1
    # Recursividad
    return n*factorial(n-1)

print(factorial(999))