import random
base = int(input("Declara la base:"))
for  j in range (1,base + 1):
    for i in range (j):
        aleatorio = random.randint(1,9)
        print(f"{aleatorio} ", end="")
    print()
    
        